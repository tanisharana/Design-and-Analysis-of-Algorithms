def lcs(m, n,str1,str2):
    L = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    pos = L[m][n]

    lcs = [""] * (pos+1)
    lcs[pos] = ""

    i = m
    j = n
    while i > 0 and j > 0:

        if str1[i-1] == str2[j-1]:
            lcs[pos-1] = str1[i-1]
            i -= 1
            j -= 1
            pos -= 1

        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1      

    print("LCS is " + "".join(lcs))


str1 = input("enter first string \n")
str2 = input("enter second string \n")
m = len(str1)
n = len(str2)
lcs( m, n,str1,str2)