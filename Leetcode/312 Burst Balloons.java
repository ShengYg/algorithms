public class Solution {
    public int maxCoins(int[] nums) {
        int[] res = new int[nums.length + 2];
        int n = 1;
        for(int i: nums){
            if(i > 0)
                res[n++] = i;
        }
        res[0] = res[n++] = 1;
        
        int[][] memo = new int[n][n];
        return burst(memo, res, 0, n-1);
    }
    
    private int burst(int[][] memo, int[] nums, int left, int right){
        if(left + 1 == right)
            return 0;
        if(memo[left][right] > 0)
            return memo[left][right];
        int ans = 0;
        for(int i = left+1; i < right; ++i)
            ans = Math.max(ans, nums[left] * nums[i] * nums[right] + burst(memo, nums, left, i) + burst(memo, nums, i, right));
        memo[left][right] = ans;
        return ans;
    }
}
