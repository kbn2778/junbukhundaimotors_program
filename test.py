import time
from tkinter import *
from bs4 import BeautifulSoup
import urllib
from urllib.request import Request

class junbuk:
    player = []
    coachs = []
    coach = []
    cname = []
    match = []
    score = []
    date = []
    when = []
    match_i = []
    err = False
    errorM = "오류 발생\n인터넷연결을 확인해주시기바랍니다."
    rank = []
    best_player = []
    Krank = []

    def getPlayer(self):
        response = urllib.request.Request('http://www.hyundai-motorsfc.com/player/player_list.asp')
        data = urllib.request.urlopen(response).read()
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        imform1 = soup.find_all('div', attrs={'class': 'player_list_box'})
        for i in imform1:
            if len(imform1) > 0:
                for j in i.find_all('div', attrs={'class': 'player_tit'}):
                    pos = str(j.text)
                for j in i.find_all('div', attrs={'class': 'player_name'}):
                    name = str(j.text)
                    self.player.append([pos, name[2:].split('.')[0], name[2:].split('.')[1]])
        imform2 = soup.find_all('div', attrs={'class': 'sub_article_div'})
        for i in imform2:
            for j in i.find_all('div', attrs={'class': 'sub_article_box_schedule'}):
                for l in j.find_all('div', attrs={'class': 'a_rank'}):
                    self.rank.append(l.text)
                for l in j.find_all('div', attrs={'class': 'a_rank_info01'}):
                    self.rank.append(l.text)
                for l in j.find_all('div', attrs={'class': 'a_rank_info02'}):
                    self.rank.append(str(l.text).replace('\n', ''))
        imform3 = soup.find_all('div', attrs={'class': 'a_record_txt'})
        for i in imform3:
            for j in i.find_all('div', attrs={'class': 'player_name'}):
                self.best_player.append(str(j.text).replace('\n', ''))
            for j in i.find_all('div', attrs={'class': 'player_record01'}):
                self.best_player.append(j.text)
    def img_add(self):
        for i in self.player:
            i.append("./img/" + i[1] + i[2] + ".gif")
    def getCoach(self):
        response = urllib.request.Request('http://www.hyundai-motorsfc.com/player/coach.asp')
        data = urllib.request.urlopen(response).read()
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        imform = soup.find_all('div', attrs={'class': 'coach_box'})
        for i in imform:
            for j in i.find_all('div', attrs={'class': 'coach_txt'}):
                self.coachs.append(j.text)
        for i in self.coachs:
            self.coach.append(i.split('\n'))
        name = soup.find_all('div', {'class': "coach_img"})
        for i in name:
            for j in i.find_all('img'):
                self.cname.append(j.get('alt'))
    def getMatch(self):
        response = urllib.request.Request('http://www.hyundai-motorsfc.com/match/match_schedule.asp')
        data = urllib.request.urlopen(response).read()
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        schedule = soup.find_all('div', attrs={'class': 'M_schedule_list'})
        for i in schedule:
            for j in i.find_all('div', attrs={'class': 'M_schedule_team'}):
                self.match += (j.text.split("\n"))
            for j in i.find_all('div', attrs={'class': 'M_schedule_num'}):
                self.score += (j.text.split("\n"))
            for j in i.find_all('div', attrs={'class': 'M_schedule_tit'}):
                self.date.append(j.text)
            for j in i.find_all('div', attrs={'class': 'M_schedule_date'}):
                self.when.append(j.text)
        for i in range(0, int(len(schedule))):
            self.match_i.append(
                [str(self.match[2 * i] + self.score[2 * i] + "vs" + self.score[2 * i + 1] + self.match[2 * i + 1]),
                 str(self.when[int(i)]),
                 str(self.date[int(i)])])

    def Update(self):
        self.getCoach()
        self.getMatch()
        self.getPlayer()
        self.img_add()

    def getKRank(self):
        url = "http://www.kleague.com/KOR_2016/home/home.asp"
        response = urllib.request.Request(url)
        data = urllib.request.urlopen(response).read()
        soup = BeautifulSoup(data, "html.parser", from_encoding="utf-8")
        table = soup.find_all('table', {'class': 'table2'})
        for k, i in enumerate(table):
            for j in i.find_all('tr'):
                self.Krank.append(j.text.split('\n')[1:8])
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
        self.getKRank()
        self.emi = {
            "광주":PhotoImage(file='./em/광주.gif'), "상주":PhotoImage(file='./em/상주.gif'),
            "서울":PhotoImage(file='./em/서울.gif'), "성남":PhotoImage(file='./em/성남.gif'),
            "수원":PhotoImage(file='./em/수원.gif'), "수원FC":PhotoImage(file='./em/수원FC.gif'),
            "울산":PhotoImage(file='./em/울산.gif'), "인천":PhotoImage(file='./em/인천.gif'),
            "전남":PhotoImage(file='./em/전남.gif'), "전북":PhotoImage(file='./em/전북.gif'),
            "제주":PhotoImage(file='./em/제주.gif'), "포항":PhotoImage(file='./em/포항.gif'),
            "강원": PhotoImage(file='./em/강원.gif'), "경남": PhotoImage(file='./em/경남.gif'),
            "고양": PhotoImage(file='./em/고양.gif'), "대구": PhotoImage(file='./em/대구.gif'),
            "대전": PhotoImage(file='./em/대전.gif'), "부산": PhotoImage(file='./em/부산.gif'),
            "부천": PhotoImage(file='./em/부천.gif'), "서울E": PhotoImage(file='./em/서울E.gif'),
            "안산": PhotoImage(file='./em/안산.gif'), "안양": PhotoImage(file='./em/안양.gif'),
            "충주": PhotoImage(file='./em/충주.gif')}
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
    def setInterface_League(self):
        self.menu = "리그 순위"
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
        self.B3 = Button(self.f,bg="black",text='리그 순위',fg='white',command = lambda : self.setInterface_League())
        self.B4 = Button(self.f,bg="black",text = '구단 소개',fg="white",command = lambda :self.setInterface_History())

        self.CB0 = self.C3.create_window(28,100,window=self.B0)
        self.CB1 = self.C3.create_window(28,140,window=self.B1)
        self.CB2 = self.C3.create_window(35,180,window=self.B2)
        self.CB3 = self.C3.create_window(35,220,window=self.B3)
        self.CB4 = self.C3.create_window(35,260,window=self.B4)
    def draw_player(self) :
        self.img = []
        self.var = []
        self.position = []
        self.img_file = []
        j = 0
        h = 84
        w = 64
        forpos = 'a'
        self.C1 = Canvas(self.f, bg='white', height=500, width=500,scrollregion=(0,0,500,2930))
        self.S1 = Scrollbar(self.f, orient=VERTICAL,jump=1)
        self.S1.grid(row=1,rowspan=10,column=1,ipady=220)
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
                self.img.append(self.C1.create_text(w,h,text="no_image"))

            self.var.append(self.C1.create_text(w, h+100, text=i[:3]))
            self.C1.grid(row=1,rowspan = 550,column=0)
            j += 1
            w +=124
            self.S1.config(command=self.C1.yview)
            self.C1.config(yscrollcommand=self.S1.set)
            self.C1.bind('<4>',lambda event : self.C1.yview('scroll',-1,'units'))
            self.C1.bind('<5>',lambda event : self.C1.yview('scroll',1,'units'))
    def draw_match(self):
        j=0
        self.C2 = Canvas(self.f,width = 500,height = 500,bg='white',scrollregion=(0,0,500,1000))
        self.S2 = Scrollbar(self.f, orient=VERTICAL, jump=1)
        em=[]
        self.matchl = []
        for i in self.match_i :
            for l in range(0,3) :
                self.matchl.append(self.C2.create_text(250,20+150*j+25*l,text = i[l],fill='black'))
            try:
                em.append(self.C2.create_image(100, 40 + 150 * j, image=self.emi.get(self.match[2*j])))
            except:
                em.append(self.C2.create_text(100, 40 + 150 * j, text="no_image"))
            try:
                em.append(self.C2.create_image(400, 40 + 150 * j, image=self.emi.get(self.match[2*j+1])))
            except:
                em.append(self.C2.create_text(400, 40 + 150 * j, text="no_image"))
            j += 1
        self.matchl.append(self.C2.create_text(350, 20+150*j+50+20, text="갱신 시각 : " + time.strftime('%c', time.localtime(time.time()))))
        self.S2.config(command=self.C2.yview)
        self.C2.config(yscrollcommand=self.S2.set)
        self.C2.bind('<4>',lambda event : self.C2.yview('scroll',-1,'units'))
        self.C2.bind('<5>',lambda event : self.C2.yview('scroll',1,'units'))
        self.C2.grid(row=1, rowspan=550, column=0)
        self.S2.grid(row=1, column=2,ipady=220)
    def draw_coach(self):
        self.coachi=[]
        for i in self.cname:
            j="./img/"+i.split(' ')[0]+i.split(' ')[1]+".gif"
            try:
                self.coachi.append(PhotoImage(file=j))
            except :
                self.coachi.append(i+"\n(no_image)")
        w=500
        h=300
        coachc=[]
        coachi=[]
        coachl=[]
        coachw=[]
        scrollw=[]
        scroll=[]
        self.C4=Canvas(self.f,width=500,height=500,bg='white',scrollregion=(-40,-40,500,1800))
        for j,i in enumerate(self.coachi) :
            coachc.append(Canvas(self.f,width=w,height=h,bg='white'))
            try :
                coachi.append(self.C4.create_image(250,30+300*j,image=self.coachi[j]))
            except :
                coachi.append(self.C4.create_text(250,30+300*j,text=self.coachi[j]))
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
        self.S4.config(command=self.C4.yview)
        self.C4.config(yscrollcommand=self.S4.set)
        self.C4.bind('<4>', lambda event: self.C4.yview('scroll', -1, 'units'))
        self.C4.bind('<5>', lambda event: self.C4.yview('scroll', 1, 'units'))
        self.S4.grid(row=1, column=2,ipady=220)
    def draw_leage(self):
        self.C6 = Canvas(self.f, width=500, height=500, bg='white',scrollregion=(0,0,550,len(self.Krank)*75))
        self.S3 = Scrollbar(self.f,orient=VERTICAL,jump=1)
        self.S3.config(command=self.C6.yview)
        self.C6.config(yscrollcommand=self.S3.set)
        self.C6.bind('<4>', lambda event: self.C6.yview('scroll', -1, 'units'))
        self.C6.bind('<5>', lambda event: self.C6.yview('scroll', 1, 'units'))
        self.S3.grid(row=1, column=2, ipady=220)

        text = []
        image = []
        for k,i in enumerate(self.Krank):
            a = ''
            for j in i:
                try :
                    a+="%2d"%int(j)+"\t"
                except :
                    a+=j+"\t"
            text.append(self.C6.create_text(250,75*k+10,text=a))
            try :
                if i[1] != "클럽":
                    image.append(self.C6.create_image(35, 75 * k, image=self.emi[i[1]]))
            except :
               image.append(self.C6.create_text(30,75*k+10,text="no_image"))

        self.C6.grid(row=1, rowspan=550, column=0)
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
            if self.menu == "리그 순위":
                self.draw_leage()
        else :
            self.draw_errormessage()
        self.f.grid()
        self.t.title("전북현대모터스 위젯")
app=interface()
app.draw_interface()
app.t.mainloop()
