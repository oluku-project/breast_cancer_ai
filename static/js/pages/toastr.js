function showToast(heading, text, icon) {
  console.log('Hi dey');
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

console.log('Hi welcome');
