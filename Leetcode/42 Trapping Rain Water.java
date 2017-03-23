public class Solution {
    public int trap(int[] height) {
        int left = 0, right = height.length - 1, maxLeft = 0, maxRight = 0;
        int res = 0;
        while(left <= right) {
            if (height[left] <= height[right]) {
                if (height[left] <= maxLeft)
                    res += maxLeft - height[left];
                else
                    maxLeft = height[left];
                left++;
            }
            else {
                if (height[right] <= maxRight)
                    res += maxRight - height[right];
                else
                    maxRight = height[right];
                right--;
            }
        }
        return res;
    }
}
