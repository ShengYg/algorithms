public class NumArray {

    public class SegmentTreeNode{
        int start, end;
        SegmentTreeNode left, right;
        int sum;

        public SegmentTreeNode(int start, int end){
            this.start = start;
            this.end = end;
            this.left = null;
            this.right = null;
            this.sum = 0;
        }
    }

    SegmentTreeNode root = null;

    public NumArray(int[] nums) {
        root = buildtree(nums, 0, nums.length - 1);
    }

    public SegmentTreeNode buildtree(int[] nums, int start, int end){
        if(start > end)
            return null;
        else {
            SegmentTreeNode ret = new SegmentTreeNode(start, end);
            if (start == end)
                ret.sum = nums[start];
            else {
                int mid = start + (end - start) / 2;
                ret.left = buildtree(nums, start, mid);
                ret.right = buildtree(nums, mid + 1, end);
                ret.sum = ret.left.sum + ret.right.sum;
            }
            return ret;
        }
    }

    public void update(int i, int val) {
        update(root, i, val);
    }

    public void update(SegmentTreeNode root, int pos, int val){
        if (root.start == root.end)
            root.sum = val;
        else {
            int mid = root.start + (root.end - root.start) / 2;
            if(pos <= mid)
                update(root.left, pos, val);
            else
                update(root.right, pos, val);
            root.sum = root.left.sum + root.right.sum;
        }
    }

    public int sumRange(int i, int j) {
        return sumRange(root, i, j);
    }

    public int sumRange(SegmentTreeNode root, int start, int end) {
        if (root.end == end && root.start == start) {
            return root.sum;
        } else {
            int mid = root.start + (root.end - root.start) / 2;
            if (end <= mid) {
                return sumRange(root.left, start, end);
            } else if (start >= mid+1) {
                return sumRange(root.right, start, end);
            }  else {
                return sumRange(root.right, mid+1, end) + sumRange(root.left, start, mid);
            }
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */
