/**
 * @param {number} num
 * @return {boolean}
 */
var isUgly = function(num) {
  if (num <= 0) return false;
  if (num == 1) return true;
  let t = num;
  while (true) {
    let flag = 0;
    if (t % 2 == 0) {
      t /= 2;
      flag = 1;
    } else if (t % 3 == 0) {
      t /= 3;
      flag = 1;
    } else if (t % 5 == 0) {
      t /= 5;
      flag = 1;
    }
    if (!flag) return false;
    if (flag && t == 1) return true;
  }
};
