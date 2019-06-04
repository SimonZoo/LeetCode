/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
  let str = "1",
    new_str = "";
  for (let i = 1; i < n; i++) {
    let t = str,
      cur_times = 1,
      new_str = "";
    let l = t.length;
    for (let j = 0; j < l; j++) {
      if (j + 1 < l && t[j] == t[j + 1]) {
        cur_times++;
      } else {
        new_str += cur_times + t[j];
        cur_times = 1;
      }
    }
    str = new_str;
  }
  return str;
};
