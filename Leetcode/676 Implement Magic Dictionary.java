class MagicDictionary {
    class TrieNode {
        public char val;
        public boolean isWord;
        public TrieNode[] children = new TrieNode[26];
        public TrieNode() {}
        public TrieNode(char c){
            val = c;
        }
    }

    private TrieNode root;
    public MagicDictionary() {
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

    public void buildDict(String[] dict) {
        for(String word:dict)
            this.insert(word);
    }

    public boolean searchsub(TrieNode root, String word, int i, int diff){
        if(diff > 1)
            return false;
        TrieNode current = root;
        if(i == word.length())
            return diff == 1 && root.isWord;
        
        char c = word.charAt(i);
        for(int j = 0; j < 26; j++){
            int diff1 = diff;
            if(root.children[j] != null){
                current = root.children[j];
                if(c != 'a'+j)
                    diff1++;
                boolean ret = searchsub(current, word, i+1, diff1);
                if(ret)
                    return true;
            }
        }
        return false;
    }

    public boolean search(String word) {
        TrieNode current = root;
        return searchsub(current, word, 0, 0);
    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dict);
 * boolean param_2 = obj.search(word);
 */
