def find_closest_to_zero(nums):
    abs = []
    for num in nums:
        if num < 0:
            abs.append(0 - num)
        else:
            abs.append(num)
    return nums[abs.index(min(abs))]

def main():
    nums1 = [-1, 0]
    nums2 = [4, 3, 8, 1]
    nums3 = [7, -5, -2, -1, 3]
    print(find_closest_to_zero(nums1))
    print(find_closest_to_zero(nums2))
    print(find_closest_to_zero(nums3))

main()