/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
  let stack = [],
    depth = 0;
  if (root != null) {
    stack.push([depth + 1, root]);
  }
  while (stack.length > 0) {
    let a = stack.pop();
    let cur_dep = a[0],
      cur_root = a[1];
    if (cur_root != null) {
      depth = depth > cur_dep ? depth : cur_dep;
      stack.push([cur_dep + 1, cur_root.left]);
      stack.push([cur_dep + 1, cur_root.right]);
    }
  }
  return depth;
};
