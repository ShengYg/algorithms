public class Solution {
    public int maxProduct(String[] words) {
        int[] value = new int[words.length];
        for(int i = 0; i < words.length; i++){
            for(int j = 0; j < words[i].length(); j++)
                value[i] |= 1 << (words[i].charAt(j) - 'a');
        }

        int maxLength = 0;
        for(int i = 0; i < words.length; i++){
            for(int j = i; j < words.length; j++)
                if((value[i] & value[j]) == 0 && (words[i].length() * words[j].length() > maxLength))
                    maxLength = words[i].length() * words[j].length();
        }
        return maxLength;
    }
}
