
class MapSum {
    class TrieNode {
        public char val;
        public boolean isWord;
        public int value;
        public TrieNode[] children = new TrieNode[26];
        public TrieNode() {}
        public TrieNode(char c){
            val = c;
        }
    }

    private TrieNode root;
    public MapSum() {
        root = new TrieNode();
        root.val = ' ';
    }

    public void insert(String key, int val) {
        TrieNode current = root;
        for(int i = 0; i < key.length(); i++){
            char c = key.charAt(i);
            if(current.children[c - 'a'] == null){
                current.children[c - 'a'] = new TrieNode(c);
            }
            current = current.children[c - 'a'];
        }
        current.isWord = true;
        current.value = val;
    }

    public int sum(String prefix) {
        TrieNode current = root;
        for(int i = 0; i < prefix.length(); i++){
            char c = prefix.charAt(i);
            if(current.children[c - 'a'] == null)
                return 0;
            current = current.children[c - 'a'];
        }
        return searchsub(current);
    }

    public int searchsub(TrieNode root){
        int ret = 0;
        if(root.isWord)
            ret += root.value;
        for(int j = 0; j < 26; j++){
            if(root.children[j] != null){
                TrieNode current = root.children[j];
                ret += searchsub(current);
            }
        }
        return ret;
    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */
