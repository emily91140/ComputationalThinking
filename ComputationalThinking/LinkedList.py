
# Linked List 用法:
# 1. 建立一自訂類別
# 2. 建立一資料欄位
# 3. 建立一指標欄位 (範例為next)

class Student:
    def __init__(self):
        #資料欄位
        self.name = ""
        self.no = ""
        self.Math = 0
        self.Eng = 0
        #指標欄位
        self.next = None

if __name__ == "__main__":
    # 建立初始 Linked List
    head = Student()
    head.next = None #指向下一個節點
    ptr = head #ptr 永遠指向 新節點的記憶體位置
    
    # 互動介面
    select = 0

    while select != 2:
        print( "(1)新增  (2)離開 =>")
        try:
            select = int(input("請輸入一個選項: "))
        except ValueError:
            print("輸入錯誤")
            print("請重新輸入\n")
        if select == 1:
            new_data = Student()
            new_data.name = input("姓名: ")
            new_data.no = input("學號: ")
            new_data.Math = eval(input("數學成績: "))
            new_data.Eng = eval(input("英文成績: "))

            ptr.next = new_data #原本ptr元素更新 next指標
            new_data.next = None #新元素為尾端元素 將next設None
            ptr = ptr.next #更新ptr 指向 最新的元素
