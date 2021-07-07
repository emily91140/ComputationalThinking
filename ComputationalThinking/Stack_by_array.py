MAXSTACK = 100 #定義最大堆疊容量
global stack
stack = [None] * MAXSTACK #堆疊的陣列宣告
top = -1 #堆疊頂端

def isEmpty():
    if top == -1:
        return True
    else:
        return False

def push(data):
    '將data加入堆疊'
    global top
    global MAXSTACK
    global stack

    if top >= MAXSTACK-1:
        print('堆疊已滿 無法再加入堆疊')
    else:
        top +=1
        stack[top] = data #將資料加入堆疊

def pop():
    '從堆疊取出資料'
    global top
    global stack

    if isEmpty():
        print('堆疊是空的')
    else:
        print('彈出的元素為: %d'%stack[top])
        top -=1

if __name__ == '__main__':
    i = 2
    count = 0
    while True:
        i = int(input('要堆入堆疊請按1, 彈出堆疊請按0, 停止操作則輸入-1:  '))
        if i == -1:
            break
        elif i == 1:
            value = int(input('請輸入元素值'))
            push(value)
        elif i == 0:
            pop()
    print('------------------------------')
    if top < 0:
        print('堆疊為空')
    else:
        i = top
        while i >=0:
            print('堆疊彈出順序為: %d'%(stack[i]))
            count += 1
            i = i -1
        print('------------------------------')
