function myFunction() {
    var element = document.getElementById('mydark');
    element.classList.toggle("dark-mode");
    var darkButton = document.getElementById('dark-button')
    if (darkButton.innerHTML === "Dark Mode") {
      darkButton.innerHTML = "Light Mode";
    } else {
      darkButton.innerHTML = "Dark Mode";
    }
  }