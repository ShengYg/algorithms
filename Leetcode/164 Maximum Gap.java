public class Solution {
    // bucket sort
    public int maximumGap(int[] num) {
        if (num == null || num.length < 2)
            return 0;

        int min = num[0];
        int max = num[0];
        for (int i : num) {
            min = Math.min(min, i);
            max = Math.max(max, i);
        }

        int gap = (int) Math.ceil((double) (max - min) / (num.length - 1));
        int[] bucketsMIN = new int[num.length - 1];
        int[] bucketsMAX = new int[num.length - 1];
        Arrays.fill(bucketsMIN, Integer.MAX_VALUE);
        Arrays.fill(bucketsMAX, Integer.MIN_VALUE);

        for (int i : num) {
            if (i == min || i == max)
                continue;
            int idx = (i - min) / gap;
            bucketsMIN[idx] = Math.min(i, bucketsMIN[idx]);
            bucketsMAX[idx] = Math.max(i, bucketsMAX[idx]);
        }

        int maxGap = Integer.MIN_VALUE;
        int previous = min;
        for (int i = 0; i < num.length - 1; i++) {
            if (bucketsMIN[i] == Integer.MAX_VALUE && bucketsMAX[i] == Integer.MIN_VALUE)
                continue;

            maxGap = Math.max(maxGap, bucketsMIN[i] - previous);
            previous = bucketsMAX[i];
        }
        maxGap = Math.max(maxGap, max - previous);
        return maxGap;
    }
}
