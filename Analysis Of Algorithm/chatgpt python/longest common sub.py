def find_lcs(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Create a table to store lengths
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Build the LCS string by tracing the table
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The LCS is built backwards, so reverse it
    return ''.join(reversed(lcs))

# Example usage
X = "ABAABA"
Y = "BABBAB"

lcs_result = find_lcs(X, Y)
print("LCS is:", lcs_result)
