import sys

class Employee:
    def __init__(self):
        self.num = 0    #員工編號
        self.salary = 0 #員工薪水
        self.name = ""  #員工姓名
        self.next = None

def reverse(x):
    p = x       #ptr = head?
    q = None    #before = None?
    #串列反轉 利用3個指標
    while p != None:
        r = q   #last = before?
        q = p
        p = p.next
        q.next = r
    return q

if __name__ == "__main__":
    findword = 0
    namedata = ["Allen", "Scott", "Marry", "John", "Mark"]
    num2salarydata = [[1001,32367],[1002,24388],[1003,27556],[1007,31299],[1012,42660]]

    #--------------------------------------------
    #建立串首
    head = Employee()
    if not head:
        print("記憶體配置失敗!")
        sys.exit(0)
    head.num = num2salarydata[0][0]
    head.name = namedata[0]
    head.salary = num2salarydata[0][1]
    head.next = None

    ptr = head
    #建立後續鏈結
    for i in range(1, len(namedata)):
        newnode = Employee()
        newnode.num = num2salarydata[i][0]
        newnode.name = namedata[i]
        newnode.salary = num2salarydata[i][1]
        newnode.next = None
        #串聯
        ptr.next = newnode
        ptr = ptr.next
    #--------------------------------------------

    ptr = head
    print("原始員工串列節點資料:")
    while ptr != None:
        print("[%2d %6s %3d] => "%(ptr.num, ptr.name, ptr.salary))
        ptr = ptr.next
    print()    
    #串列反轉
    before = reverse(head)
    ptr = before
    print("反轉後員工串列節點資料:")
    while ptr != None:
        print("[%2d %6s %3d] => "%(ptr.num, ptr.name, ptr.salary))
        ptr = ptr.next