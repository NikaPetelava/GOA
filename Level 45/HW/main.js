// Task #1
function convertMinutesToSeconds(minutes) {
  return minutes * 60;
}

let seconds = convertMinutesToSeconds(5);
console.log(seconds);

// Task #2
function calculateSumAndMultiply(num1, num2, num3) {
  let sum = num1 + num2;
  return sum * num3;
}

let result = calculateSumAndMultiply(2, 3, 4);
console.log(result);

// Task #3
function isFirstGreaterThanSecond(num1, num2) {
  return num1 > num2;
}

let result1 = isFirstGreaterThanSecond(5, 3);
let result2 = isFirstGreaterThanSecond(2, 4);

console.log(result1);
console.log(result2);

// Task #4
function logElement(id) {
  let element = document.getElementById(id);
  console.log("Element : " + element.textContent);
}

logElement("myElement");

// Task #5
function updateElementContent(id, string) {
  let element = document.getElementById(id);
  element.textContent = string;
}

updateElementContent("myElement2", "ეს არის ახალი შინაარსი.");
