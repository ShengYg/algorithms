public class Solution {
    public int newInteger(int n) {
        int i = 0;
        int res, ret=0;
        while(n > 0){
            res = n % 9;
            n /= 9;
            ret += res * (int)Math.pow((double)10, (double)i);
            i++;
        }
        return ret;
    }
}
