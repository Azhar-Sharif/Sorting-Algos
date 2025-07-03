"""best case time complexity is O(n2)
    Worst case = O(n2)
    space compexity  = O(1)
    Adaptive = NO
    Stable = NO
    Use only for education purpose and learning
"""

def selection_sort(arr):
    n  = len(arr)
    for i in range(n-1):
        mini_index = i
        for j in range(i+1,n):
            if arr[j] < arr[mini_index]:
                mini_index =  j
        arr[mini_index],arr[i] = arr[i],arr[mini_index]

    return arr
def main():
    arr = [2,1,12,45,7,8,3]
    
    print(selection_sort(arr))

main()