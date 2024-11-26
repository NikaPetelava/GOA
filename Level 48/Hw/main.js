//* Task 1

function printPositions(row, col) {
  //? რიგების ციკლი
  for (let i = 1; i <= row; i++) {
    //? სვეტების ციკლი
    for (let j = 1; j <= col; j++) {
      console.log(`row: ${i}  col: ${j}`);
    }
  }
}

printPositions(2, 2);

// * Task 2

function MultiplicationTable() {
  let table = []; //? ცარიელი მასივი 2D მასივისთვის

  for (let i = 1; i <= 10; i++) {
    let row = []; //? თითოელი რიგის შესაქმნელად
    for (let j = 1; j <= 10; j++) {
      row.push(i * j); //? i_ს გამრავლება j_ზე და შედეგის row მასივში დამატება
    }
    table.push(row); //? რიგის დამატება მთავარ მასივში
  }

  return table;
}

console.log(MultiplicationTable());

//*

function printPairs(number) {
  for (let i = 1; i <= number; i++) {
    for (let j = 1; j <= number; j++) {
      //? // ვამოწმებთ, მეორე რიცხვი მეტია თუ არა პირველზე
      if (j > i) {
        console.log(`(${i},${j})`);
      }
    }
  }
}

printPairs(3);
