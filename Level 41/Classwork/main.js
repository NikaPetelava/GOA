const friend1 = {
  firstname: "Dato",
  lastname: "Chilachava",
  age: 26,
  siblings: true,
  pet: false,
};

const friend2 = {
  firstname: "Mirian",
  lastname: "Neparidze",
  age: 29,
  siblings: true,
  pet: false,
};

const friend3 = {
  firstname: "Nino",
  lastname: "Gelashvili",
  age: 27,
  siblings: true,
  pet: false,
};

console.log(friend1);
console.log(friend1.firstname);
console.log(friend1.lastname);
friend1.firstname = "Gio";
console.log(friend1);

console.log(friend2);
console.log(friend2.firstname);
console.log(friend2.lastname);
delete friend2.pet;
console.log(friend2);

console.log(friend3);
console.log(friend3.firstname);
console.log(friend3.lastname);
friend3.eyes = "green";
console.log(friend3);

//

document.body.children[0].textContent = "Hello, There!";
document.body.children[0].style.color = "red";

document.body.children[1].textContent = "Hey";
document.body.children[1].style.color = "green";

const p = document.getElementById("p1");
p.textContent = "Goal Oriented Academy";
p.style.color = "tomato";

const btn = document.getElementById("btn");
btn.textContent = "Join Now";
btn.style.color = "green";
