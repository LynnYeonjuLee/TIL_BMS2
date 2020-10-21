def strcmp(s1, s2):
    i = 0
    if len(s1) != len(s2):
        return False
    else:
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] != s2[i]:
                return False
            i += 1
    return True



a = 'abc'
b = 'abc'

print(strcmp(a, b))