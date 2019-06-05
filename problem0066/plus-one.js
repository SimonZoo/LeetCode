/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
  digits.reverse();
  digits[0] += 1;
  let l = digits.length;
  for (let i = 0; i < l; i++) {
    if (digits[i] == 10) {
      digits[i] = 0;
      if (i + 1 < l) digits[i + 1] += 1;
      else digits[i + 1] = 1;
    }
  }
  return digits.reverse();
};
