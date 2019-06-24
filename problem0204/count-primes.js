/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
  let arr = new Array(n),
    count = 0;
  arr.fill(1);
  if (n >= 1) arr[0] = 0;
  if (n >= 2) arr[1] = 0;
  for (let i = 2; i < n; i++) {
    for (let j = 2; i * j < n; j++) {
      arr[i * j] = 0;
    }
  }
  for (let i = 0; i < n; i++) {
    if (arr[i]) {
      count++;
    }
  }
  return count;
};
