def Btree_create(btree, data, length):
    for i in range(1,length):
        level = 1
        while btree[level]!=0:
            if data[i]>btree[level]: #若陣列中的值 大於樹根, 則往右子樹比較
                level = level *2 +1
            else:
                level = level *2
        btree[level] = data[i] #把陣列值放入二元數


if __name__ == "__main__":
    length = 9
    data = [0, 6, 3, 5, 9, 7, 8, 4, 2] #原始陣列
    btree = [0]*16 #存放二元陣列
    print("data: ", data)

    Btree_create(btree, data, length)
    print("btree: ", btree)
