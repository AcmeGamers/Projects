// Variables
const mobileMenu = document.querySelector(".mobile-menu"),
  iconMenu = document.querySelector(".icon-menu"),
  closeMenu = document.querySelector(".close-menu"),
  dropDown = document.querySelectorAll(".dropdown");

// -----------
// Mobile Menu
// -----------

// Shows mobile menu
iconMenu.addEventListener("click", () => {
  mobileMenu.style.display = "inherit";
});

// Hides mobile menu
closeMenu.addEventListener("click", () => {
  mobileMenu.style.display = "none";
});

// -------------
// Dropdown Menu
// -------------

for (let i = 0; i < dropDown.length; i++) {
  dropDown[i].addEventListener("click", () => {
    dropDown[i].classList.toggle("active");
    console.log("clicked, " + i);
  });
}
