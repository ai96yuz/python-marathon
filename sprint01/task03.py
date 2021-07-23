def isPalindrome(str):
    counts = {}
    for c in str.lower():
        if c.isalpha():
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    odd_counts = [count for count in counts.values() if count % 2 == 1]
    return len(odd_counts) < 2


print(isPalindrome('abb'))