# patients/management/commands/flush_models.py
from django.core.management.base import BaseCommand
from django.apps import apps
from django.db import connection


class Command(BaseCommand):
    help = "Flush data for specified models and reset primary key sequences"

    def add_arguments(self, parser):
        parser.add_argument(
            "models",
            nargs="+",
            type=str,
            help="The models to flush (e.g., app_label.ModelName)",
        )

    def handle(self, *args, **options):
        models = options["models"]

        for model_name in models:
            try:
                app_label, model = model_name.split(".")
                Model = apps.get_model(app_label, model)
            except (ValueError, LookupError) as e:
                self.stdout.write(
                    self.style.ERROR(f"Invalid model name: {model_name} ({e})")
                )
                continue

            Model.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(f"Successfully flushed {model_name} data")
            )

            # Reset primary key sequence
            if connection.vendor == "postgresql":
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"SELECT setval(pg_get_serial_sequence('{Model._meta.db_table}', 'id'), 1, false);"
                    )
            elif connection.vendor in ("sqlite", "mysql"):
                with connection.cursor() as cursor:
                    cursor.execute(
                        f"UPDATE sqlite_sequence SET seq = 0 WHERE name = '{Model._meta.db_table}';"
                    )

            self.stdout.write(
                self.style.SUCCESS(f"Reset primary key sequence for {model_name}")
            )
