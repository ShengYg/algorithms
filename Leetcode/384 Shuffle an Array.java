import java.util.Random;

public class Solution {
    private int[] nums;
    private Random random;
    public Solution(int[] nums) {
        this.nums = nums;
        random = new Random();
    }

    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return this.nums;
    }

    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        if(nums == null)
            return null;
        int[] a = nums.clone();
        for(int j = 1; j < a.length; j++){
            int i = random.nextInt(j + 1);
            swap(i, j, a);
        }
        return a;
    }

    public void swap(int i, int j, int[] a){
        int k = a[i];
        a[i] = a[j];
        a[j] = k;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
