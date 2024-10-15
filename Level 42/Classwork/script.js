// Task #1
const increase = document.getElementById("increaseNumber");
const decrease = document.getElementById("decreaseNumber");
const p = document.getElementById("count");

let number = 0;

increase.addEventListener("click", function () {
  number++;
  p.textContent = number;
});

decrease.addEventListener("click", function () {
  number--;
  p.textContent = number;
});

// Task #2
const text = document.getElementById("text");
const output = document.getElementById("textOutput");

output.addEventListener("click", function () {
  text.textContent = "Hello, World!";
});

// Task #3
const input = document.getElementById("firstname");

input.addEventListener("input", function () {
  console.log(input.value);
});

// Task #4
const image = document.getElementById("resizingimage");

image.addEventListener("mouseover", function () {
  image.style.width = "400px";
});

image.addEventListener("mouseout", function () {
  image.style.width = "300px";
});

// ---------------------------------------------------------

// Task #1
function sum(firstNumber, secondNumber) {
  return firstNumber + secondNumber;
}

sum(5, 5);

// Task #2
function greet(userName) {
  return `Hello, ${userName}`;
}

greet("Nika");

// Task #3
function randomNumber() {
  return Math.random();
}

randomNumber();

// Task #4
function multiply(a, b, c) {
  return a * b * c;
}

multiply(2, 2, 10);

// Task #5
function greetWithDefault(name = "Stranger") {
  return `Hello, ${name}`;
}

greetWithDefault("Nika");
greetWithDefault();

// Task #6
function square(number) {
  return number * number;
}
let result = square(5);
console.log(result);

// Task #7
function capitalize(string) {
  // let string = "Hello";
  // console.log(string[0].toUpperCase() + string.slice(1));
  return string[0].toUpperCase() + string.slice(1);
}

console.log(capitalize("hello"));

// Task #8
function sumArray(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

console.log(sumArray([1, 2, 3, 4, 5]));

// Task #9

function add(a, b) {
  return a + b;
}

function doubleAdd(c, d) {
  return add(add(c, c), add(d, d));
}

console.log(add(5, 10));
console.log(doubleAdd(5, 10));

// #10

function isEven(a) {
  if (a % 2 == 0) {
    return true;
  } else {
    return false;
  }
}

console.log(isEven(2));
