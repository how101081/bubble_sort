def bubble_sort(arr):
    """
    氣泡排序法 (Bubble Sort)
    時間複雜度: O(n²)
    空間複雜度: O(1)
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("原始陣列:", arr)
    sorted_arr = bubble_sort(arr)
    print("排序後陣列:", sorted_arr)