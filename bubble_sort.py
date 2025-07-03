""" Best case time complexity is O(n)
    worst case is O(n2)
    space complexity is O(1)
    Adaptive = yes
    stable = yes
    Adaptive if you optimize with a flag to stop early
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def main():
    arr = [2,1,12,45,7,8,3]
    
    print(bubble_sort(arr))

main()