public class Solution {
    public int maxA(int N) {
        int[] res = new int[N + 1];
        for(int i = 1; i <= N; i++){
            res[i] = i;
            for(int j = 3; j <= i; j++){
                res[i] = Math.max(res[i], res[i - j] * (j - 1));
            }
        }
        return res[N];
    }
}

public class Solution {
    public int maxA(int N) {
        if (N <= 6)  
            return N;
        int[] dp = new int[N + 1];
        for (int i = 1; i <= 6; i++)
            dp[i] = i;
        for (int i = 7; i <= N; i++)
            dp[i] = Math.max(dp[i - 4] * 3, dp[i - 5] * 4);
        return dp[N];
    }
}
