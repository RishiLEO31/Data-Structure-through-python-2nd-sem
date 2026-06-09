# Bubble sort in simple
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"Swapped {arr[j]} and {arr[j+1]}: {arr}\n")
            else:
                print(f"\033[0;31mNo swap needed for {arr[j]} and {arr[j+1]}: {arr}\033[0m\n")
    return arr
# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))