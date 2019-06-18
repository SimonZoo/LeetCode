/**
 * @param {number} n
 * @return {string}
 */
var convertToTitle = function(n) {
  let arr = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z"
  ];
  let s = [];

  while (n) {
    n--;
    s.push(arr[n % 26]);
    n = Math.floor(n / 26);
  }
  return s.reverse().join("");
};
