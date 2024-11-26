// 2
function isGreaterThan(a, b) {
  return a > b;
}

console.log(comparison(10, 5));

// 3
function isBetween(a, b, c) {
  return b > a && b < c;
}

console.log(comparison(1, 3, 5));

// 4
function checkStrings(a, b) {
  if (a[0] === b[0] && a[1] === b[1]) {
    return true;
  }
  return false;
}

console.log(checkStrings("hello", "he"));

// 5
function checkValue(a) {
  if (typeof a === "string") {
    return a.length; // სტრინგის სიგრძის დაბრუნება
  } else if (typeof a === "number") {
    return a > 100; // 100_ზე მეტია თუ არა
  } else if (typeof a === "boolean") {
    return !a; // ბულეანის საპირისპიროს დაბრუნება
  } else {
    return "Unsupported type";
  }
}

console.log(checkValue("nika"));
console.log(checkValue(110));
console.log(checkValue(true));
console.log(checkValue([1, 2, 3]));
