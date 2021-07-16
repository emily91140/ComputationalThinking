#決定皇后要放的位置
def decide_position(col_value):
    global queen
    global EIGHT
    row = 0
    while row < EIGHT:
        if is_attack(row, col_value) != 1:
            #不會被攻擊
            queen[col_value] = row
            if col_value == 7:
                #print(所有解)
                print_table()
            else:
                #往下一個col 尋找解
                decide_position(col_value + 1)
        row = row + 1
#判斷兩皇后是否會被攻擊
def is_attack(row, col):
    global queen
    #初始預設值
    this_col = 0
    atk = 0 #是否被攻擊
    offset_row = 0
    offset_col = 0
    while(atk != 1) and this_col < col:
        offset_col = abs(this_col - col)
        offset_row = abs(queen[this_col] - row)
        #判斷兩個皇后是否在同一直行橫列, 或對角線上
        if queen[this_col]==row or offset_col == offset_row:
            atk = 1
        this_col = this_col + 1
    return atk
#印出求解結果
def print_table():
    global number
    x = y = 0
    number += 1
    print()
    print('8-queen problem, 第 %d 組解\t'%number)
    for x in range(EIGHT):
        for y in range(EIGHT):
            if x == queen[y]:
                print('<q>', end='')
            else:
                print('<->', end='')
        print('\t')
    input('\n...按下任意鍵繼續...\n')
if __name__ == '__main__':
    EIGHT = 8
    queen = [None]*EIGHT # row = queen[col] 
    
    # 8-queen problemW
    number = 0 #計算總共有幾組解    
    
    decide_position(0)

