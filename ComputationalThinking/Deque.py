class Node:
    def __init__(self):
        self.data = 0
        self.next = None

def enqueue(data):
    global front
    global rear
    #建立新節點
    newNode = Node()
    newNode.data = data
    newNode.next = None

    #檢查是否為空佇列 是則將front改成第一個節點
    if rear == None:
        front = newNode
    else:
        #佇列原有節點 舊的rear進行串接
        rear.next = newNode
    #更新結尾指標
    rear = newNode

def dequeue(action):
    global front
    global rear

    #分別處理 從前端取資料 or 從後端取資料
    if action == 1:
        #前端取資料
        if not(front == None) and action == 1:
            #若佇列剩餘最後一個節點 例外處理rear
            if front == rear:
                print('佇列已經為空')
            #取出資料
            data = front.data
            front = front.next #更新front
            #回傳結果
            return data
    elif not(rear==None) and action == 2:
        #暫存前端的指標值, 因為接下來front會被動到
        frontNode = front
        data = rear.data #紀錄尾端data值

        #串列處理更新
        #--------遍歷 找到倒數第二個節點---------
        tmpNode = front
        while front.next != rear and front.next != None:
            front = front.next
            tmpNode = front
        #--------------------------------------
        #front 寫回原本的指標, rear 寫成剛剛找到的倒數第二個節點
        front = frontNode
        rear = tmpNode
        #例外處理
        #當佇列中僅剩下最後一個節點時, 取出資料後, 將front & rear 改回None
        if front.next == None or rear.next == None:
            front = None
            rear = None
        #回傳結果
        return data
    else:
        return -1

if __name__ == '__main__':
    front = rear = None

    print('以LinkedList來實作Deque (Double Ended Queue)')
    print('-------------------------------------------')

    choice = 'a'
    while True:
        choice = input('[a]加入 [d]取出 [e]結束:  ')
        if choice == 'e':
            break
        elif choice == 'a':
            data = int(input('欲加入的元素值:  '))
            enqueue(data)
        elif choice == 'd':
            action = int(input('[1]從前端取出 [2]從後端取出:  '))
            pop_data = dequeue(action)
            if action == 1:
                print('從前端取出之元素值為: %d'%pop_data)
            else:
                print('從後端取出之元素值為: %d'%pop_data)
        else:
            break