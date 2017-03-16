public class Solution {
    public int minPatches(int[] nums, int n) {
        long miss = 1;
        int i = 0, added = 0;
        while (miss <= n) {
            if (i < nums.length && miss >= nums[i])
                miss += nums[i++];
            else {
                miss += miss;
                added++;
            }
        }
        return added;
    }
}
