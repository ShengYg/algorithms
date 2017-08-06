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
    int height;

    public List<List<String>> printTree(TreeNode root) {
        height = get_height(root);
        String[][] res = new String[height][(1 << height) - 1];
        for(int i = 0; i < height; i++)
            for(int j = 0; j < (1 << height) - 1; j++)
                res[i][j] = "";
        addnum(root, height - 1, 1, res);
        List<List<String>> ret = new ArrayList<>();
        for(String[] item: res)
            ret.add(Arrays.asList(item));
        return ret;
    }

    public int get_height(TreeNode root){
        if(root == null)
            return 0;
        return Math.max(get_height(root.left), get_height(root.right)) + 1;
    }

    public void addnum(TreeNode root, int h, int w, String[][] res){
        res[height - h - 1][w * (1 << h) - 1] = Integer.toString(root.val);
        if(root.left != null)
            addnum(root.left, h - 1, 2 * w - 1, res);
        if(root.right != null)
            addnum(root.right, h - 1, 2 * w + 1, res);
    }
}
