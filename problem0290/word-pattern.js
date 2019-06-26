/**
 * @param {string} pattern
 * @param {string} str
 * @return {boolean}
 */
var wordPattern = function(pattern, str) {
  let arr = str.split(" "),
    obj = {},
    s = "",
    p = [],
    j = 0;
  for (let i = 0; i < pattern.length; i++) {
    if (p.indexOf(pattern[i]) == -1) p.push(pattern[i]);
  }
  for (let i = 0; i < arr.length; i++) {
    if (!(arr[i] in obj)) {
      obj[arr[i]] = p[j++];
    }
    s += obj[arr[i]];
  }
  return s == pattern;
};
