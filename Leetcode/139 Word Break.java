public class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        if (wordDict.size() == 0)
            return false;

        int sl = s.length();
        List<Boolean> dp = new ArrayList<>();

        for (int i = 0; i < s.length() + 1; i++)
            dp.add(false);
        dp.set(0, true);

        for (int i = 1; i <= s.length(); i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (dp.get(j) == true) {
                    String word = s.substring(j, i);
                    if (wordDict.contains(word)) {
                        dp.set(i, true);
                        break;
                    }
                }
            }
        }
        return dp.get(s.length());
    }
}
