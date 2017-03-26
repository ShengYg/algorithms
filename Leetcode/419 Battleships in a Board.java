public class Solution {
    public int countBattleships(char[][] board) {
        if(board == null || board[0] == null || board[0].length == 0)
            return 0;
        int n = board.length;
        int m = board[0].length;
        int cnt = 0;
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                if(board[i][j] == 'X' && (j == 0 || board[i][j-1] == '.') && (i == 0 || board[i-1][j] == '.'))
                    cnt ++;
        return cnt;
    }
}
