public class Solution {
    public int reversePairs(int[] nums) {
        return mergesort(nums, 0, nums.length - 1);
    }

    public int mergesort(int[] nums, int s, int e){
        if(s >= e)
            return 0;
        int mid = (s + e) / 2;
        int cnt = mergesort(nums, s, mid) + mergesort(nums, mid + 1, e);
        for(int i = s, j = mid + 1; i <= mid; i++){
            while(j <= e && nums[i] / 2.0 > nums[j])
                j++;
            cnt += j - mid - 1;
        }
        Arrays.sort(nums, s, e+1);
        return cnt;
    }
}


public class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length-1);
    }
    private int mergeSort(int[] nums, int l, int r) {
        if (l >= r) return 0;
        int mid = l + (r - l)/2;
        int count = mergeSort(nums, l, mid) + mergeSort(nums, mid + 1, r);
        int[] cache = new int[r - l + 1];
        int i = l, t = l, c = 0;
        for (int j = mid + 1; j <= r; j++, c++) {
            while (i <= mid && nums[i] <= 2 * (long)nums[j]) i++;
            while (t <= mid && nums[t] < nums[j]) cache[c++] = nums[t++];
            cache[c] = nums[j];
            count += mid - i + 1;
        }
        while (t <= mid) cache[c++] = nums[t++];
        System.arraycopy(cache, 0, nums, l, r - l + 1);
        return count;
    }
}
