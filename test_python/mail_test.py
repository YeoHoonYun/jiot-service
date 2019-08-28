# """
# 이메일 주소로 전송된 이메일을 가져오기 위해 이메일 서비스 업체의 서버와 통신하는 방법을 지정
# """
# import imapclient
# imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# imapObj.login("cjswo9207@gmail.com", "0rhk1tkdl#")
# import pprint
# pprint.pprint(imapObj.list_folders())
# imapObj.select_folder("INBOX", readonly=True)
# imapObj.search(["ALL"])

"""
# SMTP : 인터넷을 선송할 때 사용되는 프로토콜
"""
import smtplib, datetime

class smtp_service:
    def __init__(self, receiver, sender="iot.jigeum@gmail.com"):
        self.smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        # self.smtpObj = smtplib.SMTP('localhost',1025)
        self.sender = sender
        self.receiver = receiver

    def send_mail(self, title , message):
        headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'Content-Disposition': 'inline',
            'Content-Transfer-Encoding': '8bit',
            'From': self.sender,
            'To': self.receiver,
            'Date': datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z'),
            'X-Mailer': 'python',
            'Subject': title
        }

        self.smtpObj.ehlo()
        self.smtpObj.starttls()
        self.smtpObj.login('iot.jigeum@gmail.com', "zpcqseuieddxitju")

        # create the message
        msg = ''
        for key, value in headers.items():
            msg += "%s: %s\n" % (key, value)

        # add contents
        msg += "\n%s\n" % (message)

        self.smtpObj.sendmail(headers['From'], headers['To'], msg.encode("utf8"))

    def smtp_close(self):
        self.smtpObj.quit()

if __name__ == '__main__':
    sender = "cjswo9207@naver.com"
    receiver = "iot.jigeum@gmail.com"
    title = "테스트 메일입니다."
    message = """
        회사 내부에서 사용할 메일 서버를 사용할 예정입니다.
    """
    smtp_service = smtp_service(sender=sender, receiver=receiver)
    smtp_service.send_mail(title, message)
    smtp_service.smtp_close()

