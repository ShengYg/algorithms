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

public class Solution {
    public boolean increasingTriplet(int[] nums) {
        int c1 = Integer.MAX_VALUE, c2 = Integer.MAX_VALUE;
        for (int x : nums)
            if (x <= c1)
                c1 = x;
            else if (x <= c2)
                c2 = x;
            else
                return true;
        return false;
    }
}
