function findMinMax(arr) {
  let max = Math.max(...arr);
  let min = Math.min(...arr);

  return [max, min];
}

let number = [12, 45, 7, 89, 23];
let result = findMinMax(number);
console.log(result);
