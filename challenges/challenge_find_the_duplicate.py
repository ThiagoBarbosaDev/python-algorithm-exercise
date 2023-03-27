def find_duplicate(nums):
    unique_nums = set()
    if not nums or len(set(nums)) == len(nums):
        return False
    for num in nums:
        if num < 0:
            return False
        if num in unique_nums:
            return num
        unique_nums.add(num)
