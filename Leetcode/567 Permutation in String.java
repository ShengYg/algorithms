public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int len1 = s1.length(), len2 = s2.length();
        if (len1 > len2)
            return false;
        
        int[] cnt = new int[26];
        for (int i = 0; i < len1; i++) {
            cnt[s1.charAt(i) - 'a']++;
            cnt[s2.charAt(i) - 'a']--;
        }
        if (allZero(cnt)) 
            return true;
        
        for (int i = len1; i < len2; i++) {
            cnt[s2.charAt(i) - 'a']--;
            cnt[s2.charAt(i - len1) - 'a']++;
            if (allZero(cnt)) return true;
        }
        
        return false;
    }
    private boolean allZero(int[] cnt) {
        for (int i = 0; i < 26; i++)
            if (cnt[i] != 0) 
                return false;
        return true;
    }
}
