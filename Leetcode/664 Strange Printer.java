class Solution {
    public int strangePrinter(String s) {
        int n = s.length();
        if (n == 0) 
            return 0;
        
        int[][] dp = new int[101][101];
        for (int i = 0; i < n; i++) 
            dp[i][i] = 1;
        
        for (int i = 1; i < n; i++)
            for (int j = 0; j < n - i; j++){
                dp[j][j + i] = dp[j][j + i - 1] + 1;
                for (int k = j + 1; k <= j + i; k++)
                    if (s.charAt(k - 1) == s.charAt(j + i))
                        dp[j][j + i] = Math.min(dp[j][j + i], dp[j][k - 1] + dp[k][j + i] - 1);
            }
        return dp[0][n - 1];
    }
}
