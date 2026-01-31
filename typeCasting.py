def typeCast(string):
    length = len(string)-1
    i=0
    final=0
    while i<len(string) and length>=0:
        adder=((ord(string[i])-ord('0'))*(10**length))
        final+=adder
        print(final)
        i+=1
        length-=1
    return final
print(type(typeCast('13488')))