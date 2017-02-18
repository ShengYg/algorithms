public class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int n = nums.length;
        int[] next = new int[n];
        Stack<Integer> stack = new Stack<>();
        Arrays.fill(next, -1);

        for(int i = 0; i < 2*n; i++){
            int num = nums[i % n];
            while(!stack.isEmpty() && nums[stack.peek()] < num)
                next[stack.pop()] = num;
            if(i < n)
                stack.push(i);
        }
        return next;
    }
}
