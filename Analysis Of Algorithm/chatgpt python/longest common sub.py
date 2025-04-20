def lcs(word1, word2):
    m = len(word1)
    n = len(word2)

    # Create a box (table) to keep track of matches
    box = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the box with how many letters match
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                box[i+1][j+1] = box[i][j] + 1
            else:
                box[i+1][j+1] = max(box[i][j+1], box[i+1][j])

    # Now go backward to find the actual matching letters
    i, j = m, n
    result = ""

    while i > 0 and j > 0:
        if word1[i-1] == word2[j-1]:
            result = word1[i-1] + result  # Add to front
            i -= 1
            j -= 1
        elif box[i-1][j] > box[i][j-1]:
            i -= 1
        else:
            j -= 1

    return result

# Try it
word1 = "ABAABA"
word2 = "BABBAB"
print("LCS is:", lcs(word1, word2))
