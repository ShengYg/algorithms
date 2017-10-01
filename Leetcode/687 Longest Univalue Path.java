/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public int longestUnivaluePath(TreeNode root) {
        return Math.max(0, dfs(root)[0]-1);
    }

    public int[] dfs(TreeNode root) // global local
    {
        if(root == null)return new int[]{0, 0};
        int[] L = dfs(root.left);
        int[] R = dfs(root.right);
        int ans = Math.max(L[0], R[0]);
        int len = 1;
        int myans = 1;
        if(root.left != null && root.left.val == root.val){
            myans += L[1];
        }
        if(root.right != null && root.right.val == root.val){
            myans += R[1];
        }
        ans = Math.max(ans, myans);
        if(root.left != null && root.left.val == root.val){
            len = Math.max(len, L[1] + 1);
        }
        if(root.right != null && root.right.val == root.val){
            len = Math.max(len, R[1] + 1);
        }
        return new int[]{ans, len};
    }
}

