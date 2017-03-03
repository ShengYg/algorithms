//min-heap
public class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for(int val: nums){
            heap.offer(val);
            if(heap.size() > k)
                heap.poll();
        }
        return heap.peek();
    }
}
