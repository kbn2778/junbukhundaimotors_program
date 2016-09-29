from bs4 import BeautifulSoup
import urllib
from urllib.request import Request
class junbuk :
    player=[]
    coachs = []
    coach=[]
    match = []
    score = []
    date = []
    when = []
    match_i = []
    err=False
    errorM="오류 발생\n인터넷연결을 확인해주시기바랍니다."
    rank=[]
    best_player=[]
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
                    self.player.append([pos, name[2:].split('.')[0],name[2:].split('.')[1]])
        imform2=soup.find_all('div',attrs={'class':'sub_article_div'})
        for i in imform2:
            for j in i.find_all('div',attrs={'class':'sub_article_box_schedule'}):
                for l in j.find_all('div',attrs={'class':'a_rank'}):
                    self.rank.append(l.text)
                for l in j.find_all('div',attrs={'class':'a_rank_info01'}):
                    self.rank.append(l.text)
                for l in j.find_all('div',attrs={'class':'a_rank_info02'}):
                    self.rank.append(str(l.text).replace('\n',''))
        imform3 = soup.find_all('div',attrs={'class':'a_record_txt'})
        for i in imform3:
            for j in i.find_all('div',attrs={'class':'player_name'}):
                self.best_player.append(str(j.text).replace('\n',''))
            for j in i.find_all('div',attrs={'class':'player_record01'}):
                self.best_player.append(j.text)
    def img_add(self):
        for i in self.player :
            i.append("./img/" + i[1] + i[2] + ".gif")
    def getCoach(self):
        response = urllib.request.Request('http://www.hyundai-motorsfc.com/player/coach.asp')
        data = urllib.request.urlopen(response).read()
        soup = BeautifulSoup(data, 'html.parser', from_encoding='utf-8')
        imform = soup.find_all('div', attrs={'class': 'coach_box'})
        for i in imform:
            for j in i.find_all('div',attrs={'class':'coach_txt'}) :
                self.coachs.append(j.text)
        for i in self.coachs:
            self.coach.append(i.split('\n'))
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
                [str(self.match[2 * i] + self.score[2 * i] + "vs" + self.score[2 * i + 1] + self.match[2 * i + 1]), str(self.when[int(i / 2)]),
                 str(self.date[int(i / 2)])])
    def Update(self):
        self.getCoach()
        self.getMatch()
        self.getPlayer()
        self.img_add()