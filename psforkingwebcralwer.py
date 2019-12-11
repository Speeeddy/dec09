import multiprocessing
from email.mime.text import MIMEText
from smtplib import SMTP
import requests

"""https://codeshare.io/anVXEV"""


def send_alert_email(from_addr, to_addr, subject, message):
    msg = MIMEText(message)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    smtp = SMTP('localhost')
    # smtp.login()
    smtp.debuglevel = 1
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    smtp.close()


def web_crawler(q):
    """child process"""
    try:
        p_name = multiprocessing.current_process().name
        url = q.get()  # block
        response = requests.get(url)
        print(f'{p_name}: {url}: {response.text[:128]}')
    except requests.exceptions.ConnectionError as err:
        subject = f'{p_name}: error in {url}'
        send_alert_email('ravi@localhost', 'training@localhost', subject, str(err))


def main():
    """producer & consumer"""
    urls = ['http://kernel.org', 'http://linux.org', 'http://python.org', 'http://golang.org', 'http://perllang.org']
    queue = multiprocessing.Queue()  # IPC

    for url in urls:
        queue.put(url)  # add item into queue

    for url in urls:
        p = multiprocessing.Process(target=web_crawler, args=(queue,))
        p.start()

    for child in multiprocessing.active_children():
        child.join()


if __name__ == '__main__':
    main()
