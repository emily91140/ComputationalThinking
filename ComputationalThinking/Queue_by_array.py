import sys

if __name__ == '__main__':
    MAX = 10
    queue = [0]*MAX
    #初始化定位點
    front = rear = -1

    choice = ''

    while rear < MAX-1 and choice != 'e':
        choice = input('[a]存入一個數值  [d]刪除一個數值  [e]跳出此程式:  ')
        if choice == 'a':
            value = int(input('請輸入欲插入數值:  '))
            rear += 1
            queue[rear] = value
        elif choice == 'd':
            if rear > front:
                front += 1
                print('取出的數值為: [%d]'%queue[front])
                queue[front] = 0 #更改queue FIFO 先進先出
            else:
                print('佇列已經為空')
                sys.exit(0)
        else:
            print()

    print('----------------------------------------')
    print('輸出佇列中所有元素')
    if rear == MAX-1:
        print('佇列已滿')
    elif front >= rear:
        print('佇列為空')
    else:
        while rear > front:
            front += 1
            print('[%d]'%queue[front])
        print()
        print('----------------------------------------')
    print()
