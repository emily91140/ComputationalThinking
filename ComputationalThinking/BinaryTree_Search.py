class tree:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None
def create_tree(root, val):
    '建立二元樹函數'
    newnode = tree()
    newnode.data = val
    newnode.left = None
    newnode.right = None
    if root == None:
        root = newnode
        return root
    else:
        current = root
        while current != None:
            backup = current
            if current.data > val:
                current = current.left
            else:
                current = current.right
        if backup.data > val:
            backup.left = newnode
        else:
            backup.right = newnode
    return root
def search(ptr, val):
    i = 1
    while True:
        if ptr == None:
            return None
        if ptr.data == val:
            print('共搜尋 %3d 次'%i)
            return ptr
        elif ptr.data > val: #節點值 > 搜尋值
            ptr = ptr.left
        else:
            ptr = ptr.right
        i +=1


if __name__ == "__main__":
    arr = [7, 1, 4, 2, 8, 13, 12, 11, 15, 9, 5]
    ptr = None
    print("原始陣列內容: ")
    for i in range(11):
        ptr = create_tree(ptr, arr[i])
        print("[%2d] "%arr[i], end = " ")
    print()

    search_num = int(input("請輸入搜尋值: "))
    if search(ptr, search_num) != None:
        print("您要找的值 [%3d] 有找到!"%search_num)
    else:
        print("找不到您要找的值")