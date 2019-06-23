/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
  let c = 0;
  while (n >= 5) {
    c += Math.floor(n / 5);
    n = Math.floor(n / 5);
  }
  return c;
};
