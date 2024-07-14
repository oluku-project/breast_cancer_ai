from django import template

register = template.Library()


@register.filter
def gender_to_avatar(gender):
    value = 13 if gender == "Male" else 16
    return value


@register.simple_tag(takes_context=True)
def update_registration_session(context):
    request = context["request"]
    request.session["registration_success"] = False
    if "registration_success" in request.session:
        success = request.session.pop("registration_success")
        return success
    return False
