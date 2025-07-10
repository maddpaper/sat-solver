import sys

def subset_sum(arr, target):
    arr.sort(reverse=True)
    arr = [x for x in arr if x <= target]
    n = len(arr)
    
    for i in range(n):
        current_sum = arr[i]
        if current_sum == target:
            return True
            
        added = False
        for j in range(i+1, n):
            if current_sum + arr[j] <= target:
                current_sum += arr[j]
                added = True
                if current_sum == target:
                    return True
            else:
                continue
                
        if added and current_sum < target:
            break
            
    return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python subset_sum.py <filename> <target>")
        sys.exit(1)
        
    filename = sys.argv[1]
    try:
        target = int(sys.argv[2])
    except ValueError:
        print("Error: Target must be an integer.")
        sys.exit(1)
        
    try:
        with open(filename, 'r') as f:
            data = f.readline().split()
        arr = [int(x) for x in data]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    result = subset_sum(arr, target)
    print(result)

if __name__ == "__main__":
    main()