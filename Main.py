#기본설정
import tkinter as tk

ScereenNum = 0 #화면에 표시될 변수
sign = {'+':1, '-':2, '/':3, '*':4, 'C':5, '=':6} #기호에 맞는 계산을 하게끔 딕셔너리
saveNum = 0 #수를 저장할 변수
SelectSign = 0 #


#화면 클리어
def clear():
    global ScereenNum,saveNum,SelectSign #전역으로 호출
    ScereenNum = 0 #초기화
    saveNum = 0
    SelectSign = 0
    str_Value.set(ScereenNum) #화면에 표시

#숫자 감지
def NumCheck(value):
    global ScereenNum
    ScereenNum = (ScereenNum*10) + value
    str_Value.set(ScereenNum)


#계산
def Calculate(value):
    global ScereenNum,sign,saveNum,SelectSign
    op = sign[value] #기능선택
    
    if op == 5: #C
        clear()
    
    elif ScereenNum == 0: 
        SelectSign = 0
    
    elif SelectSign == 0: 
        SelectSign = op
        saveNum = ScereenNum
        ScereenNum = 0
        str_Value.set(str(ScereenNum))
    
    elif op == 6: #계산
        if SelectSign == 1: #+
            ScereenNum = saveNum + ScereenNum
        if SelectSign == 2: #-
            ScereenNum = saveNum - ScereenNum
        if SelectSign == 3: #/
            ScereenNum = saveNum / ScereenNum
        if SelectSign == 4: #*
            ScereenNum = saveNum * ScereenNum

        str_Value.set(str(ScereenNum))
        ScereenNum = 0
        saveNum = 0
        SelectSign = 0
    
    else:
        clear()

#입력받기
def but_click(value):
    try:
        value = int(value)
        NumCheck(value)
    except:
        Calculate(value)

#기본구성
window= tk.Tk()
window.title("대충 계산기")

#수 입력 공간
str_Value = tk.StringVar()
str_Value.set(str(ScereenNum))
input = tk.Entry(window, textvariable=str_Value, justify='right', bg='white',fg='red')
input.grid(column=0,row=0,columnspan = 5, ipadx=120,ipady=30)

#리스트형식으로 저장
calNum = [['7','8','9','+',],['4','5','6','-'],['1','2','3','*'],['0','C','=','/']]

#버튼생성
for i,Num in enumerate(calNum):
    for j,Num in enumerate(Num):
        bt = tk.Button(window, text=Num, 
            width=10, 
            height=5, 
            bg= 'white' ,
            fg= 'blue', 
            command= lambda cmd=Num: but_click(cmd)
            )

        bt.grid(column=j, row=(i+1))

#기본설정    
window.mainloop()