def subset_sum(arr, target):
    arr = [x for x in arr if x <= target]
    arr.sort()
    n = len(arr)
    if n == 0:
        return False, []

    current_sum = 0
    j = 0
    used_in_greedy = []
    while j < n:
        if current_sum + arr[j] <= target:
            current_sum += arr[j]
            used_in_greedy.append(arr[j])
            if current_sum == target:
                return True, used_in_greedy
            j += 1
        else:
            break

    for k in range(j, n):
        candidate = arr[k]
        if candidate == target:
            return True, [candidate]

        rem = target - candidate
        available = []
        for i in range(n):
            if i == k:
                continue
            num = arr[i]
            if num < candidate and num <= rem:
                available.append(num)
        
        available.sort(reverse=True)
        temp_rem = rem
        used_in_available = []
        for num in available:
            if num <= temp_rem:
                temp_rem -= num
                used_in_available.append(num)
                if temp_rem == 0:
                    subset = [candidate] + used_in_available
                    return True, subset

    return False, []

def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as f:
            target = int(f.readline().strip())
            data_line = f.readline().strip()
            if not data_line:
                arr = []
            else:
                arr = list(map(int, data_line.split()))
        found, subset = subset_sum(arr, target)
        if found:
            print("True")
            print(" ".join(map(str, subset)))
        else:
            print("False")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()