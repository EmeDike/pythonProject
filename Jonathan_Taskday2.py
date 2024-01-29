def list_with_additional_number(input_list):
    remainder = 1
    result = []

    for num in reversed(input_list):
        current_sum = num + remainder
        result.append(current_sum % 10)
        remainder = current_sum // 10

    while remainder > 0:
        result.append(remainder % 10)
        remainder //= 10

    return result[::-1]
