# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import datetime
START_DATE = datetime.date(2021, 1, 25)

Participants = [ENTER NAMES]
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



DAYS = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14, day15]


Recipients = """ """
def send_email(content):
    body = content

    message_body = """
Good morning beloved.

<p> Here is today's partnership schedule:
{}
</p>

<p> Stay immortal! </p>
""".format(body)
    message = Mail(
        from_email='',
        to_emails=[]
        subject='Prayer-Pairing Schedules',
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
