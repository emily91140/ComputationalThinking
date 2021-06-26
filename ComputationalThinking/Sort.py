
#https://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html

def partition(array, front, end):
    pivot = array[end]
    i = front - 1
    
    for j in range(front, end):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    i += 1
    array[i], array[end] = array[end], array[i]
    return i

def quick_sort(array, front, end):
    if front < end:
        pivot = partition(array, front, end)
        quick_sort(array, front, pivot-1)
        quick_sort(array, pivot+1, end)


if __name__ == "__main__":
    arr = [9, 4, 1, 6, 7, 3, 8, 2, 5]
    print(arr)

    quick_sort(arr, 0, len(arr)-1)
    print(arr)