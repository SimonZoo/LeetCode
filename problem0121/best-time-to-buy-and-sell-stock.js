/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
  let profit = 0,
    minPrice = prices[0];
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i];
    } else {
      profit = profit > prices[i] - minPrice ? profit : prices[i] - minPrice;
    }
  }
  return profit;
};
