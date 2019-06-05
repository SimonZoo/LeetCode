/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
  let ways = [0, 1, 2, 3];
  for (let i = 4; i <= n; i++) {
    ways[i] = ways[i - 1] + ways[i - 2];
  }
  return ways[n];
};
