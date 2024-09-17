import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    
    
    for i in range(len(arrays)):
        heapq.heappush(min_heap, (arrays[i][0], i, 0))
    
    merged_array = []
    
    
    while min_heap:
        value, array_idx, element_idx = heapq.heappop(min_heap)
        merged_array.append(value)
        
        if element_idx + 1 < len(arrays[array_idx]):
            heapq.heappush(min_heap, (arrays[array_idx][element_idx + 1], array_idx, element_idx + 1))
    
    return merged_array

array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]
array3 = [0, 9, 10, 11]
arrays = [array1, array2, array3]
print(merge_k_sorted_arrays(arrays))  

array1 = [1,3,7]
array2 = [2,4,8]
array3 = [9,10,11]
arrays = [array1, array2, array3]
print(merge_k_sorted_arrays(arrays))  
