// Task #1
document.getElementById("firstelement").textContent = "Hello World!";

// Task #2
document.getElementById("secondelement").style.color = "tomato";

// Task #3
let thirdelement = document.getElementById("thirdelement");
thirdelement.style.color = "red";
thirdelement.style.background = "black";

// Task #4
let fourthelement = document.getElementById("fourthelement");
fourthelement.textContent = "We love JavaScript";
fourthelement.style.fontSize = "30px";
fourthelement.style.textAlign = "center";

// Task #5
let newElement = document.createElement("p");
let newElement2 = document.createElement("p");

newElement.textContent = "Lorem ipsum dolor sit amet.";
newElement2.textContent = "Lorem ipsum dolor sit amet.";

newElement.style.background = "blue";
newElement2.style.background = "green";

let elementContainer = document.getElementById("fifthelement");

elementContainer.appendChild(newElement);
elementContainer.appendChild(newElement2);
