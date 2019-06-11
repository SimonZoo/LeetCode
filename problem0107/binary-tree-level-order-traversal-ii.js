/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrderBottom = function(root) {
  if (!root) return [];
  let queue = [root],
    res = [];
  while (queue.length > 0) {
    let l = queue.length;
    let temp = [];
    for (let i = 0; i < l; i++) {
      let t = queue.shift();
      temp.push(t.val);
      if (t.left) queue.push(t.left);
      if (t.right) queue.push(t.right);
    }
    res.push(temp);
  }
  return res.reverse();
};
