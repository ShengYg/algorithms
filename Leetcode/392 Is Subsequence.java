public class Solution {
    public boolean isSubsequence(String s, String t) {
        if(s.length() == 0)
            return true;
        int indexT = 0, indexS = 0;
        while(indexT < t.length()){
            if(t.charAt(indexT) == s.charAt(indexS)){
                indexS++;
                if(indexS == s.length())
                    return true;
            }
            indexT++;
        }
        return false;
    }
}
