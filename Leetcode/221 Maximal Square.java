public class Solution {
    public int maximalSquare(char[][] matrix) {
        int m = matrix.length;
        if(m == 0)
            return 0;
        int n = matrix[0].length;
        int[] pre = new int[m], cur = new int[m];
        int maxsize = 0;
        for (int i = 0; i < m; i++) {
            pre[i] = matrix[i][0] - '0';
            maxsize = Math.max(maxsize, pre[i]);
        }
        for (int j = 1; j < n; j++) {
            cur[0] = matrix[0][j] - '0';
            maxsize = Math.max(maxsize, cur[0]);
            for (int i = 1; i < m; i++) {
                if (matrix[i][j] == '1') {
                    cur[i] = Math.min(cur[i - 1], Math.min(pre[i - 1], pre[i])) + 1;
                    maxsize = Math.max(maxsize, cur[i]);
                }
            }
            for (int i = 0; i < m; i++) {
                pre[i] = cur[i];
            }
            Arrays.fill(cur, 0);
        }
        return maxsize * maxsize;
    }
}
