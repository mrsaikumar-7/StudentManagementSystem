hamburger = document.querySelector(".hamburger")
hamburger.onclick = function(){
    navBar =document.querySelector(".nav-bar");
    navBar.classList.toggle("active")
    // alert('the menu bar is active')
} 


// Get the current URL
const currentUrl = window.location.href;

// Get all the menu items
const menuItems = document.querySelectorAll('.nav-item');
// console.log('menu items' + menuItems)
// Loop through each menu item
menuItems.forEach((item) => {
  // Get the href attribute of the item
  const href = item.getAttribute('href');
  console.log(href)
  console.log('current url: '+currentUrl)
  // If the href matches the current URL, add the active class
  if (href === currentUrl) {
    item.classList.add('active');
  }
});



