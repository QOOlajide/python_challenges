class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        MOD = 10**9 + 7  # For final modulo return
        nums.sort()      # Sort to make min + max check easier

        # Precompute powers of 2 up to len(nums)
        powers = [1] * len(nums)
        for i in range(1, len(nums)):
            powers[i] = (powers[i - 1] * 2) % MOD

        left = 0
        right = len(nums) - 1
        valid_subseq = 0  # Final count of valid subsequences

        # Loop until pointers cross
        while left <= right:
            # Check if the smallest + largest values meet the condition
            if nums[left] + nums[right] <= target:
                # All subsets between left and right are valid
                count = powers[right - left]
                valid_subseq = (valid_subseq + count) % MOD
                left += 1  # Try next bigger min
            else:
                # Too big → try a smaller max
                right -= 1

        return valid_subseq
