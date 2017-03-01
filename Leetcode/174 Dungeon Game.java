public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length, n = dungeon[0].length;
        dungeon[m-1][n-1] = dungeon[m-1][n-1] > 0 ? 1 : 1 - dungeon[m-1][n-1];
        for(int j = n-2; j >= 0; j--)
            dungeon[m-1][j] = Math.max(dungeon[m-1][j+1] - dungeon[m-1][j], 1);
        for(int i = m-2; i >= 0; --i)
            dungeon[i][n-1] = Math.max(dungeon[i+1][n-1] - dungeon[i][n-1], 1);
        for (int i = m-2; i >= 0;--i)
            for (int j = n-2; j >= 0; --j)
                dungeon[i][j] = Math.max(Math.min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j], 1);
        return dungeon[0][0];
    }
}
