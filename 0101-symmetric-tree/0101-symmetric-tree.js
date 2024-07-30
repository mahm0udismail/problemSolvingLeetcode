/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
let arr=[]
var isSymmetric = function(root) {
    let queue = [root.left, root.right];
    while(queue.length > 0) {
        let leftNode = queue.shift();
        let rightNode = queue.shift();
        if (leftNode == null && rightNode == null) continue;
        if (leftNode == null ||
            rightNode == null ||
            leftNode.val !== rightNode.val) {
            return false;
        }
        queue.push(leftNode.left,rightNode.right)
        queue.push(leftNode.right,rightNode.left)
    }
    return true
};