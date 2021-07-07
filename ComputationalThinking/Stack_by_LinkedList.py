# LinkedList 優點為: 可隨時改變串列長度 有效利用記憶體資源
class Node:
    def __init__(self):
        self.data = 0 #資料宣告
        self.next = None #指向下一個節點

top = None #堆疊頂端

def isEmpty():
    global top 
    if top == None:
        return 1
    else:
        return 0

def push(data):
    '將data存入堆疊'
    global top
    new_node = Node()
    new_node.data = data
    new_node.next = top #將新節點指向堆疊頂端
    top = new_node #新節點成為堆疊頂端

def pop():
    '從堆疊取出資料'
    global top
    if isEmpty():
        print('目前為空陣列')
        return -1
    else:
        ptr = top #ptr 指向 堆疊頂端
        top = top.next #將top指向下一個節點
        tmp_data = ptr.data #取出堆疊資料
        return tmp_data

if __name__ == '__main__':
    while True:
        i = int(input('要堆入堆疊請按1, 彈出堆疊請按0, 停止操作則輸入-1:  '))
        if i == -1:
            break
        elif i == 1:
            value = int(input('請輸入元素值'))
            push(value)
        elif i == 0:
            print('堆疊彈出元素為: %d'%(pop()))
    print('------------------------------')
    while(not isEmpty()):
        print('堆疊彈出元素為: %d'%(pop()))