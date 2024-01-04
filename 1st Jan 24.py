class Solution:
    def canPair(self, nums, k):
        # Check for odd array length
        if len(nums) % 2 != 0:
            return False

        # Create a frequency map to store remainder counts
        remainder_map = {}
        for num in nums:
            remainder = num % k
            remainder_map[remainder] = remainder_map.get(remainder, 0) + 1

        # Check if pairs with complementary remainders are possible
        for remainder in remainder_map:
            complement = k - remainder  # Calculate the complementary remainder

            # Handle the special case of remainder 0
            if remainder == 0:
                if remainder_map[remainder] % 2 != 0:
                    return False
            # Check for existence of the complementary remainder
            elif complement not in remainder_map:
                return False
            # Check for matching counts of complementary remainders
            elif remainder_map[remainder] != remainder_map[complement]:
                return False

        return True