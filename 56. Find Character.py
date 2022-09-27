#56. Find Character
haystack = input().lower()
needle = input().lower()
if (len(haystack)> 0 and len(haystack) <= 300 and len(needle) == 1):
    found_index = []
    if (needle in haystack):
        for i in range(len(haystack)):
            if haystack[i] == needle:
               found_index.append(i + 1)
    else:
        print("Not found.")
        quit()
    print('There is/are ', len(found_index),' "', needle, '" ', "in the above sentences.", sep='')
    print("Position: ", end='')
    print(*found_index, sep=', ')