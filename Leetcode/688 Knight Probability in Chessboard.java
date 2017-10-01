class Solution {
    public boolean inside(int x, int y, int N){
        return (x >= 0 && x < N && y >= 0 && y < N);
    }

    public double knightProbability(int N, int K, int r, int c) {
        int[] dx = new int[]{ 1, 2, 2, 1, -1, -2, -2, -1};
        int[] dy = new int[]{ 2, 1, -1, -2, -2, -1, 1, 2};

        double[][][] dp1 =new double[N][N][K+1];

        for (int i = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                dp1[i][j][0] = 1;

        for (int s = 1; s <= K; ++s){
            for (int x = 0; x < N; ++x){
                for (int y = 0; y < N; ++y){
                    double prob = 0.0;
                    for (int i = 0; i < 8; ++i){
                        int nx = x + dx[i];
                        int ny = y + dy[i];

                        if (inside(nx, ny, N))
                            prob += dp1[nx][ny][s-1] / 8.0;
                    }

                    dp1[x][y][s] = prob;
                }
            }
        }

        return dp1[c][r][K];
    }
}
