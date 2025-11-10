def find(s, n):

    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            elif s[i] + s[j] == n:
                return [i,j]
    return None

print(find([3,2,4],6))