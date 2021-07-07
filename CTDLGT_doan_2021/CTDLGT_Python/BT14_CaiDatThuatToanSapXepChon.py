def sx_chon (nums):
    for i in range(len(nums)):
        gia_tri_nho_nhat = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[gia_tri_nho_nhat]:
                gia_tri_nho_nhat = j
        nums[i], nums[gia_tri_nho_nhat] = nums[gia_tri_nho_nhat], nums[i]

list_random = [10, 9, 25, 18, 3]
sx_chon (list_random)
print(list_random)  