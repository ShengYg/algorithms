/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        int max_index = maxindex(nums);
        TreeNode root = new TreeNode(nums[max_index]);
        if(max_index > 0) {
            int[] part1 = new int[max_index];
            System.arraycopy(nums, 0           , part1, 0     , part1.length);
            root.left = subtree(part1, 0, part1.length);
        }
        if(max_index < nums.length - 1){
            int[] part2 = new int[nums.length - max_index - 1];
            System.arraycopy(nums, max_index + 1, part2, 0     , part2.length);
            root.right = subtree(part2, 0, part2.length);
        }
        return root;
    }

    public TreeNode subtree(int[] nums, int s, int e){
        int max_index = maxindex(nums);
        TreeNode root = new TreeNode(nums[max_index]);
        if(max_index > 0) {
            int[] part1 = new int[max_index];
            System.arraycopy(nums, 0, part1, 0     , part1.length);
            root.left = subtree(part1, 0, part1.length);
        }
        if(max_index < nums.length - 1){
            int[] part2 = new int[nums.length - max_index - 1];
            System.arraycopy(nums, max_index + 1, part2, 0     , part2.length);
            root.right = subtree(part2, 0, part2.length);
        }
        return root;
    }

    public int maxindex(int[] nums){
        int max_val = Integer.MIN_VALUE;
        int max_index = 0;
        for(int i = 0; i < nums.length; i++)
            if(nums[i] > max_val){
                max_val = nums[i];
                max_index = i;
            }
        return max_index;
    }
}
