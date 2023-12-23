def convert(s,numRows):
    snew = ''
    for i in range(numRows):
        k = i
        while k<len(s):
            snew += s[k]
            k = k + numRows + 1
    return snew
s = input()
numRows = int(input())
print(convert(s,numRows))
