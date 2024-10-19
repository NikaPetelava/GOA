// Task #1
function sayHello() {
  console.log("გამარჯობა");
}

sayHello();

// Task #2
function greet(name) {
  console.log(`გამარჯობა, ${name}`);
}

greet("ნიკა");

// Task #3
function increment(number) {
  return number + 1;
}

let result = increment(55);
console.log(result);

// Task #4
function makeNegative(number) {
  return number * -1;
}

let result2 = makeNegative(44) + 1;
console.log(result2);

// Task #5
function idModify(id) {
  let element = document.getElementById(id);

  element.style.color = "red";
  element.style.background = "green";
  element.textContent = "JavaScript";
}

idModify("paragraph");
