# Longest Common Subsequence using Dynamic Programming

def longest_common_subsequence(X, Y):
    # Lengths of the two sequences
    m = len(X)
    n = len(Y)

    # Create a 2D DP table to store lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS from the DP table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Return the LCS as a string
    return ''.join(reversed(lcs))

# Example usage
if __name__ == "__main__":
    X = "ABCBDAB"
    Y = "BDCAB"
    result = longest_common_subsequence(X, Y)
    print(f"Longest Common Subsequence: {result}")