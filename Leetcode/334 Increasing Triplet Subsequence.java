public class Solution {
    public boolean increasingTriplet(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;

        for(int x : nums) {
            int i = Arrays.binarySearch(dp, 0, len, x);
            if(i < 0) i = -(i + 1);
            dp[i] = x;
            if(i == len) len++;
            if(len >= 3)
                return true;
        }

        return false;
    }
}
