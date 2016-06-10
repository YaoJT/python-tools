class cau_mail:

    def __init__(self,username,password):
        self.smtp_cau = 'smtp.cau.edu.cn'
        self.__username = username + '@cau.edu.cn'
        self.__password = password
        self.msg = email.MIMEMultipart.MIMEMultipart() 
        self.send_record = {}
        serve = smtplib.SMTP('smtp.cau.edu.cn',25)
        serve.login(self.__username, self.__password)
        serve.close()

    def add_msg(self,text_message,charset='utf-8'):
        text_msg = email.MIMEText.MIMEText(text_message,_charset=charset)
        self.msg.attach(text_msg)
    def add_file(self,file_name):
        basename = os.path.basename(file_name)
        part = email.MIMEText.MIMEText(open(file_name,'rb').read(),'base64', 'gb2312')
        part["Content-Type"] = 'application/octet-stream'
        part["Content-Disposition"] = 'attachment; filename=%s' % basename.encode('gb2312') 
        self.msg.attach(part) 

    def send_mail(self,mail_to,subject=u'默认主题11',record_file = "g:/",max_try = 10,wait_second = 1):
        record_file = os.path.join(record_file,'record.txt')
        self.msg['From'] = self.__username 
        self.msg['To'] = mail_to  
        self.msg['Subject'] = subject 
        self.msg['Date'] = email.Utils.formatdate()
        for i in range(max_try):
            try:
                serve = smtplib.SMTP('smtp.cau.edu.cn',25)
                serve.login(self.__username, self.__password)
                message = serve.sendmail(self.__username,mail_to,self.msg.as_string())
                self.send_record[mail_to] = message
                serve.close()
                print mail_to + u'发送成功'
                break
            except:
                if i == max_try-1:
                    self.send_record[mail_to] = 'error'
                    print mail_to + u'发送失败'
                else: 
                    print mail_to + u' 第{0}次发送失败，将再次发送'.format(i+1)
                time.sleep(wait_second)
        ## recoding
        ff = open(record_file,'a')
        ff.write(time.ctime()+' '+(mail_to+' '+subject +' '+str(self.send_record[mail_to])).encode('utf-8')+'\n')
        ff.close()
        self.msg = email.MIMEMultipart.MIMEMultipart()
