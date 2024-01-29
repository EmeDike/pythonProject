def return_duplicates(my_list):
    count_dict = {}
    for num in my_list:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    for num, count in count_dict.items():
        if count > 1:
            return num

    return None
