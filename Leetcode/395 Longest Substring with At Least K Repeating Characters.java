public class Solution {
    public int longestSubstring(String s, int k) {
        char[] str = s.toCharArray();
        return helper(str, 0, s.length(), k);
    }
    
    private int helper(char[] str, int start, int end,  int k){
        if(end - start < k)
            return 0;
        int[] count = new int[26];
        for(int i = start;i < end;i++)
            count[str[i]-'a']++;
        for(int i = start; i < end; i++)
            if(count[str[i] - 'a'] < k)
                return Math.max(helper(str, start, i, k), helper(str, i + 1, end, k));
        return end - start;
    }
}
