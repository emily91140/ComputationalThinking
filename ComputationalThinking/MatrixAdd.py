# 二維矩陣相加

# 宣告二維矩陣
A = [[1,3,5],[7,9,11],[13,15,17]]
B = [[9,8,7],[6,5,4],[3,2,1]]

# 給定維度N 建立空矩陣C
N = 3
C = [ [None]*N for row in range(N) ]
#print(C)

# C = A + B
for i in range(N):
    for j in range(N):
        C[i][j] = A[i][j] + B[i][j]
#print(C)
print("相加後的C矩陣為:")

# 書中特定輸出格式
for i in range(N):
    for j in range(N):
        print("%d"%C[i][j], end='\t') # https://openhome.cc/Gossip/Python/StringFormat.html
    print()