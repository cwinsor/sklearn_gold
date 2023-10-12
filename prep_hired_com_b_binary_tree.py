def solution(arr):

    def sum_below(my_1_based_index):
        my_0_based_index = my_1_based_index - 1

        my_level = my_1_based_index // 2
        my_offset_in_level = my_1_based_index - (2**my_level)
        
        # print(f"my_1_based_index {my_1_based_index} my_level {my_level} my_offset_in_level {my_offset_in_level}")

        if my_1_based_index > len(arr):
            # print("  is off array")
            return 0, "equal"
        if arr[my_1_based_index - 1] == -1:
            # print("  is a -1 cell")
            return 0, "equal"
        
        my_val = arr[my_1_based_index - 1]
        # print(f"my_val {my_val}")

        down_one_based_base = (2**(my_level+1))
        left_one_based_index  = down_one_based_base + (2*my_offset_in_level) + 0
        right_one_based_index = down_one_based_base + (2*my_offset_in_level) + 1
        # print(f"left_one_based_index {left_one_based_index} right_one_based_index {right_one_based_index}")
        
        sum_left, _ = sum_below(left_one_based_index)
        sum_right, _ = sum_below(right_one_based_index)

        if sum_left > sum_right:
            compare = "left"
        elif sum_right > sum_left:
            compare = "right"
        else:
            compare = "equal"

        total = sum_left + sum_right + arr[my_0_based_index]

        return total, compare

    _, comp = sum_below(1)
    return comp

arr = [3,6,2,9,-1,10]
print(solution(arr))
