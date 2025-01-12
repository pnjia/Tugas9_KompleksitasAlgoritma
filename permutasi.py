def permute_backtracking(array):
    def backtrack(current_permutation, used):
        if len(current_permutation) == len(array):
            results.append(list(current_permutation))
            return
        
        for i in range(len(array)):
            if not used[i]:
                used[i] = True
                current_permutation.append(array[i])
                backtrack(current_permutation, used)
                current_permutation.pop()
                used[i] = False

    results = []
    used = [False] * len(array)
    backtrack([], used)
    return results

array = [1, 2, 3]
output = permute_backtracking(array)
print("Semua permutasi:", output)
