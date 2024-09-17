def remove_duplicates(arr):
    if not arr:
        return []
    
    index = 0
    
    for i in range(1, len(arr)):
        if arr[i] != arr[index]:
            index += 1
            arr[index] = arr[i]
    
    return arr[:index + 1]

array = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(array))  
