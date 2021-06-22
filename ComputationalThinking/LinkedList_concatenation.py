
import sys
import random

def concatlist(ptr1, ptr2):
    ptr = ptr1
    while ptr.next != None: #若此物件非最後一筆
        ptr = ptr.next
    ptr.next = ptr2 #將 list1 尾端連結至 list2
    return ptr1

class Employee:
    def __init__(self):
        self.num = 0    #員工編號
        self.salary = 0 #員工薪水
        self.name = ""  #員工姓名
        self.next = None

if __name__ == "__main__":
    # data
    namedata1 = ["Allen", "Scott", "Marry", "John", "Mark"]
    namedata2 = ["Kitty", "Emily", "Ann", "Joanna", "Sue"]
    
    findword = 0
    # 暫存資料
    data = [[None]*2 for row in range(len(namedata1))]
    for i in range(len(namedata1)):
        data[i][0] = i+1 #num 員工編號
        data[i][1] = random.randint(51, 100) #salary 員工薪水

    #建立第一個串列
    head1 = Employee()
    if not head1:
        print("記憶體配置失敗!")
        sys.exit(0)
    head1.num = data[0][0]
    head1.name = namedata1[0]
    head1.salary = data[0][1]
    head1.next = None
    ptr = head1

    for i in range(1, len(namedata1)):
        newnode = Employee()
        newnode.num = data[i][0]
        newnode.name = namedata1[i]
        newnode.salary = data[i][1]
        newnode.next = None
        
        ptr.next = newnode
        ptr = ptr.next

    for i in range(len(namedata2)):
        data[i][0] = i+len(namedata1)+1 #num 員工編號
        data[i][1] = random.randint(51, 100) #salary 員工薪水

    #建立第二個串列
    head2 = Employee()
    if not head2:
        print("記憶體配置失敗!")
        sys.exit(0)
    head2.num = data[0][0]
    head2.name = namedata2[0]
    head2.salary = data[0][1]
    head2.next = None
    ptr = head2

    for i in range(1, len(namedata2)):
        newnode = Employee()
        newnode.num = data[i][0]
        newnode.name = namedata2[i]
        newnode.salary = data[i][1]
        newnode.next = None
        
        ptr.next = newnode
        ptr = ptr.next

    i=0
    #兩串列 串聯起來
    ptr = concatlist(head1, head2)
    print("兩鏈結串列相連的結果:")
    while ptr != None:
        print("[%2d %6s %3d] => "%(ptr.num, ptr.name, ptr.salary), end = " ")
        i += 1
        if i >=3: #排版?
            print()
            i = 0
        ptr = ptr.next