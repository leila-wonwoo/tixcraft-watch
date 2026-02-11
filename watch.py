import requests
from bs4 import BeautifulSoup
import os
import smtplib

URL = "https://tixcraft.com/ticket/area/26_cxm/21777"
KEYWORD = "立即訂購"   # 若頁面出現這種字樣代表有票（可依實際頁面改）

def send_email(subject, body):
    gmail_user = os.environ["dream574839@gmail.com"]
    gmail_pass = os.environ["nnkl hpks koax ihfj"]

    msg = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(gmail_user, gmail_pass)
    server.sendmail(gmail_user, gmail_user, msg)
    server.quit()

def check_ticket():
    r = requests.get(URL, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    text = soup.get_text()

    if KEYWORD in text:
        send_email(
            "🎫 Tixcraft 有票了！",
            f"偵測到可能有票，請立刻查看：\n{URL}"
        )

if __name__ == "__main__":
    check_ticket()
