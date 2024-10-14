// Easy assignment

document.getElementById("text").style.background = "green";

document.getElementById("styledText").style.fontWeight = "bold";
document.getElementById("styledText").style.fontStyle = "italic";

document.getElementById("resizable").style.width = "100px";

document.getElementById("myDiv").style.backgroundImage = "url('2.jpg')";

document.getElementById("textAppender").innerText = "JavaScript";

const btn = document.getElementById("increaseNumber");
let number = 0;

btn.onclick = function () {
  number++;
  btn.textContent = number;
};

const btn2 = document.getElementById("moveBtn");
let movable = document.getElementById("movable");

btn2.onclick = function () {
  movable.align = "right";
};

document.getElementById("contentContainer").innerHTML = "GOA";

document.getElementById("hiddenElement").style.display = "block";
