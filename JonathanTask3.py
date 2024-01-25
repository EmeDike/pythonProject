def unpack_list(input_list):
    if input_list:
        return input_list[0]
    else:
        return None


def list_with_additional_number(input_list):
    # Assuming the additional number to be added is 1
    additional_number = 1

    # Create a new list with the elements of the input list and add the additional number
    result_list = [x + additional_number for x in input_list]

    return result_list
