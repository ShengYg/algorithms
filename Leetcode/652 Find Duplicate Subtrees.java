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
    int id;
    HashMap<String, Integer> map;
    HashMap<Integer, Integer> cnt;
    ArrayList<TreeNode> dup;

    public char dfs(TreeNode x){
        if(x == null)
            return (char)('0');
        String tmp = new String(new char[]{dfs(x.left), dfs(x.right), (char)(x.val+ '0')});
        if(!map.containsKey(tmp))
            map.put(tmp, id++);
        int ret = map.get(tmp);
        if(cnt.getOrDefault(ret, 0) == 1)
            dup.add(x);
        cnt.put(ret, cnt.getOrDefault(ret, 0) + 1);
        return (char)(ret + '0');
    }

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        map = new HashMap<>();
        cnt = new HashMap<>();
        dup = new ArrayList<>();
        id = 1;
        dfs(root);
        return dup;
    }
}
