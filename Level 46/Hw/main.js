const name = prompt("გთხოვთ, შეიყანეთ თქვენი სახელი?");
const greeting = document.getElementById("greeting");
greeting.textContent = `გამარჯობა, ${name}!`;
greeting.style.textAlign = "right";

const resultElement = document.getElementById("result");
const numberInput = document.getElementById("numberInput");
let result = 0;

const addButton = document.getElementById("add");
const substractButton = document.getElementById("substract");
const multiplyButton = document.getElementById("multiply");

const clearButton = document.getElementById("clear");

addButton.addEventListener("click", () => {
  const number = parseInt(numberInput.value);
  result += number;
  resultElement.textContent = result;
});

substractButton.addEventListener("click", () => {
  const number = parseInt(numberInput.value);
  result -= number;
  resultElement.textContent = result;
});

multiplyButton.addEventListener("click", () => {
  const number = parseInt(numberInput.value);
  result *= number;
  resultElement.textContent = result;
});

clearButton.addEventListener("click", () => {
  result = 0;
  resultElement.textContent = result;
});
