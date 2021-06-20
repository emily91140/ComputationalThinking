import sys

class Employee:
    def __init__(self):
        self.num = 0
        self.salary = 0
        self.name = ""
        self.next = None

def findNode(head, num):
    '用 員工編號搜尋Linked List 回傳ptr'
    ptr = head #從頭開始尋找

    while ptr != None:
        if ptr.num == num:
            return ptr
        else:
            ptr = ptr.next
    return ptr

def insertNode(head, ptr, num, salary, name):
    '插入新節點 並回傳更新的head'
    insert_node = Employee()
    #防呆
    if not insert_node:
        return None
    insert_node.num = num
    insert_node.salary = salary
    insert_node.name = name
    insert_node.next = None
    # 判斷插入位置
    if ptr == None: #插入第一個節點
        insert_node.next = head
        return insert_node
    else:
        if ptr.next == None: #插入在最後一個節點
            ptr.next = insert_node
        else:
            insert_node.next = ptr.next
            ptr.next = insert_node
    return head

if __name__ == "__main__":
    position = 0
    num2salarydata = [[1001,32367],[1002,24388],[1003,27556],[1007,31299],[1012,42660]]
    namedata = ["Allen", "Scott", "Marry", "John", "Mark"]
    # 輸出 num2salarydata
    print("員工編號 薪水")
    print("------------------------")
    for i in range(len(namedata)):
        print("[%4d] $%5d"%(num2salarydata[i][0], num2salarydata[i][1]))
    print("------------------------")

    # 建立串列首
    head = Employee()
    head.next = None
    if not head:
        print("記憶體配置失敗!\n")
        sys.exit(0)
    head.num = num2salarydata[0][0]
    head.name = namedata[0]
    head.salary = num2salarydata[0][1]
    head.next = None
    ptr = head

    # 建立串列
    for i in range(1, len(namedata)):
        newnode = Employee()
        newnode.next = None
        newnode.num = num2salarydata[i][0]
        newnode.name = namedata[i]
        newnode.salary = num2salarydata[i][1]
        newnode.next = None
        ptr.next = newnode
        ptr = ptr.next #注意寫法

    while(True):
        print("請輸入要插入其後的員工編號, 如輸入的編號不在此串列中, ")
        search_num = int(input("新輸入的員工編號將是此串列的串列首, 要結束插入過程, 請輸入-1: "))
        if search_num == -1:
            break
        else:
            ptr = findNode(head, search_num)
            new_num = int(input("請輸入新插入的員工編號: "))
            new_salary = int(input("請輸入新插入的員工薪水: "))
            new_name = input("請輸入新插入的員工姓名: ")
            head = insertNode(head, ptr, new_num, new_salary, new_name)
        print()

    ptr = head
    print("\t員工編號\t姓名\t薪水")
    print("------------------------")
    while ptr != None:
        print("\t[%2d]\t[%-7s]\t[%3d]"%(ptr.num, ptr.name, ptr.salary))
        ptr = ptr.next