//! ...args აგროვებს ყველა გადაცემულ არგუმენტს ერთ მასივში
function countArea(...args) {
  //* ამოწმებს მასივში მყოფი არგუმენტების რაოდენობა შეესაბამება თუ არა მითითებულ რიცხვს.
  if (args.length === 2) {
    //* მართკუთხედი (სიგრძე და სიგანე)
    const [lenght, width] = args;
    return lenght * width;
  } else if (args.length === 1) {
    //* წრე (რადიუსი)
    const [radius] = args;
    //! Math.Pi არის მუდმივი მნიშვნელობა, რომელიც შეესაბამება π-ს(3.14159)
    //! Math.pow(რიცხვი, ხარისხი) გამოიყენება რიცხვს კონკრეტულ ხარისხში აყვანისთვის
    return Math.PI * Math.pow(radius, 2);
  } else if (args.length === 3) {
    //* სამკუთხედი(სამი გვერდი, ჰერონის ფორმულა)
    const [a, b, c] = args;
    const s = (a + b + c) / 2;
    //!Math.sqrt გამოთვლის რიცხვის კვადრატულ ფესვს
    return Math.sqrt(s * (s - a) * (s - b) * (s - c));
  } else {
    return "Invalid input";
  }
}

console.log(countArea(5, 10));
console.log(countArea(9));
console.log(countArea(3, 4, 5));
console.log(countArea());
