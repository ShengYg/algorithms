public class Solution {
    public boolean isPossible(int[] nums) {
        HashMap<Integer, Integer>cnt = new HashMap<>();
        for(int item:nums){
            if(cnt.containsKey(item))
                cnt.put(item, cnt.get(item) + 1);
            else
                cnt.put(item, 1);
        }
        Integer[] nums_b = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(nums_b));
        for(int num: set){
            int a = cnt.getOrDefault(num - 2, 0);
            int b = cnt.getOrDefault(num - 1, 0);
            int c = cnt.getOrDefault(num, 0);
            int d = cnt.getOrDefault(num + 1, 0);
            int e = cnt.getOrDefault(num + 2, 0);
            int l = Math.min(a, b);
            int r = Math.min(d, e);
            a -= l;
            b -= l;
            d -= r;
            e -= r;
            c -= (l + r);
            if(c > 0 && c > Math.min(b, d))
                return false;
        }
        return true;
    }
}
