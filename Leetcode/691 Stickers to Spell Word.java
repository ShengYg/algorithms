class Solution {
    public int minStickers(String[] stickers, String target) {
        HashMap<String, Integer> dp = new HashMap<>();
        int[][] mp = new int[stickers.length][26];
        for(int i = 0; i < stickers.length; i++){
            for(char c: stickers[i].toCharArray())
                mp[i][c-'a']++;
        }
        dp.put("", 0);
        return helper(dp, mp, target);
    }
    public int helper(HashMap<String, Integer>dp, int[][] mp, String target){
        if(dp.containsKey(target))
            return dp.get(target);
        int ans = Integer.MAX_VALUE;
        int[] tar = new int[26];
        for (char c:target.toCharArray())
            tar[c-'a']++;
        for(int i = 0; i < mp.length; i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < 26; j++){
                if(tar[j] > 0)
                    for (int k = 0; k < Math.max(0, tar[j]-mp[i][j]); k++)
                        sb.append((char)('a'+j));
            }
            String s = sb.toString();
            if(s.length() != target.length()){
                int tmp = helper(dp, mp, s);
                if(tmp != -1){
                    ans = Math.min(ans, 1 + tmp);
                }
            }
        }
        dp.put(target, ans == Integer.MAX_VALUE ? -1: ans);
        return dp.get(target);
    }
}
