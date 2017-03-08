public class Solution {
    public boolean canWinNim(int n) {
        if(n % 4 == 0 && n >= 4)
            return false;
        return true;
    }
}
