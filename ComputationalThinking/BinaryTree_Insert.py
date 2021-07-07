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
    '搜尋二元樹'
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
def inorder(ptr):
    '中序走訪'
    if ptr != None:
        inorder(ptr.left)
        print('[%2d]'%ptr.data, end = ' ')
        inorder(ptr.right)

if __name__ == "__main__":
    data = [7, 1, 4, 2, 8, 13, 12, 11, 15, 9, 5]
    ptr = None
    print("原始陣列內容")
    # 輸出陣列 並建立二元樹
    for i in range(len(data)):
        ptr = create_tree(ptr, data[i])
        print("[%2d]"%data[i], end = " ")
    print()

    insert_num = int(input("請輸入欲插入之值: "))
    if search(ptr, insert_num) != None:
        print("此二元數已存在此值")
    else:
        create_tree(ptr, insert_num)
        inorder(ptr)

