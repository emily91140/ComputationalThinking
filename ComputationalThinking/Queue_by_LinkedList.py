class Student:
    def __init__(self):
        self.name = ''*20
        self.score = 0
        self.next = None

#在尾端將資料存入佇列
def enqueue(name, score):
    global front
    global rear
    
    #新增節點資料
    newNode = Student()
    newNode.name = name
    newNode.score = score
    #連結
    if rear == None: #rear為None 代表此為第一筆資料
        front = newNode
    else:
        rear.next = newNode #將原本最後一個元素的next 連至新增的元素
    #更新指標
    rear = newNode
    newNode.next = None

#從佇列前端取出一個資料
def dequeue():
    global front
    global rear
    if front == None:
        print('佇列已為空')
    else:
        print('姓名:%s\t成績:%d....取出'%(front.name, front.score))
        front = front.next #更新front 至下一個節點

#顯示所有佇列資料
def show_all_queue():
    global front
    global rear
    #設定一個ptr
    ptr = front

    if ptr == None:
        print('佇列為空')
    else:
        while ptr != None:
            print('姓名:%s\t成績:%d....取出'%(ptr.name, ptr.score))
            ptr = ptr.next

if __name__ == '__main__':
    #初始化定位點
    front = rear = None
    #主程式
    selection = 0
    while True:
        selection = int(input('[1]存入 [2]取出 [3]顯示 [4]離開:   '))
        if selection == 4:
            break
        elif selection == 1:
            name = input('姓名:  ')
            score = int(input('成績:  '))
            enqueue(name, score)
        elif selection == 2:
            dequeue()
        else:
            show_all_queue()

