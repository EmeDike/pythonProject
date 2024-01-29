def calculate_products(nums):
    n = len(nums)

    result = [1] * n
    left_product = 1

    for i in range(1, n):
        left_product *= nums[i - 1]
        result[i] *= left_product

    right_product = 1
    for i in range(n - 2, -1, -1):
        right_product *= nums[i + 1]
        result[i] *= right_product

    return result
