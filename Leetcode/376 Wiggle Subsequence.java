public class Solution {
    public int wiggleMaxLength(int[] nums) {
        boolean large = true;
        if(nums.length == 0 || nums.length == 1)
            return nums.length;
        int k = 0;
        while (k < nums.length - 1 && nums[k] == nums[k + 1]) {
            k++;
        }
        if (k == nums.length - 1) {
            return 1;
        }
        int result = 2;
        boolean small = nums[k] < nums[k + 1];
        for (int i = k + 1; i < nums.length - 1; i++) {
            if (small && nums[i + 1] < nums[i]) {
                nums[result] = nums[i + 1];
                result++;
                small = !small;
            } else {
                if (!small && nums[i + 1] > nums[i]) {
                    nums[result] = nums[i + 1];
                    result++;
                    small = !small;
                }
            }
        }
        return result;
    }
}
