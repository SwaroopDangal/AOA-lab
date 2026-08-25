def subset_sum_backtracking(weights, M):
    n = len(weights)
    result = []
    X = [0] * n
    total = sum(weights)

    def feasible(idx, current_sum, rem_sum):
        if current_sum > M or current_sum + rem_sum < M:
            return False
        return True

    def backtrack(idx, current_sum, rem_sum):
        if not feasible(idx, current_sum, rem_sum):
            return

        if current_sum == M:
            subset = [weights[i] for i in range(idx) if X[i] == 1]
            result.append(subset)
            return

        if idx >= n:
            return

        # Include weights[idx]
        X[idx] = 1
        backtrack(idx + 1,
                  current_sum + weights[idx],
                  rem_sum - weights[idx])

        # Exclude weights[idx]
        X[idx] = 0
        backtrack(idx + 1,
                  current_sum,
                  rem_sum - weights[idx])

    backtrack(0, 0, total)
    return result


weights = [5, 7, 10, 12, 15, 18, 20]
M = 35
subsets = subset_sum_backtracking(weights, M)
print(f"Subsets summing to {M}:")
for s in subsets:
    print(s)