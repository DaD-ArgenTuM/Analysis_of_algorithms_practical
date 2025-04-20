def naive_match_recursive(text, pattern, i=0):
    n = len(text)
    m = len(pattern)
    
    if i > n - m:
        return

    def match(j):
        if j == m:
            return True
        if text[i + j] != pattern[j]:
            return False
        return match(j + 1)

    if match(0):
        print(f"Pattern found at index {i}")

    naive_match_recursive(text, pattern, i + 1)

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
naive_match_recursive(text, pattern)
