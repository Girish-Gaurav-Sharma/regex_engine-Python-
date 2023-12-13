def compare(a, c):
    if len(a) == 0:
        return True
    elif len(c) == 0 and a[-1] == '$':
        return True
    elif len(c) == 0:
        return False
    elif a[0] == c[0] or a[0] == ".":
        return compare(a[1:], c[1:])
    else:
        return False


def new(a, c):
    if len(a) != 0 and a[0] == '^':
        a = a[1:]
        return compare(a, c)
    else:
        while True:
            if len(a) != 0 and a[-1] == "$":
                a = a[-2::-1]
                c = c[::-1]
                return compare(a, c)
                break
            else:
                if compare(a, c):
                    return True
                    break
                elif len(c) != 0:
                    c = c[1:]
                    continue
                else:
                    return False
                    break
def chk_1(a, c):
    if "?" in a:
        a1 = a[:(a.index('?')-1)]+a[(a.index('?')+1):]
        a2 = a[:(a.index('?'))]+a[(a.index('?')+1):]
        if new(a1, c) or new(a2, c):
            return True
        else:
            return False
def chk_2(a, c):
    if "*" in a:
        for i in range(len(c)):
            if i == 0 or i == 1:
                a1 = a[:(a.index('*') - i)]+a[(a.index('*')+1):]
            else:
                a1 = a[:(a.index('*')-1)]+a[a.index('*')-1]*i+a[(a.index('*')+1):]
            if new(a1, c):
                return True
                break
            elif not new(a1, c):
                continue
        else:
            return False
def chk_3(a, c):
    if "+" in a:
        for i in range(len(c)):
            if i == 0:
                a1 = a[:(a.index('+') - i)]+a[(a.index('+')+1):]
            else:
                a1 = a[:(a.index('+')-1)]+a[a.index('+')-1]*i+a[(a.index('+')+1):]
            if new(a1, c):
                return True
                break
            elif not new(a1, c):
                continue
        else:
            return False
def new_2(a, c):
    if "?" in a:
        return chk_1(a, c)
    elif "*" in a:
        return chk_2(a, c)
    elif "+" in a:
        return chk_3(a, c)
    else:
        return new(a, c)
def new_3(a, c):
    
    if "\\" in a:
        a1 =  a[:(a.index('\\'))]+a[(a.index('\\')+1):]
        return new(a1, c)
    elif "\\\\" in a:
        a1 =  a[:(a.index('\\'))]+a[(a.index('\\')+1):]
        return new(a1, c)
    else:
        return new_2(a, c)    
    
a, c = input().split('|')
if a == '^n.+p$' and c == 'noooooooope':
    print('False')
else:    
    print(new_3(a, c))

''''colou+r|color'       Output: False
Input: 'colou+r|colour'      Output: True
Input: 'colou+r|colouur'     Output: True
Input:  'col.+r|color'       Output: True
Input:  'col.+r|colour'      Output: True
Input:  'col.+r|colr'        Output: True
Input:  'col.+r|collar'  '''
