import java.util.stream.*;

public class Solution {
    public int candy(int[] ratings) {
        int length = ratings.length;
        if(length <= 1){
            return length;
        }

        int[] nums = new int[length];
        for(int i = 0; i < length; i++){
            nums[i] = 1;
        }
        for(int i = 1; i < length; i++){
            if(ratings[i] > ratings[i-1])
                nums[i] = nums[i-1] + 1;
        }
        for(int i = length - 1; i > 0; i--){
            if(ratings[i] < ratings[i-1])
                nums[i-1] = Math.max(nums[i-1],nums[i] + 1);
        }

        // int sum = IntStream.of(nums).sum();
        int sum = 0;
        for(int i = 0; i < length; i++){
            sum += nums[i];
        }
        return sum;
    }
}
