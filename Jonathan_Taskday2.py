def list_with_additional_number(my_list):
    carry = 1
    result = []

    for num in reversed(my_list):
        current_sum = num + carry
        result.insert(0, current_sum % 10)
        carry = current_sum // 10

    if carry:
        result.insert(0, carry)

    return result
