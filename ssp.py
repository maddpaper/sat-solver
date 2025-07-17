def subset_sum(arr, target):
    # Filter out numbers larger than target and sort in ascending order
    arr = [x for x in arr if x <= target]
    arr.sort()
    n = len(arr)
    
    # Handle empty array case
    if n == 0:
        return False, []

    # Phase 1: Greedy accumulation from smallest numbers
    current_sum = 0
    j = 0
    used_in_greedy = []  # Track numbers used in greedy phase
    
    # Iterate through sorted array
    while j < n:
        # Check if adding next number keeps us at or below target
        if current_sum + arr[j] <= target:
            current_sum += arr[j]
            used_in_greedy.append(arr[j])
            # Found exact match!
            if current_sum == target:
                return True, used_in_greedy
            j += 1
        else:
            # Stop when adding next number would exceed target
            break

    # Phase 2: Candidate-based subtraction
    # Start from first number that broke greedy accumulation (index j)
    for k in range(j, n):
        candidate = arr[k]
        # Case 1: Single number equals target
        if candidate == target:
            return True, [candidate]

        # Calculate remainder after using candidate
        rem = target - candidate
        available = []  # Numbers we can use with candidate
        
        # Build available list: numbers < candidate and <= remainder
        for i in range(n):
            if i == k:  # Skip candidate itself
                continue
            num = arr[i]
            if num < candidate and num <= rem:
                available.append(num)
        
        # Sort available numbers in descending order for greedy subtraction
        available.sort(reverse=True)
        temp_rem = rem
        used_in_available = []  # Track numbers used with candidate
        
        # Try to reduce remainder to zero
        for num in available:
            if num <= temp_rem:
                temp_rem -= num
                used_in_available.append(num)
                # Successfully formed subset!
                if temp_rem == 0:
                    subset = [candidate] + used_in_available
                    return True, subset

    # No subset found after all attempts
    return False, []

def main():
    # Get input filename from user
    filename = input("Enter the filename: ")
    try:
        # Read input file
        with open(filename, 'r') as f:
            # First line = target sum
            target = int(f.readline().strip())
            # Second line = space-separated numbers
            data_line = f.readline().strip()
            if not data_line:
                arr = []  # Handle empty array case
            else:
                # Convert to list of integers
                arr = list(map(int, data_line.split()))
        
        # Solve subset sum problem
        found, subset = subset_sum(arr, target)
        
        # Output results
        if found:
            print("True")
            # Print solution subset as space-separated numbers
            print(" ".join(map(str, subset)))
        else:
            print("False")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
