def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    textList = list(encrypted_text)
    length = len(textList)
    if length % 2 == 0:
        splitOn = length//2
    else:
        splitOn = (length-1)//2
    first = textList[0:splitOn]
    second = textList[splitOn:length]
    
    resultList = [ second[i//2] if i % 2 == 0 else first[(i-1)//2] for i in range(0,length) ]
    result = ''.join(resultList)
    return decrypt(result,n-1)

def encrypt(text, n):
    if n <= 0 :
        return text
    textList = list(text)
    first = textList[::2]
    second = textList[1::2]
    encrypted = second + first
    result = ''.join(encrypted)
    return encrypt(result,n-1)

