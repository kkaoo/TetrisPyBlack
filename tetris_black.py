#UTF-8
import os,sys,time,copy,threading

import keyboard

scr_base = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,'2','0','2','4','0','5',0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],

    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],

    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,0,0,0,0,0,0,0,0,0,0],
    [0,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0],
]

screen = copy.deepcopy(scr_base)
scr_shape = copy.deepcopy(scr_base)
scr2 = copy.deepcopy(scr_base)

zh = "░░▒回懿国乐懿国回懿"

def show(s):
    """显示函数，将缓存列表s刷新到屏幕
    """
    print("\033[F\033[K"*(len(s)), end="") 

    for row in s:
        s = ''
        for bit in row:
            if type(bit) == str:
                s += bit
            elif bit == 0:
                s += '  '
            elif bit < 3:
                s += zh[bit] + zh[bit]
            elif bit > 0 and bit < 9:
                s += zh[bit]
            else:
                s += '||'
        print(s)

_L = [
"1  ",
"1  ",
"11 ",
]

_7 = [
" 2 ",
" 2 ",
"22 "
]

_O = [
"33 ",
"33 ",
"   ",
]

_Z = [
"4  ",
"44 ",
" 4 ",
]

_S = [
" 5 ",
"55 ",
"5  ",
]

_T = [
"6  ",
"66 ",
"6  ",
]

_1 = [
" 7  ",
" 7  ",
" 7  ",
" 7  ",
]

_empty = [
"    ",
"    ",
"    ",
"    ",
]

T = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
]

T3 = [
[0,0,0],
[0,0,0],
[0,0,0],
]

def __copy(a,b):
    for n in range(len(b)):
        for m in range(len(b[n])):
            a[n][m] = b[n][m]

def __add(a,b):
    for n in range(len(b)):
        for m in range(len(b[n])):
            if type(b[n][m]) == int and b[n][m] == 0:
                pass
            else:
                a[n][m] = b[n][m]                         
     

def __doT(w, c=0):
    buf = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    ]

    __copy(buf,w)
    __copy(T, buf)

    for n in range(c):
        T[0][0] = buf[0][3]
        T[0][1] = buf[1][3]
        T[0][2] = buf[2][3]
        T[0][3] = buf[3][3]
        T[1][0] = buf[0][2]
        T[1][1] = buf[1][2]
        T[1][2] = buf[2][2]
        T[1][3] = buf[3][2]
        T[2][0] = buf[0][1]
        T[2][1] = buf[1][1]
        T[2][2] = buf[2][1]
        T[2][3] = buf[3][1]
        T[3][0] = buf[0][0]
        T[3][1] = buf[1][0]
        T[3][2] = buf[2][0]
        T[3][3] = buf[3][0]
        __copy(buf, T)
    return T

def __doT3(w, c=0):
    buf = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    ]

    # 如果是4x4的格子，那么调用doT来旋转
    if len(w) == 4:
        return(__doT(w, c%2))

    # 执行3x3的旋转
    __copy(buf,w)
    __copy(T3, buf)

    for n in range(c):
        T3[0][0] = buf[0][2]
        T3[0][1] = buf[1][2]
        T3[0][2] = buf[2][2]
        T3[1][0] = buf[0][1]
        T3[1][1] = buf[1][1]
        T3[1][2] = buf[2][1]
        T3[2][0] = buf[0][0]
        T3[2][1] = buf[1][0]
        T3[2][2] = buf[2][0]
        __copy(buf, T3)
    return T3

def __clr(scr):
    for m in range(0,len(scr)):
        for n in range(0,len(scr[0])):
            scr[m][n] = 0;


def place(scr, _word,x,y):
    m = 0; n = 0;
    for line in _word:
        for w in line:
            if((m+y) < len(scr)) and ((n+x) < len(scr[0])):
                if(w is ' '):
                    scr[m+y][n+x] = 0
                elif w is '1' or w is '2' or w is '3' or w is '4' or w is '5' or w is '6' or w is '7':
                    scr[m+y][n+x] = int(w)
                else:
                    scr[m+y][n+x] = 8
                n = n + 1;
        m = m + 1;
        n = 0;

word = (_1, _L, _Z, _S, _7, _T, _O)


# 为线程定义函数
def print_time( threadName, delay):
   count = 0
   while True:
      time.sleep(1)
 
# 创建两个线程
try:
   th1 = threading.Thread( target=print_time,args= ("Thread-1", 9, ) )
   th1.start()
except:
   print("Error: unable to start thread")

__copy(scr2, scr_base)

cycle = 0;
count = 0;
offset = 0;
wcnt = 0;
x = 10;
y = 0;
angle = 0;
y_speed = 0;


def keyCallback(k):
    global wcnt,angle,x,y,y_speed
    if(k.name == "left"):
        if(x < 1):
            return
        x_new = x - 1
        if(__shape_detect(wcnt, angle, x_new, y) is False):
            x = x_new

    if(k.name == "right"):
        if(x > 32):
            return
        x_new = x + 1
        if(__shape_detect(wcnt, angle, x_new, y) is False):
            x = x_new

    if(k.name == "space"):
        angle_new = angle + 1
        if(__shape_detect(wcnt, angle_new, x, y) is False):
            angle = angle_new

    if(k.name == "up"):
        angle_new = angle + 1
        if(__shape_detect(wcnt, angle_new, x, y) is False):
            angle = angle_new

    if(k.name == "down"):
        if(y_speed == 0):
            y_speed = 2

    if(k.name == "q"):
        pass

def keyReleaseCallback(k):
    global y_speed
    if(k.name == "down"):
        y_speed = 0

keyboard.on_press(keyCallback)

keyboard.on_release_key('down',keyReleaseCallback)


def __pz_detect(a, b):
    for m in range(0,len(b)):
        for n in range(0,len(b[0])):
            if(b[m][n]!=0) and (a[m][n]!=0):
                return True
    return False

def __shape_detect(shape, angle, x, y):
    __clr(scr_shape);
    place(scr_shape, __doT3(word[shape], angle%4), x, y)
    return __pz_detect(scr_shape, scr_base)


def __reload_screen():
    __clr(scr_shape)
    place(scr_shape, __doT3(word[wcnt], angle%4), x, y)

    __clr(screen)
    __add(screen, scr_base)
    __add(screen, scr_shape)



# 主循环程序
while(True):

    # 将所有幕布集合在一起
    __reload_screen()
    show(screen)
    time.sleep(0.005)

    # 检测是否加速下降
    cycle_max = 25
    if(y_speed ==2 ):
        cycle_max = 1

    # 等待时间到后，就下降一格
    cycle = cycle + 1
    if(cycle > cycle_max):
        cycle = 0;
        y_new = y + 1

        #检测是否发生了碰撞
        if(__shape_detect(wcnt, angle, x, y_new) is True):
            __clr(scr_shape)
            place(scr_shape, __doT3(word[wcnt], angle%4), x, y)
            __add(scr_base, scr_shape)

            y_speed = 1;
            y = 0;
            x = 10;
            wcnt = wcnt + 1;
            if(wcnt >= len(word)):
                wcnt = 0;
        
            z = wcnt + 1;
            if(z >= len(word)):
                z = 0;
            
            #显示右上角的提醒方块
            place(scr_base, _empty, 25, 5)
            place(scr_base, word[z], 25, 5)
        
        else:
            y = y_new
            

        # 扫描行是否满足一条完整的方块
        if False:
            x1 = 3;
            x2 = 20;
        else:
            # 检测方块容器一行有多少个格子
            x1 = 0; #起始格子号码
            x2 = 0; #结束格子号码
            y_index = 2
            for cnt in range(len(scr2[y_index])):
                if x1 == 0:
                    if scr2[y_index][cnt] != 0:
                        x1 = cnt + 1
                else:
                    if scr2[y_index][cnt] != 0:
                        x2 = cnt - 1
                        break;
        
        # 以loopy来扫描整个容量，消除满足条件的方块行
        loopy = len(scr2) - 2         
        for ycnt in range(0, loopy+1):
            y_index = ycnt
        
            chk_0 = False
            for cnt in range(x1, x2+1):
                if scr_base[y_index][cnt] == 0:
                    chk_0 = True
                    break;
        
            if(chk_0 == False):
                # 闪烁3次
                for three in range(3):
                    __clr(screen)
                    __add(screen, scr_base)
                    # __add(screen, scr_shape)

                    for _loopx in range(10):                    
                        show(screen)
                        time.sleep(0.005)

                    for cnt in range(y_index):
                        for cnt in range(x1, x2+1):
                            screen[y_index][cnt] = 0
                                
                    for _loopx in range(10):                    
                        show(screen)
                        time.sleep(0.005)

                # 消失掉
                for cnt in range(y_index):
                    _y = y_index-cnt 
                    for _x in range(x1, x2+1):
                        scr_base[_y][_x] = scr_base[_y-1][_x];
                        if _y-1 == 0:
                            scr_base[_y-1][_x] = 0;

    count = count+1
    if count > 3000000:
        break;
    

