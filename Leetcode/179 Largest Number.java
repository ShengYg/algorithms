public class Solution {
    public String largestNumber(int[] nums) {
        if(nums == null || nums.length == 0)
            return "";
        String[] s_sum = new String[nums.length];
        for(int i = 0; i < nums.length; i++)
            s_sum[i] = String.valueOf(nums[i]);
        
        Comparator<String> comp = new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                String str1 = s1 + s2;
                String str2 = s2 + s1;
                return str2.compareTo(str1);
            }
        };
        
        Arrays.sort(s_sum, comp);
        if(s_sum[0].charAt(0) == '0')
            return new String("0");

        StringBuilder sb = new StringBuilder();
        for(String s: s_sum)
            sb.append(s);
        
        return sb.toString();
    }
}
