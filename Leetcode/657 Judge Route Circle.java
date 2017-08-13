public class Solution {
    public boolean judgeCircle(String moves) {
        int[] res;
        res = new int[]{0, 0};
        for(int i = 0; i < moves.length(); i++){
            char c = moves.charAt(i);
            if(c == 'U')
                res[0]++;
            else if(c == 'D')
                res[0]--;
            else if(c == 'L')
                res[1]++;
            else if(c == 'R')
                res[1]--;
        }
        for(int item:res){
            if(item != 0)
                return false;
        }
        return true;
    }
}
