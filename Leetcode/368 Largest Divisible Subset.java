public class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        Arrays.sort(nums);
        int[] res = new int[nums.length];
        int[] parent = new int [nums.length];
        int m = 0, mi = 0;

        for(int i = 0; i < nums.length; i++){
            for(int j = i; j >= 0; j--){
                if(nums[i] % nums[j] == 0 && res[j] + 1 > res[i]) {
                    res[i] = 1 + res[j];
                    parent[i] = j;
                    if(res[i] > m){
                        m = res[i];
                        mi = i;
                    }
                }
            }
        }
        List<Integer> ret = new ArrayList<>();
        for(int i = 0; i < m; i++){
            ret.add(0, nums[mi]);
            mi = parent[mi];
        }
        return ret;
    }
}
