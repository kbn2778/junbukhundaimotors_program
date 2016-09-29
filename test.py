import time
from tkinter import *

from widget.get.getImformation import *


class interface(junbuk):
    def __init__(self):
        self.t = Tk()
        self.f = Frame(self.t)
        self.menu = '선수단'
        self.logoi = PhotoImage(file='./img/logo.gif')
        try:
            self.Update()
        except Exception:
            self.err=True
    def setInterface_Player(self):
        self.menu = "선수단"
        self.draw_interface()
    def setInterface_Coach(self):
        self.menu = "코치진"
        self.draw_interface()
    def setInterface_Match(self):
        self.menu = "경기 일정"
        self.draw_interface()
    def setInterface_History(self):
        self.menu = "구단 소개"
        self.draw_interface()
    def draw_basic(self):
        self.C0=Canvas(self.f,bg="#22b14c",height=50,width=510)
        self.C0.create_text(30,25,text = self.menu)
        self.C0.grid(row=0,column=0)

        self.C3 = Canvas(self.f, bg="black",width=80,height=550)
        self.C3.create_text(20,25,text="메뉴",fill = "white")
        self.C3.create_image(40, 450, image=self.logoi)
        self.C3.grid(row=0,rowspan = 550,column=3)

        self.B0 = Button(self.f,bg="black",text = '선수단',fg="white",command = lambda : self.setInterface_Player())
        self.B1 = Button(self.f,bg="black",text = '코치진',fg="white",command = lambda :self.setInterface_Coach())
        self.B2 = Button(self.f,bg="black",text = '경기 일정',fg="white",command = lambda :self.setInterface_Match())
        self.B3 = Button(self.f,bg="black",text = '구단 소개',fg="white",command = lambda :self.setInterface_History())

        self.CB0 = self.C3.create_window(28,100,window=self.B0)
        self.CB1 = self.C3.create_window(28,140,window=self.B1)
        self.CB2 = self.C3.create_window(35,180,window=self.B2)
        self.CB3 = self.C3.create_window(35,220,window=self.B3)
    def draw_player(self) :
        self.img = []
        self.var = []
        self.position = []
        self.img_file = []
        j = 0
        h = 84
        w = 64
        forpos = 'a'
        self.C1 = Canvas(self.f, bg='white', height=500, width=500)
        self.S1 = Scrollbar(self.f, orient=VERTICAL,jump=1)
        self.S1.grid(row=1,rowspan=10,column=1)
        for i in self.player:
            if w == 4*124+64:
                w = 64
                h += 200
            if i[0] != forpos:
                if w !=4*124+64 and w !=64 :
                    h+=200
                w = 64
                forpos = i[0]
                h+=20
                self.position.append(self.C1.create_text(30,h,text=forpos))
                h += 200
            try :
                self.img_file.append(PhotoImage(file=i[3]))
                self.img.append(self.C1.create_image(w, h, image=self.img_file[j]))
            except :
                self.img_file.append("no_image")
                self.img.append(self.C1.create_text(w,h,text="no_image"))

            self.var.append(self.C1.create_text(w, h+100, text=i[:3]))
            self.C1.grid(row=1,rowspan = 550,column=0)
            j += 1
            w +=124
            self.S1.config(command=self.C1.yview)
    def draw_match(self):
        j=0
        self.C2 = Canvas(self.f,width = 500,height = 500,bg='white')
        self.S2 = Scrollbar(self.f, orient=VERTICAL, jump=1)

        self.matchl = []
        for i in self.match_i :
            for l in range(0,3) :
                self.matchl.append(self.C2.create_text(250,20+150*j+25*l,text = i[l],fill='black'))
            j+=1
        self.matchl.append(self.C2.create_text(350, 20+150*j+50+20, text="갱신 시각 : " + time.strftime('%c', time.localtime(time.time()))))

        self.C2.grid(row=1,rowspan=550,column=0)
        self.S2.grid(row=1, column=2)
        self.S2.config(command=self.C2.yview)
    def draw_coach(self):
        self.coachi =[
            PhotoImage(file='./img/감독최강희.gif'),PhotoImage(file='./img/코치김상식.gif'),
            PhotoImage(file='./img/코치김이주.gif'),PhotoImage(file='./img/코치박충균.gif'),
            PhotoImage(file='./img/GK코치최은성.gif'),PhotoImage(file='./img/피지컬코치파비오.gif')]
        w=500
        h=300
        coachc=[]
        coachi=[]
        coachl=[]
        coachw=[]
        scrollw=[]
        scroll=[]
        self.C4=Canvas(self.f,width=500,height=500,bg='white')
        for j,i in enumerate(self.coachi) :
            coachc.append(Canvas(self.f,width=w,height=h,bg='white'))
            coachi.append(self.C4.create_image(250,30+300*j,image=i))
            coachl.append(Listbox(self.C4))
            coachw.append(self.C4.create_window(100,180+300*j,window=coachl[j],anchor=W,width=300,height = 120))
            scroll.append([Scrollbar(self.C4,orient=HORIZONTAL),Scrollbar(self.C4,orient=VERTICAL)])
            scroll[j][0].config(command=coachl[j].xview)
            scroll[j][1].config(command=coachl[j].yview)
            scrollw.append(self.C4.create_window(250,240+300*j,window=scroll[j][0]))
            scrollw.append(self.C4.create_window(400,180+300*j,window=scroll[j][1]))
            for l,k in enumerate(self.coach[j]):
                coachl[j].insert(l,k)
        self.C4.grid(row=1,rowspan=550,column=0)
        self.S4=Scrollbar(self.f,orient=VERTICAL,jump=1)
        self.S4.grid(row=1,column=2)
        self.S4.config(command=self.C4.yview)
    def draw_history(self):
        self.b_pi=[]
        for i in self.player:
            if str(self.best_player[0]).split('.')[1].replace(' ','') in i:
                self.b_pi.append(PhotoImage(file=i[3]))
        for i in self.player:
            if str(self.best_player[3]).split('.')[1].replace(' ','') in i:
                self.b_pi.append(PhotoImage(file=i[3]))

        self.C5 = Canvas(self.f,width=500,height=500,bg='white')
        self.C5.create_image(10,60,anchor=W,image=self.logoi)
        self.C5.grid(row=1,rowspan=550,column=0)
        C50= Canvas(self.C5,width=300,height=100)
        C50t=[]
        C50t.append(C50.create_text(100,40,text="순위 : "+self.rank[0],fill='red'))
        C50t.append(C50.create_text(150,40,text=self.rank[1]))
        C50t.append(C50.create_text(120, 60, text=self.rank[2]))
        C50w = self.C5.create_window(160,60,anchor=W,window=C50)
        C51 = Canvas(self.C5,width=200,height=200)
        C51t=[]
        C51t.append(C51.create_image(100,100,image=self.b_pi[0]))
        C51t.append(C51.create_text(10,20,anchor=W,text="최다득점 : "+self.best_player[0]))
        C51t.append(C51.create_text(10, 190, anchor=W, text=self.best_player[1]))
        C51t.append(C51.create_text(120, 190, anchor=W, text=self.best_player[2]))
        C51w = self.C5.create_window(40,225,anchor=W,window=C51)
        C52 = Canvas(self.C5,width=200,height=200)
        C52t=[]
        C52.create_image(100,100,image=self.b_pi[1])
        C52t.append(C52.create_text(10,20,anchor=W,text="최다도움 : "+self.best_player[3]))
        C52t.append(C52.create_text(10,190,anchor=W,text=self.best_player[4]))
        C52t.append(C52.create_text(120, 190, anchor=W, text=self.best_player[5]))
        C52w = self.C5.create_window(260,225,anchor=W,window=C52)
        C53 = Canvas(self.C5,width=420,height=150)
        C53t=[]
        C53t.append(C53.create_text(10,30,anchor=W,text='경기장 주소 : 전주시 덕진구 반월동 763-1 (전주 IC인근)'))
        C53t.append(C53.create_text(10,50,anchor=W,text='구단 사이트 : http://www.hyundai-motorsfc.com/main.asp'))
        C53t.append(C53.create_text(10,70,anchor=W,text='제작자 : 한국디지털미디어고등학교 김병남'))
        C53w = self.C5.create_window(40,420,anchor=W,window=C53)

    def draw_errormessage(self):
        self.C5=Canvas(self.f,width=500,height=300)
        self.C5.create_text(250,150,text=self.errorM)
        self.C5.grid()
    def draw_interface(self):
        for i in self.f.winfo_children():
            i.destroy()
        if not self.err:
            self.draw_basic()
            if self.menu == '선수단':
                self.draw_player()
            if self.menu == "경기 일정":
                self.draw_match()
            if self.menu == '코치진':
                self.draw_coach()
            if self.menu == '구단 소개':
                self.draw_history()
        else :
            self.draw_errormessage()
        self.f.grid()
        self.t.title("전북현대모터스 위젯")

app=interface()
app.draw_interface()
app.t.mainloop()
import sys
from cx_Freeze import setup, Executable
import os
os.environ['TCL_LIBRARY']="C:\Program Files\Python3.5\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\Program Files\Python3.5\tcl\tk8.6"
build_exe_options = {"includes":["sys","tkinter","urllib","urllib.request"],"include_files":app.player[:][3]}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "guifoo",
        version = "0.1",
        description = "gui",
        options = {"build_exe":build_exe_options},
        executables = [Executable("test.py",base=base,targetName="text.exe")]
)