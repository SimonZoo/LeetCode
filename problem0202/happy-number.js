/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
  let obj = { n: 1 },
    t = 0;
  while (n != 1) {
    while (n) {
      t += Math.pow(n % 10, 2);
      n = Math.floor(n / 10);
    }
    n = t;
    t = 0;
    if (n in obj) return false;
    else obj[n] = 1;
  }
  return true;
};
