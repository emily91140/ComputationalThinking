import sys

class Employee:
    def __init__(self):
        self.num = 0    #員工編號
        self.salary = 0 #員工薪水
        self.name = ""  #員工姓名
        self.next = None

def delete_ptr(head, ptr):
    #head 該串列
    #ptr 欲刪除位置
    top = head
    #刪除節點在列首
    if ptr.num == head.num:
        head = head.next
        print("已刪除第 %d 號員工 姓名:%s 薪資:%d"%(ptr.num, ptr.name, ptr.salary))
    else:
        #找尋刪除點的前一個位置
        while top.next != ptr:
            top = top.next
        #完成top定位 
        if ptr.next == None: #刪除點位於列尾
            top.next = None
            print("已刪除第 %d 號員工 姓名:%s 薪資:%d"%(ptr.num, ptr.name, ptr.salary))
        else:#刪除點位在中間位置
            top.next = ptr.next
            print("已刪除第 %d 號員工 姓名:%s 薪資:%d"%(ptr.num, ptr.name, ptr.salary))
    return head

if __name__ == "__main__":
    findword = 0
    namedata = ["Allen", "Scott", "Marry", "John", "Mark"]
    num2salarydata = [[1001,32367],[1002,24388],[1003,27556],[1007,31299],[1012,42660]]
    # 輸出 num2salarydata
    print("員工編號 薪水")
    print("------------------------")
    for i in range(len(namedata)):
        print("[%4d] $%5d"%(num2salarydata[i][0], num2salarydata[i][1]))
    print("------------------------")

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

    while(True):
        findword = int(input("請輸入要刪除的員工編號, 要結束刪除動作, 請輸入-1:  "))
        if(findword == -1):
            break
        else:
            ptr = head
            find = 0
            while ptr != None:
                if ptr.num == findword:
                    ptr = delete_ptr(head, ptr)
                    find = find +1
                    head = ptr
                ptr = ptr.next
            if find == 0:
                print("######沒有找到######")

    #結束互動程式 輸出串列
    ptr = head
    print("員工編號\t姓名\t薪水")
    print("=====================")
    while ptr != None:
        print("[%2d %6s %3d] => "%(ptr.num, ptr.name, ptr.salary))
        ptr = ptr.next