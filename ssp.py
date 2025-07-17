def subset_sum(arr, target):
    arr = [x for x in arr if x <= target]
    arr.sort()
    n = len(arr)
    if n == 0:
        return False

    current_sum = 0
    j = 0
    while j < n:
        if current_sum + arr[j] <= target:
            current_sum += arr[j]
            if current_sum == target:
                return True
            j += 1
        else:
            break

    for k in range(j, n):
        candidate = arr[k]
        if candidate == target:
            return True
        rem = target - candidate
        available = []
        for i in range(n):
            if i == k:
                continue
            x = arr[i]
            if x < candidate and x <= rem:
                available.append(x)
        available.sort(reverse=True)
        temp_rem = rem
        for num in available:
            if num <= temp_rem:
                temp_rem -= num
                if temp_rem == 0:
                    return True
    return False

def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as f:
            target = int(f.readline().strip())
            data_line = f.readline().strip()
            if data_line == '':
                arr = []
            else:
                arr = list(map(int, data_line.split()))
        result = subset_sum(arr, target)
        print(result)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()