x = -12345

if x > 0:
    str1 = str(x)
    str2 = list(str1)
    str2.reverse()
    str3 = ''.join(str2)
    str2 = int(str3)

    if str2 > 2147483648:
        print(0)
    else:
        print(str2)
else:
    x = -x
    str1 = str(x)
    str2 = list(str1)
    str2.reverse()
    str3 = ''.join(str2)
    str2 = int(str3)
    str2 = -str2
    if str2 < -2147483649:
        print(0)
    else:
        print(str2)
    
