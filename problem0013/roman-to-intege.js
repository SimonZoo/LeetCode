/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
  let l = s.length;
  let num = 0;
  for (let i = 0; i < l; i++) {
    if (s[i] == "M") num += 1000;
    else if (s[i] == "D") num += 500;
    else if (s[i] == "C") {
      if (i + 1 < l && s[i + 1] == "D") {
        num += 400;
        i += 1;
      } else if (i + 1 < l && s[i + 1] == "M") {
        num += 900;
        i += 1;
      } else num += 100;
    } else if (s[i] == "L") num += 50;
    else if (s[i] == "X") {
      if (i + 1 < l && s[i + 1] == "L") {
        num += 40;
        i += 1;
      } else if (i + 1 < l && s[i + 1] == "C") {
        num += 90;
        i += 1;
      } else num += 10;
    } else if (s[i] == "V") num += 5;
    else if (s[i] == "I") {
      if (i + 1 < l && s[i + 1] == "V") {
        num += 4;
        i += 1;
      } else if (i + 1 < l && s[i + 1] == "X") {
        num += 9;
        i += 1;
      } else num += 1;
    }
  }
  return num;
};
