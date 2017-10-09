class Solution {
    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        HashMap<List<Integer>, Integer> memory = new HashMap<>();
        ArrayList<Integer> zero = new ArrayList<>();
        for(int i = 0; i < needs.size(); i++)
            zero.add(0);
        memory.put(zero, 0);
        int calculatedSum = dfs(price, special, memory, needs);
        int regularSum = 0;
        for (int idx = 0; idx < needs.size(); idx ++)
            regularSum += needs.get (idx) * price.get (idx);
        return Math.min (calculatedSum, regularSum);
    }

    public int dfs(List<Integer> price, List<List<Integer>> special, HashMap<List<Integer>, Integer> memory, List<Integer> needs){
        if(memory.containsKey(needs))
            return memory.get(needs);
        int res = Integer.MAX_VALUE;
        for(List<Integer> s : special) {
            List<Integer> needsCopy = new ArrayList<>(needs);
            boolean valid = true;
            for(int i = 0; i < needs.size(); i++) {
                needsCopy.set(i, needsCopy.get(i) - s.get(i));
                if(needsCopy.get(i) < 0) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                res = Math.min(res, s.get(needs.size()) + dfs(price, special, memory, needsCopy));
            }
        }
        if (res == Integer.MAX_VALUE) {
            res = 0;
            for (int idx = 0; idx < needs.size(); idx ++)
                res += needs.get (idx) * price.get (idx);
        }
        memory.put(needs, res);
        return res;
    }
}
