""" In best case its time complexity is o(n)
    and in worst case o(n2)
    space complexity is o(1)
    adaptive = yes
    stable = yes
    very efficient for nearly sorted data"""


def insertion_sort(arr):
    n = len(arr)
    for index in range(1,n):
        cur_element = arr[index]
        pos = index
        while cur_element < arr[pos-1] and pos > 0:
            arr[pos] = arr[pos-1]
            pos = pos - 1
        arr[pos] =  cur_element
    return arr


def main():
    arr = [2,1,12,45,7,8,3]
    
    print(insertion_sort(arr))

main()