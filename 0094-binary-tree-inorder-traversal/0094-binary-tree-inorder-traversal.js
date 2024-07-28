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
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    const result = []
    nextAndStor(root,result)
    return result;
};

function nextAndStor(root,result){
    if(root !== null){
        nextAndStor(root.left,result)
        result.push(root.val)
        nextAndStor(root.right,result)
    }
}