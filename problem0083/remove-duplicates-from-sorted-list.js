/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
  if (!head) return head;
  let h = head,
    cur = head,
    next = head.next;
  if (next == null) return h;
  while (next) {
    if (cur.val == next.val) {
      next = next.next;
      cur.next = next;
    } else {
      cur = next;
      next = next.next;
    }
  }
  return h;
};
