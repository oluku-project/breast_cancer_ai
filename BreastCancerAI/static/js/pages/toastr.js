function showToast(heading, text, icon) {
  $.toast({
    heading: heading,
    text: text,
    position: 'top-right',
    loaderBg: '#ff6849',
    icon: icon,
    hideAfter: 3500,
    stack: 6,
  });
}

