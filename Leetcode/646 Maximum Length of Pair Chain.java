public class Solution {
    public int findLongestChain(int[][] pairs) {
        Arrays.sort(pairs, (a, b) -> a[1] - b[1]);
        int res = 0;
        double end = -Double.MAX_VALUE;
        for(int[] item : pairs) {
            if (item[0] > end) {
                end = item[1];
                res += 1;
            }
        }
        return res;
    }
}
