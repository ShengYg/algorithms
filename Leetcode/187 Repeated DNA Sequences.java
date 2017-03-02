public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        
        Set<Integer> word = new HashSet<>();
        Set<Integer> doubleword = new HashSet<>();
        List<String> rv = new ArrayList<>();
        char[] map = new char[26];
        map['C' - 'A'] = 1;
        map['G' - 'A'] = 2;
        map['T' - 'A'] = 3;

        for(int i = 0; i < s.length() - 9; i++) {
            int v = 0;
            for(int j = i; j < i + 10; j++) {
                v <<= 2;
                v |= map[s.charAt(j) - 'A'];
            }
            if(!word.add(v) && doubleword.add(v)) {
                rv.add(s.substring(i, i + 10));
            }
        }
        return rv;
    }
}
