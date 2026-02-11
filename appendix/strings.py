
print("Search for 'ssip' in 'mississippi'")

def search(text, patterntern):
    for i in range(len(text) - len(patterntern) + 1):
        for j in range(len(patterntern)):
            if text[i + j] != patterntern[j]:
                break
        else:
            return i
    return -1

print("Search:", search("mississippi", "ssip"))

def smarter_search(text, patterntern):
    n, m = len(text), len(patterntern)
    i = 0  # index in text
    j = 0  # index in patterntern

    while i < n:
        if text[i] == patterntern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m  # match found
        else:
            if j > 0:
                # key idea: don't restart from scratch
                j = j - 1   # fall back to partial match
            else:
                i += 1
    return -1

print("Smarter search:", smarter_search("mississippi", "ssip"))

def boyer_moore(text, pattern):
    m, n = len(pattern), len(text)
    
    # Preprocess last occurrence of each character
    last = {c: i for i, c in enumerate(pattern)}
    
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[i+j]:
            j -= 1
        if j < 0:
            print(f"Match at index {i}")
            i += m  # shift by pattern length after match
        else:
            i += max(1, j - last.get(text[i+j], -1))  # jump using last occurrence
    return i 

print("Boyer-Moore (index of last character):", boyer_moore("mississippi", "ssip"))



