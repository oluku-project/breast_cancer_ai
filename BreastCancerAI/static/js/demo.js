$(function () {
  'use strict';

  // Get access to plugins
  $('[data-toggle="control-sidebar"]').controlSidebar();
  $('[data-toggle="push-menu"]').pushMenu();

  var $pushMenu = $('[data-toggle="push-menu"]').data('lte.pushmenu');
  var $controlSidebar = $('[data-toggle="control-sidebar"]').data(
    'lte.controlsidebar'
  );
  var $layout = $('body').data('lte.layout');

  var mySkins = [
    'theme-primary',
    'theme-secondary',
    'theme-info',
    'theme-success',
    'theme-danger',
    'theme-warning',
  ];

  function get(name) {
    if (typeof Storage !== 'undefined') {
      return localStorage.getItem(name);
    } else {
      window.alert(
        'Please use a modern browser to properly view this project!'
      );
    }
  }

  function store(name, val) {
    if (typeof Storage !== 'undefined') {
      localStorage.setItem(name, val);
    } else {
      window.alert(
        'Please use a modern browser to properly view this project!'
      );
    }
  }

  function changeLayout(cls) {
    $('body').toggleClass(cls);
    if ($('body').hasClass('fixed') && cls === 'fixed') {
      $pushMenu.expandOnHover();
      $layout.activate();
    }
    $controlSidebar.fix();
  }

  function changeSkin(cls) {
    $.each(mySkins, function (i) {
      $('body').removeClass(mySkins[i]);
    });

    $('body').addClass(cls);
    store('theme', cls);
    return false;
  }

  function setup() {
    var tmp = get('theme');
    if (tmp && $.inArray(tmp, mySkins) !== -1) {
      changeSkin(tmp);
    } else {
      changeSkin('theme-primary');
    }

    $('[data-theme]').on('click', function (e) {
      if ($(this).hasClass('knob')) return;
      e.preventDefault();
      changeSkin($(this).data('theme'));
    });

    $('[data-layout]').on('click', function () {
      changeLayout($(this).data('layout'));
    });

    $('[data-controlsidebar]').on('click', function () {
      changeLayout($(this).data('controlsidebar'));
      var slide = !$controlSidebar.options.slide;
      $controlSidebar.options.slide = slide;
      if (!slide) $('.control-sidebar').removeClass('control-sidebar-open');
    });

    $('[data-enable="expandOnHover"]').on('click', function () {
      $(this).attr('disabled', true);
      $pushMenu.expandOnHover();
      if (!$('body').hasClass('sidebar-collapse'))
        $('[data-layout="sidebar-collapse"]').click();
    });

    $('[data-enable="rtl"]').on('click', function () {
      $(this).attr('disabled', true);
      $pushMenu.expandOnHover();
      if (!$('body').hasClass('rtl')) $('[data-layout="rtl"]').click();
    });

    $('[data-mainsidebarskin="toggle"]').on('click', function () {
      var $sidebar = $('body');
      if ($sidebar.hasClass('dark-skin')) {
        $sidebar.removeClass('dark-skin');
        $sidebar.addClass('light-skin');
        store('theme-skin', 'light-skin');
      } else {
        $sidebar.removeClass('light-skin');
        $sidebar.addClass('dark-skin');
        store('theme-skin', 'dark-skin');
      }
    });

    var skin = get('theme-skin');
    if (skin) {
      $('body').removeClass('dark-skin light-skin').addClass(skin);
    } else {
      $('body').addClass('light-skin');
    }

    if ($('body').hasClass('fixed')) {
      $('[data-layout="fixed"]').attr('checked', 'checked');
    }
    if ($('body').hasClass('layout-boxed')) {
      $('[data-layout="layout-boxed"]').attr('checked', 'checked');
    }
    if ($('body').hasClass('sidebar-collapse')) {
      $('[data-layout="sidebar-collapse"]').attr('checked', 'checked');
    }
    if ($('body').hasClass('rtl')) {
      $('[data-layout="rtl"]').attr('checked', 'checked');
    }
    if ($('body').hasClass('dark')) {
      $('[data-layout="dark"]').attr('checked', 'checked');
    }
  }

  var $tabPane = $('<div />', {
    id: 'control-sidebar-theme-demo-options-tab',
    class: 'tab-pane active',
  });

  var $tabButton = $('<li />', { class: 'nav-item' }).html(
    "<a href='#control-sidebar-theme-demo-options-tab' class='active' data-bs-toggle='tab' title='Setting'>" +
      '<i class="mdi mdi-settings"></i>' +
      '</a>'
  );

  $('[href="#control-sidebar-home-tab"]').parent().before($tabButton);

  var $demoSettings = $('<div />');

  $demoSettings.append(
    '<h4 class="control-sidebar-heading p-0">' +
      '</h4>' +
      '<div class="flexbox mb-10 pb-10 bb-1 light-on-off">' +
      '<label for="toggle_left_sidebar_skin" class="control-sidebar-subheading">' +
      'Dark or Light Skin' +
      '</label>' +
      '<label class="switch">' +
      '<input type="checkbox" data-mainsidebarskin="toggle" id="toggle_left_sidebar_skin">' +
      '<span class="switch-on fs-30"><i data-feather="moon"></i></span>' +
      '<span class="switch-off fs-30"><i data-feather="sun"></i></span>' +
      '</label>' +
      '</div>'
  );

  $demoSettings.append(
    '<h4 class="control-sidebar-heading p-0">' +
      '</h4>' +
      '<div class="flexbox mb-10 pb-10 bb-1">' +
      '<label for="rtl" class="control-sidebar-subheading">' +
      'Turn RTL/LTR' +
      '</label>' +
      '<label class="switch switch-border switch-danger">' +
      '<input type="checkbox" data-layout="rtl" id="rtl">' +
      '<span class="switch-indicator"></span>' +
      '<span class="switch-description"></span>' +
      '</label>' +
      '</div>'
  );

  $demoSettings.append(
    '<h4 class="control-sidebar-heading p-0">' +
      '</h4>' +
      '<div class="flexbox mb-10">' +
      '<label for="toggle_sidebar" class="control-sidebar-subheading">' +
      'Toggle Sidebar' +
      '</label>' +
      '<label class="switch switch-border switch-danger">' +
      '<input type="checkbox" data-layout="sidebar-collapse" id="toggle_sidebar">' +
      '<span class="switch-indicator"></span>' +
      '<span class="switch-description"></span>' +
      '</label>' +
      '</div>' +
      '<div class="flexbox mb-10">' +
      '<label for="toggle_right_sidebar" class="control-sidebar-subheading">' +
      'Toggle Right Sidebar Slide' +
      '</label>' +
      '<label class="switch switch-border switch-danger">' +
      '<input type="checkbox" data-controlsidebar="control-sidebar-open" id="toggle_right_sidebar">' +
      '<span class="switch-indicator"></span>' +
      '<span class="switch-description"></span>' +
      '</label>' +
      '</div>'
  );

  var $skinsList = $('<ul />', {
    class: 'list-unstyled clearfix theme-switch',
  });

  var $themePrimary = $('<li />', { style: 'padding: 5px;' }).append(
    '<a href="javascript:void(0)" data-theme="theme-primary" style="background: #46bc5c; display: block;vertical-align: middle;" class="clearfix rounded w-p100 h-30 mb-5" title="Theme primary">' +
      '</a>'
  );
  $skinsList.append($themePrimary);

  var $themeInfo = $('<li />', { style: 'padding: 5px;' }).append(
    '<a href="javascript:void(0)" data-theme="theme-info" style="background: #733aeb; display: block;vertical-align: middle;" class="clearfix rounded w-p100 h-30 mb-5" title="Theme info">' +
      '</a>'
  );
  $skinsList.append($themeInfo);

  var $themeSuccess = $('<li />', { style: 'padding: 5px;' }).append(
    '<a href="javascript:void(0)" data-theme="theme-success" style="background: #51ce8a; display: block;vertical-align: middle;" class="clearfix rounded w-p100 h-30 mb-5" title="Theme success">' +
      '</a>'
  );
  $skinsList.append($themeSuccess);

  var $themeDanger = $('<li />', { style: 'padding: 5px;' }).append(
    '<a href="javascript:void(0)" data-theme="theme-danger" style="background: #fb5a7f; display: block;vertical-align: middle;" class="clearfix rounded w-p100 h-30 mb-5" title="Theme danger">' +
      '</a>'
  );
  $skinsList.append($themeDanger);

  var $themeWarning = $('<li />', { style: 'padding: 5px;' }).append(
    '<a href="javascript:void(0)" data-theme="theme-warning" style="background: #fcc955; display: block;vertical-align: middle;" class="clearfix rounded w-p100 h-30 mb-5" title="Theme warning">' +
      '</a>'
  );
  $skinsList.append($themeWarning);

  var $themeSecondary = $('<li />', { style: 'padding: 5px;' }).append(
    '<a href="javascript:void(0)" data-theme="theme-secondary" style="background: #1ea1f2; display: block;vertical-align: middle;" class="clearfix rounded w-p100 h-30 mb-5" title="Theme secondary">' +
      '</a>'
  );
  $skinsList.append($themeSecondary);

  $demoSettings.append('<h4 class="control-sidebar-heading">Theme Colors</h4>');
  $demoSettings.append($skinsList);

  $tabPane.append($demoSettings);
  $('#control-sidebar-home-tab').after($tabPane);

  setup();

  // Add event listener for sidebar toggle
  $('#toggle_sidebar').on('click', function () {
    var isSidebarCollapsed = $('body').hasClass('sidebar-collapse');
    store('sidebar-collapse', isSidebarCollapsed ? '' : 'sidebar-collapse');
  });

  // Apply sidebar state from local storage on page load
  if (get('sidebar-collapse') === 'sidebar-collapse') {
    $('body').addClass('sidebar-collapse');
    $('#toggle_sidebar').attr('checked', true);
  }

  // Add event listener for RTL toggle
  $('#rtl').on('click', function () {
    var isRTL = $('body').hasClass('rtl');
    store('rtl', isRTL ? '' : 'rtl');
  });

  // Apply RTL state from local storage on page load
  if (get('rtl') === 'rtl') {
    $('body').addClass('rtl');
    $('#rtl').attr('checked', true);
  }
});
