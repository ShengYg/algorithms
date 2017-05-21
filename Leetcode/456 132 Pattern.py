class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s3 = -float('inf')
        st = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while st and nums[i] > st[-1]:
                    s3 = st.pop()
            st.append(nums[i])
        return False
