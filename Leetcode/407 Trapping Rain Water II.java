class Solution {
    class Cell{
        int row;
        int col;
        int height;
        Cell(int row, int col, int height){
            this.row = row;
            this.col = col;
            this.height = height;
        }
    }
    
    public int trapRainWater(int[][] heightMap) {
        PriorityQueue<Cell> queue = new PriorityQueue<>(1, (a, b) -> a.height - b.height);
        if(heightMap == null || heightMap.length == 0 || heightMap[0].length == 0)
            return 0;

        int m = heightMap.length;
        int n = heightMap[0].length;
        boolean[][] visited = new boolean[m][n];
        for(int i = 0; i < m; i++){
            visited[i][0] = true;
            visited[i][n - 1] = true;
            queue.add(new Cell(i, 0, heightMap[i][0]));
            queue.add(new Cell(i, n-1, heightMap[i][n-1]));
        }
        for(int j = 0; j < n; j++){
            visited[0][j] = true;
            visited[m - 1][j] = true;
            queue.add(new Cell(0, j, heightMap[0][j]));
            queue.add(new Cell(m-1, j, heightMap[m-1][j]));
        }

        int[][] dirs = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        int res = 0;
        while (!queue.isEmpty()){
            Cell cell = queue.poll();
            for (int[] dir : dirs) {
                int row = cell.row + dir[0];
                int col = cell.col + dir[1];
                if (row >= 0 && row < m && col >= 0 && col < n && !visited[row][col]) {
                    visited[row][col] = true;
                    res += Math.max(0, cell.height - heightMap[row][col]);
                    queue.offer(new Cell(row, col, Math.max(heightMap[row][col], cell.height)));
                }
            }
        }
        return res;
    }
}
