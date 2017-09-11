class Solution {
    int[][] dir = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    
    public int cutOffTree(List<List<Integer>> forest) {
        if(forest == null || forest.size() == 0)
            return -1;
        int m = forest.size();
        int n = forest.get(0).size();
        int res = 0;
        List<int[]> heights = new ArrayList<>();
        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                if(forest.get(i).get(j) > 1)
                    heights.add(new int[]{forest.get(i).get(j), i, j} );
            }
        }
        Collections.sort(heights, Comparator.comparingInt(a -> a[0]));

        int start_x = 0, start_y = 0;
        for(int i = 0; i < heights.size(); i++){
            int cnt_steps = BFS(forest, m, n, start_x, start_y, heights.get(i)[1], heights.get(i)[2]);
            if(cnt_steps == -1)
                return -1;
            res += cnt_steps;
            start_x = heights.get(i)[1];
            start_y = heights.get(i)[2];
        }
        return res;
    }

    public int BFS(List<List<Integer>> forest, int m, int n, int start_x, int start_y, int des_x, int des_y){
        if(start_x == des_x && start_y == des_y)
            return 0;
        int steps = 0;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{start_x, start_y});
        int[][] visited = new int[m][n];
        visited[start_x][start_y] = 1;
        while(!q.isEmpty()){
            int qsize = q.size();
            steps++;
            while(qsize-- >0 ){
                int[] cur = q.poll();
                int cur_x = cur[0], cur_y = cur[1];
                for(int k = 0; k < 4; k++){
                    int x = cur_x + dir[k][0], y = cur_y + dir[k][1];
                    if(x>=0 && x<m && y>=0 && y<n && forest.get(x).get(y) > 0 && visited[x][y] == 0){
                        if(x == des_x && y == des_y)
                            return steps;
                        visited[x][y] = 1;
                        q.add(new int[]{x,y});
                    }
                }
            }
        }
        return -1;
    }
}
