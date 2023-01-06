const greetingClose = document.querySelector(".greeting-close");
const checkBox = document.querySelector("#checkbox");
const label = document.querySelector(".greeting label");
const dim = document.querySelector("#overlay");
const greeting = document.querySelector(".greeting");
const checked = localStorage.getItem("checkbox");
const info = document.querySelector(".header i");

if (checked == null) {
  dim.classList.add("active");
  greeting.classList.add("active");
}
function onCloseGreeting(event) {
  event.preventDefault();
  dim.classList.remove("active");
  greeting.classList.remove("active");
  if (checkBox.checked) {
    localStorage.setItem("checkbox", "checked");
  }
}
greetingClose.addEventListener("click", onCloseGreeting);
function showInfo() {
  dim.classList.add("active");
  greeting.classList.add("active");
  checkBox.style.display = "none";
  label.style.display = "none";
}
info.addEventListener("click", showInfo);
