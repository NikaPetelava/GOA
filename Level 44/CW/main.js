function greet(id) {
  document.getElementById(id).textContent = "გამარჯობა!";
}

greet("p1");

function sum(a, b, c) {
  return a * b * c;
}

console.log(sum(2, 3, 4));
