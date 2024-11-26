// let num1 = parseInt(prompt("შეიყვანეთ პირველი რიცხვი:"));
// let num2 = parseInt(prompt("შეიყვანეთ მეორე რიცხვი: "));

// let operation = prompt("აირჩიეთ ოპერაცია ('+' - მიმატება, '-' - გამოკლება): ");

// if (operation === "+") {
//   result = num1 + num2;
//   prompt(`შედეგი ${num1} + ${num2} = ${result}`);
// } else if (operation === "-") {
//   result = num1 - num2;
//   prompt(`შედეგი  ${num1} - ${num2} = ${result}`);
// } else {
//   promt("არასწორი ოპერაცია! შეიყვანეთ '+' ან '-'.");
// }

function calculate(operation) {
  let num1 = parseInt(document.getElementById("num1").value);
  let num2 = parseInt(document.getElementById("num2").value);

  let result;
  if (operation === "+") {
    result = num1 + num2;
  } else if (operation === "-") {
    result = num1 - num2;
  } else {
    result = "არასწორი ოპერაცია!";
  }

  document.getElementById("result").textContent = `შედეგი: ${result}`;
}
