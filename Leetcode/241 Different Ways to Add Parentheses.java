public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> ret = new LinkedList<>();
        for (int i = 0; i < input.length(); i++) {
            if(input.charAt(i) == '-' || input.charAt(i) == '+' || input.charAt(i) == '*'){
                List<Integer> part1 = diffWaysToCompute(input.substring(0,i));
                List<Integer> part2 = diffWaysToCompute(input.substring(i+1));
                for(Integer p1: part1){
                    for(Integer p2: part2){
                        int c = 0;
                        switch (input.charAt(i)){
                            case '+': c = p1+p2;
                                break;
                            case '-': c = p1-p2;
                                break;
                            case '*': c = p1*p2;
                                break;
                        }
                        ret.add(c);
                    }
                }
            }
        }
        if (ret.size() == 0) {
            ret.add(Integer.valueOf(input));
        }
        return ret;
    }
}
