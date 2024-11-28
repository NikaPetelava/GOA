//* output
let textOutput = document.getElementById("output");

//* buttons
let addText = document.getElementById("addtext");
let changeColor = document.getElementById("changecolor");
let changeSize = document.getElementById("changesize");

//? დავამატოთ ტექსტის ვებგვერდზე
addText.addEventListener("click", () => {
  let textInput = document.getElementById("textinput").value;
  textOutput.textContent = textInput;
});

//? შევუცვალოთ ტექსტს ფერი
changeColor.addEventListener("click", () => {
  let colorInput = document.getElementById("colorinput").value;
  textOutput.style.color = colorInput;
});

//? შევუცვალოთ ტექსტს ზომა
changeSize.addEventListener("click", () => {
  let sizeInput = document.getElementById("sizeinput").value;
  textOutput.style.fontSize = sizeInput + "px";
});

const themeToggleBtn = document.querySelector(".theme-toggle");

themeToggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});
