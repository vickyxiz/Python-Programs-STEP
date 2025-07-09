def count(lst):
    freq = {}  # empty dictionary to store frequency
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq
lst = input("Enter the list elements : ").split(',')
result = count(lst)
print("Frequency:", result)