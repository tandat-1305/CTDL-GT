def sx_chen(nums):
    for i in range(1, len(nums)):
        muc_de_chen = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > muc_de_chen:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = muc_de_chen

list_random	 = [10, 9, 25, 18, 3]
sx_chen(list_random	)
print(list_random	) 