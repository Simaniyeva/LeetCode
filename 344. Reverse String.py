def reverseString(s):
        new = []
        for i in range(len(s) - 1, -1, -1):
            new.append(s[i])
        for i in range(len(s)):
            s[i] = new[i]