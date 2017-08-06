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
    public boolean findTarget(TreeNode root, int k) {
        List<Integer> res = inorderTraversal(root);
        for(int i = 0, j = res.size() - 1; i < j;){
            if(res.get(i) + res.get(j) < k)
                i++;
            else if(res.get(i) + res.get(j) > k)
                j--;
            else
                return true;
        }
        return false;
    }

    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> nodes = new ArrayList<Integer>();
        LinkedList<TreeNode> toVisit = new LinkedList<TreeNode>();
        TreeNode curNode = root;

        while(curNode!=null){
            if(curNode.left != null){
                TreeNode predecessor = curNode.left;
                while(predecessor.right != null && predecessor.right != curNode)
                    predecessor = predecessor.right;
                if(predecessor.right == null){
                    predecessor.right = curNode;
                    curNode = curNode.left;
                } else{
                    predecessor.right = null;
                    nodes.add(curNode.val);
                    curNode = curNode.right;
                }
            } else{
                nodes.add(curNode.val);
                curNode = curNode.right;
            }
        }
        return nodes;
    }
}
