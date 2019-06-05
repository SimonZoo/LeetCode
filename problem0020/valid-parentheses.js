/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  let arr = [],
    l = s.length;
  if (l == 0) return true;
  else if (l % 2 == 1) return false;
  else arr[0] = s[0];
  for (let i = 1; i < l; i++) {
    let t = arr[arr.length - 1];
    let cur = t + s[i];
    if (cur == "()" || cur == "{}" || cur == "[]") {
      arr.pop();
    } else {
      arr.push(s[i]);
    }
  }
  return arr.length == 0;
};
