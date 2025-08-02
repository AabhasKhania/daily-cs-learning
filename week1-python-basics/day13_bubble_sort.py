 # Day 13 – Bubble Sort Visualizer (Text-Based)
# Aabhas Khaniya
# Simple sort algorithm with print steps to see how sorting works.

def bubble_sort(arr):
    n = len(arr)
    print("Initial array:", arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            print(f"Step {i}-{j}: {arr}")
        if not swapped:
            break
    print("✅ Sorted array:", arr)

# Test input
nums = input("Enter numbers separated by space: ")
arr = list(map(int, nums.strip().split()))
bubble_sort(arr)
