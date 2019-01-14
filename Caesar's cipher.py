def chipher(a, b):
    res = ""
    if a.isalpha():
        for i in a:
            arg = chr(ord(i) + b)
            res += arg
        print(res)
