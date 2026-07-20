def findHighLow(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    max_count = min(frequency.values())
    max_number = 0
    low_count = max(frequency.values())
    low_number = 0

    for key, value in frequency.items():
        if value > max_count:
            max_number = key
            max_count = value
        if value < low_count:
            low_number = key
            low_count = value
    return (max_number, low_number)

print(findHighLow([10, 20, 5,5,5,5 ,20, 20]))
