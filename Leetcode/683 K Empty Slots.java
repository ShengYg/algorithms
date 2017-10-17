class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        int N = flowers.length;
        int[] t = new int[N+2];
        for(int i = 0; i < N; i++)
            t[flowers[i]] = i+1;

        int min = N+1;
        for(int i = 1; i+k+1 <= N; i++){
            boolean flag = false;
            for(int j = i+1; j <= i+k; j++){
                if(t[j]<t[i] || t[j]<t[i+k+1]){
                    flag = true;
                    break;
                }
            }
            if(!flag)
                min = Math.min(min, Math.max(t[i], t[i+k+1]));
        }
        if(min < N+1)
            return min;
        else
            return -1;
    }
}
