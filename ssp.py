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
        
        total_available = sum(available)
        if rem > total_available:
            continue

        available.sort(reverse=True)
        len_avail = len(available)
        for skip_count in range(len_avail):
            candidate_set = available[skip_count:]
            candidate_set_asc = sorted(candidate_set)
            current_asc = 0
            used_asc = []
            for num in candidate_set_asc:
                if current_asc + num <= rem:
                    current_asc += num
                    used_asc.append(num)
                    if current_asc == rem:
                        full_subset = [candidate] + used_asc
                        return True, full_subset

            current_desc = 0
            used_desc = []
            for num in candidate_set:
                if current_desc + num <= rem:
                    current_desc += num
                    used_desc.append(num)
                    if current_desc == rem:
                        full_subset = [candidate] + used_desc
                        return True, full_subset

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