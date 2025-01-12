def subset_sum_backtracking(array, target):
    def backtrack(start, current_subset, current_sum):
        if current_sum == target:
            results.append(list(current_subset))
            return
        if current_sum > target:
            return
        
        for i in range(start, len(array)):
            current_subset.append(array[i])
            backtrack(i + 1, current_subset, current_sum + array[i])
            current_subset.pop()

    results = []
    backtrack(0, [], 0)
    return results

array = [1, 4, 6, 8]
target = 10
output = subset_sum_backtracking(array, target)
print("Subset yang jumlahnya sama dengan target:", output)