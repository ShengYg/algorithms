public class Solution {
    public int[] findErrorNums(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        int sum = 0;
        int[] res = new int[2];
        for(int item: nums){
            if(set.contains(item))
                res[0] = item;
            else{
                set.add(item);
                sum += item;
            } 
        }
        
        int n = nums.length;
        res[1] = n * (n + 1) / 2 - sum;
        return res;
    }
}

public class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        boolean[] used = new boolean[n+1];

        int sum = 0;
        int[] res = new int[2];
        for(int item: nums){
            if(used[item])
                res[0] = item;
            else{
                used[item] = true;
                sum += item;
            }
        }

        res[1] = n * (n + 1) / 2 - sum;
        return res;
    }
}
