# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from Pairs import *
import datetime
START_DATE = datetime.date(2021, 1, 20)

Participants = ['Godwin Divine','Kudsy','Chigozirim Precious Aviara','Merelam','Favour Uche Asiro','Tochukwu Kingsley Smith','John C Aneke','Chioma Emeakama','Okechukwu Marvellous','Valentine','Jonathan Asogbon','Kingsley']
n = int(len(Participants) / 2)
Stages = []
for i in range(len(Participants) - 1):
    t = Participants[:1] + Participants[-i:] + Participants[1:-i] if i else Participants
    Stages.append(list(zip(t[:n], reversed(t[n:]))))


Pairings = []
for step in Stages:
    for pair in step:
        Pairings.append("{} is praying with {}".format(pair[0], pair[1]))

round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11 = [],[],[],[],[],[],[],[],[],[],[]
days = [round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11]
for i in range(len(days)):
            days[i] = Pairings[(i*6):((i*6)+6)]


round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11 = days[0],days[1],days[2],days[3],days[4],days[5],days[6],days[7],days[8],days[9],days[10]
Rounds = [round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11]


day1 = """Godwin Divine is praying with Kingsley.  
  Kudsy is praying with Jonathan Asogbon.      
  Chigozirim Precious Aviara is praying with Valentine.    
  Merelam is praying with Okechukwu Marvellous.     
  Favour Uche Asiro is praying with Chioma Emeakama.   
  Tochukwu Kingsley Smith is praying with John C Aneke."""

day2 = """Godwin Divine is praying with Jonathan Asogbon.
  Kingsley is praying with Valentine.
  Kudsy is praying with Okechukwu Marvellous.
  Chigozirim Precious Aviara is praying with Chioma Emeakama.
  Merelam is praying with John C Aneke.
  Favour Uche Asiro is praying with Tochukwu Kingsley Smith"""

day3 = """ Godwin Divine is praying with Valentine.
  Jonathan Asogbon is praying with Okechukwu Marvellous.
  Kingsley is praying with Chioma Emeakama.
  Kudsy is praying with John C Aneke.
  Chigozirim Precious Aviara is praying with Tochukwu Kingsley Smith.
  Merelam is praying with Favour Uche Asiro. """

day4 = """ Godwin Divine is praying with Okechukwu Marvellous.
  Valentine is praying with Chioma Emeakama.
  Jonathan Asogbon is praying with John C Aneke.
  Kingsley is praying with Tochukwu Kingsley Smith.
  Kudsy is praying with Favour Uche Asiro.
  Chigozirim Precious Aviara is praying with Merelam. """

day5 = """ Godwin Divine is praying with Chioma Emeakama.
  Okechukwu Marvellous is praying with John C Aneke.
  Valentine is praying with Tochukwu Kingsley Smith.
  Jonathan Asogbon is praying with Favour Uche Asiro.
  Kingsley is praying with Merelam.
  Kudsy is praying with Chigozirim Precious Aviara. """

day6 = """ Godwin Divine is praying with John C Aneke.
  Chioma Emeakama is praying with Tochukwu Kingsley Smith.
  Okechukwu Marvellous is praying with Favour Uche Asiro.
  Valentine is praying with Merelam. 
  Jonathan Asogbon is praying with Chigozirim Precious Aviara.
  Kingsley is praying with Kudsy. """

day7 = """ Godwin Divine is praying with Tochukwu Kingsley Smith.
  John C Aneke is praying with Favour Uche Asiro.
  Chioma Emeakama is praying with Merelam.
  Okechukwu Marvellous is praying with Chigozirim Precious Aviara.
  Valentine is praying with Kudsy.
  Jonathan Asogbon is praying with Kingsley. """

day8 = """ Godwin Divine is praying with Favour Uche Asiro.
  Tochukwu Kingsley Smith is praying with Merelam.
  John C Aneke is praying with Chigozirim Precious Aviara.
  Chioma Emeakama is praying with Kudsy.
  Okechukwu Marvellous is praying with Kingsley.
  Valentine is praying with Jonathan Asogbon. """

day9 = """ Godwin Divine is praying with Merelam.
  Favour Uche Asiro is praying with Chigozirim Precious Aviara.
  Tochukwu Kingsley Smith is praying with Kudsy.
  John C Aneke is praying with Kingsley.
  Chioma Emeakama is praying with Jonathan Asogbon.
  Okechukwu Marvellous is praying with Valentine. """

day10 = """ Godwin Divine is praying with Chigozirim Precious Aviara.
  Merelam is praying with Kudsy.
  Favour Uche Asiro is praying with Kingsley.
  Tochukwu Kingsley Smith is praying with Jonathan Asogbon.
  John C Aneke is praying with Valentine.
  Chioma Emeakama is praying with Okechukwu Marvellous. """

day11 = """ Godwin Divine is praying with Kudsy.
  Chigozirim Precious Aviara is praying with Kingsley.
  Merelam is praying with Jonathan Asogbon.
  Favour Uche Asiro is praying with Valentine.
  Tochukwu Kingsley Smith is praying with Okechukwu Marvellous.
  John C Aneke is praying with Chioma Emeakama. """

DAYS = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11]


Recipients = """ godwindivine362@gmail.com,
Kudsysoma@gmail.com,
aviarachigozirimprecious@gmail.com,
merelam22@gmail.com,
favourasiro@gmail.com,
tochukwukingsley93@gmail.com,
aneke.chukwunonso@gmail.com,
chiomaemeakama@gmail.com,
okechukwumarvelous1@gmail.com,
ifaugustine94@gmail.com,
asogbon.jonathan@gmail.com,
Bigmodo@gmail.com """
def send_email(content):
    body = content

    message_body = """
Hi there!

<p> Here is today's partnership schedule
</p>
{}
""".format(body)
    message = Mail(
        from_email='Chabod@resumeflo.com',
        to_emails=['Henry.uwakxy@gmail.com', 'uwaks4arsenal@yahoo.com'],
        subject='Trialing Your Auto-Pairing Scheduler',
        html_content=message_body)
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    today = datetime.datetime.today().date()
    diff = (today - START_DATE).days
    index = (diff % len(DAYS))
    text = DAYS[index]
    try:
        send_email(text)
    except IndexError:
        pass