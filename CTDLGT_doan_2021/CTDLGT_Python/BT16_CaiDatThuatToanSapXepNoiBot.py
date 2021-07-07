def sx_noi_bot(nums):
    bien_thaydoi = True
    while bien_thaydoi:
        bien_thaydoi = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                bien_thaydoi = True

list_random = [5, 2, 1, 8, 4]
sx_noi_bot(list_random)
print(list_random)