class TrieNode {
    public char val;
    public boolean isWord;
    public TrieNode[] children = new TrieNode[26];
    public TrieNode() {}
    public TrieNode(char c){
        val = c;
    }
}

class Trie {
    private TrieNode root;
    public Trie() {
        root = new TrieNode();
        root.val = ' ';
    }

    public void insert(String word) {
        TrieNode current = root;
        for(int i = 0; i < word.length(); i++){
            char c = word.charAt(i);
            if(current.children[c - 'a'] == null){
                current.children[c - 'a'] = new TrieNode(c);
            }
            current = current.children[c - 'a'];
        }
        current.isWord = true;
    }

    public String getprefix(String s){
        StringBuilder res = new StringBuilder();
        TrieNode current = root;
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(current.children[c - 'a'] == null || res.toString() == null)
                break;
            current = current.children[c - 'a'];
            res.append(current.val);
            if(current.isWord)
                return res.toString();
        }
        return s;
    }
}

public class Solution {
    public String replaceWords(List<String> dict, String sentence) {
        Trie tree = new Trie();
        for(String word: dict)
            tree.insert(word);

        String[] s = sentence.split(" ");
        String[] out = new String[s.length];

        int i = 0;
        for(String word: s){
            out[i] = tree.getprefix(word);
            i ++;
        }
        String res = String.join(" ", out);
        return res;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        String res = s.replaceWords(new ArrayList<String>(Arrays.asList("cat", "bat", "rat")), "the cattle was rattled by the battery");
        System.out.println(res);
    }
}
