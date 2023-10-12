def solution(s):
    current_longest_nonrepeating_substring = ""
    current_nonrepeating_substring = ""
    for c in s:
        if c in current_nonrepeating_substring:
            a, b = current_nonrepeating_substring.split(c)
            current_nonrepeating_substring = b + c
        else:
            current_nonrepeating_substring += c
            if len(current_nonrepeating_substring) > len(current_longest_nonrepeating_substring):
                current_longest_nonrepeating_substring = current_nonrepeating_substring

    # return len(current_longest_nonrepeating_substring), current_longest_nonrepeating_substring
    return len(current_longest_nonrepeating_substring)
arr = "nndNfdfdf"
print(solution(arr))
