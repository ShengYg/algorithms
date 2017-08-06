public class Solution {
    public List<Integer> cheapestJump(int[] A, int B) {
        int n = A.length;
        int[] dp = new int[n];
        int[] path = new int[n];
        dp[n - 1] = 0;

        for(int i = n - 2; i >= 0; i--) {
            dp[i] = Integer.MAX_VALUE;
            if(A[i] == -1) {
                path[i] = -1;
                continue;
            }
            for(int j = 1; j <= B && i + j < n; j++){
                if(A[i + j] < 0)
                    continue;
                if(dp[i + j] + A[i] < dp[i]){
                    dp[i] = dp[i + j] + A[i];
                    path[i] = i + j;
                }
            }
        }

        ArrayList<Integer> res = new ArrayList<>();
        if(Math.abs(dp[0]) > 1e9)
            return res;
        int i = 0;
        while(true){
            res.add(i + 1);
            if(i == n - 1)
                break;
            i = path[i];

        }
        return res;
    }
}
