result = []
def chan(conso):
    
    if conso == 'a' or conso == 'e' or conso == 'i' or conso == 'o' or conso == 'u' or conso == 'y':
        temp = None
    else:
        temp = '.' + conso
    if temp != None:
        result.append(temp)
    return conso
st=input()
st = st.lower();
li=list(st)
li = [chan(stm) for stm in li]
st = ''.join(result)
print(st)