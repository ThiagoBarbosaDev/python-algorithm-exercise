def merge_sort(str):
    if len(str) <= 1:
        return str

    mid = len(str) // 2
    left = merge_sort(str[:mid])
    right = merge_sort(str[mid:])

    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def is_anagram(first_string, second_string):
    str1 = "".join(merge_sort(first_string.lower()))
    str2 = "".join(merge_sort(second_string.lower()))
    if len(first_string) == 0 or len(second_string) == 0:
        return (str1, str2, False)
    return (str1, str2, str1 == str2)
