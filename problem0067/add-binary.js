/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
  function str_reverse(s) {
    return s
      .split("")
      .reverse()
      .join("");
  }
  a = str_reverse(a);
  b = str_reverse(b);
  let c = [];
  if (a.length != b.length) {
    let short = a.length < b.length ? a : b;
    let long = a.length > b.length ? a : b;
    for (let i = short.length; i < long.length; i++) {
      short += " ";
    }
    a = short;
    b = long;
  }

  let flag = 0;
  for (let i = 0; i < a.length; i++) {
    c[i] = a[i] - 0 + (b[i] - 0);
    if (flag) {
      c[i] += 1;
      flag = 0;
    }
    if (c[i] >= 2) {
      c[i] -= 2;
      flag = 1;
    }
  }
  if (flag) {
    c[c.length] = 1;
  }
  return c.reverse().join("");
};
