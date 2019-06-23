/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
  let s = n.toString(2);
  let count = 0,
    l = s.length;
  for (let i = 0; i < l; i++) {
    if (s[i] == "1") {
      count++;
    }
  }
  return count;
};
