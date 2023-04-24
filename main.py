from telebot import TeleBot, types
import psutil ,os,time


# class Settings_Apps:
#     def __init__(self,Process_Name):
#         self.Process_Name = Process_Name
#         self.Target = ""
#         self.Threads = ""
#         self.NumberOfWindow = 1
#         self.LengthAcc = 0
#         self.LengthProxy = 0
#         self.test = Center()
        
#     def Set_Threads(self,message): 
#         self.Threads = message.text.replace(" ",'');
#         if self.Process_Name == "test":
#             self.test.bot.send_message(self.test.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}',reply_markup= self.test.ButtonsProgram())
            
                
#         elif Process_Name == "Checker":
#             Center().bot.send_message(Center().id, text = f'Icant Set This Option', reply_markup = Center().main());
#             Center().bot.register_next_step_handler(Process_Name,Center().ma)



    # def Set_NumberOfWindow(self,message,Process_Name) -> str : self.NumberOfWindow = message.text.replace(" ",'');#self.Center.bot.register_next_step_handler(message,self.Center.run)
    # def Set_Proxy_Writing(self,message,Process_Name) :
    #         with open("proxies.txt",'w',encoding="utf-8") as file: 
    #             for i in message.text.splitlines():
    #                 x = i.replace(" ",'')
    #                 file.write(f"{x}\n")
    #         self.LengthProxy = len(open("proxies.txt","r").read().splitlines())
           
    # def Set_Proxy_TextFile(self,message):
    #     try:
    #         file_id = message.document.file_id
    #         file_name = message.document.file_name  
    #         if ".txt" in file_name:
    #             file_path = bot.get_file(file_id).file_path
    #             downloaded_file = bot.download_file(file_path)
    #             with open("proxies.txt", 'wb') as new_file:
    #                 new_file.write(downloaded_file)
    #             self.LengthProxy = len(open("proxies.txt","r").read().splitlines())
    #             #self.Center.bot.register_next_step_handler(message,self.Center.run)
    #     except:pass
    # def Set_Accounts_Writing(self,message) :
    #     with open("Accounts.txt",'w',encoding="utf-8") as file: 
    #         for i in message.text.splitlines():
    #             x = i.replace(" ",'')
    #             file.write(f"{x}\n")
    #     self.LengthAcc = len(open("Accounts.txt","r").read().splitlines())
    #    # self.Center.bot.register_next_step_handler(message,self.Center.run)
    # def Set_Accounts_TextFile(self,message):
    #     try:
    #         file_id = message.document.file_id
    #         file_name = message.document.file_name  
    #         if ".txt" in file_name:
    #             file_path = bot.get_file(file_id).file_path
    #             downloaded_file = bot.download_file(file_path)
    #             with open("Accounts.txt", 'wb') as new_file:
    #                 new_file.write(downloaded_file)
    #             self.LengthAcc = len(open("Accounts.txt","r").read().splitlines())
    #             #self.Center.bot.register_next_step_handler(message,self.Center.run)
    #     except:pass
    
        

    
class Center:
    def __init__(self,id,BotTele):
        self.id = id
        self.Target = ""
        self.Threads = ""
        self.NumberOfWindow = 1
        self.LengthAcc = 0
        self.LengthProxy = 0
        self.bot = BotTele
        self.Apps = None;

    def main(self):
        button = types.ReplyKeyboardMarkup(True)
        button.row("My Program")

        return button

    def ButtonsProgram(self):
        button = types.ReplyKeyboardMarkup(True)
        button.row("Start Program")
        button.row("Terminate Program","Suspend Program","Resume Program")
        button.row("Number of windows","Set Threads","Set Target")
        button.row("Set Proxy (Writing)","Set Proxy (text File)")
        button.row("Set Accounts (Writing)","Set Accounts (text File)")
        button.row("Back To Main Page")
        return  button
    def Start_Process(self,message,Process_Name):
        for i in range(int(self.NumberOfWindow)):
            os.system(f"start {Process_Name}")
        self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
        self.bot.register_next_step_handler(message, self.Set_Parameters)



    def Terminate_Process(self,message, Process_Name):
        ListProcess = []
        for process in psutil.process_iter():
            ListProcess.append(process.name())
            if process.name() == Process_Name:
                process.terminate()
                ListProcess.remove(Process_Name)
            
        if Process_Name in ListProcess:
            self.bot.reply_to(message, f"Failed to terminate Process {Process_Name}")
        else:
            self.bot.reply_to(message, f"Successfully Terminated Process {Process_Name}")
        self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
        self.bot.register_next_step_handler(message, self.Set_Parameters)


    def Suspend_Process(self,message, Process_Name):
        for process in psutil.process_iter():
            if process.name() == Process_Name:
                process.suspend()
                status = process.status()
                if status == psutil.STATUS_STOPPED:
                    self.bot.reply_to(message, f"Successfully Suspended Process {Process_Name}")
                else:
                    self.bot.reply_to(message, f"Process {Process_Name} was not suspended")
                return
        self.bot.reply_to(message, f"The Process Name {Process_Name} Not Found")

    def Resume_Process(self,message, Process_Name):
        for process in psutil.process_iter():
            if process.name() == Process_Name:
                process.resume()
                status = process.status()
                if status != psutil.STATUS_STOPPED:
                    self.bot.reply_to(message, f"Successfully Resumed Process {Process_Name}")
                else:
                    self.bot.reply_to(message, f"Process {Process_Name} was not resumed")
                return
        self.bot.reply_to(message, f"The Process Name '{Process_Name}' Not Found")
        self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
        self.bot.register_next_step_handler(message, self.Set_Parameters)
        

    def Set_Threads(self,message,Process_Name): 
        self.Threads = message.text.replace(" ",'')
        if Process_Name == "test":
            self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
            self.bot.register_next_step_handler(message, self.Set_Parameters)
    def Set_Target(self,message,Process_Name): 
        self.Target = message.text.replace(" ",'')
        if Process_Name == "test":
            self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
            self.bot.register_next_step_handler(message, self.Set_Parameters)
    def Set_NumberOfWindow(self,message,Process_Name) :
        self.NumberOfWindow = message.text.replace(" ",'');
        if Process_Name == "test":
            self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
            self.bot.register_next_step_handler(message, self.Set_Parameters)
    def Set_Proxy_Writing(self,message,Process_Name) :
            with open("proxies.txt",'w',encoding="utf-8") as file: 
                for i in message.text.splitlines():
                    x = i.replace(" ",'')
                    file.write(f"{x}\n")
            self.LengthProxy = len(open("proxies.txt","r").read().splitlines())
            if Process_Name == "test":
                self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
                self.bot.register_next_step_handler(message, self.Set_Parameters)
           
    def Set_Proxy_TextFile(self,message,Process_Name):
        try:
            file_id = message.document.file_id
            file_name = message.document.file_name  
            if ".txt" in file_name:
                file_path = bot.get_file(file_id).file_path
                downloaded_file = bot.download_file(file_path)
                with open("proxies.txt", 'wb') as new_file:
                    new_file.write(downloaded_file)
                self.LengthProxy = len(open("proxies.txt","r").read().splitlines())
                if Process_Name == "test":
                    self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
                    self.bot.register_next_step_handler(message, self.Set_Parameters)
        except:pass
    def Set_Accounts_Writing(self,message,Process_Name) :
        with open("Accounts.txt",'w',encoding="utf-8") as file: 
            for i in message.text.splitlines():
                x = i.replace(" ",'')
                file.write(f"{x}\n")
        self.LengthAcc = len(open("Accounts.txt","r").read().splitlines())
        if Process_Name == "test":
                self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
                self.bot.register_next_step_handler(message, self.Set_Parameters)
    def Set_Accounts_TextFile(self,message,Process_Name):
        try:
            file_id = message.document.file_id
            file_name = message.document.file_name  
            if ".txt" in file_name:
                file_path = bot.get_file(file_id).file_path
                downloaded_file = bot.download_file(file_path)
                with open("Accounts.txt", 'wb') as new_file:
                    new_file.write(downloaded_file)
                self.LengthAcc = len(open("Accounts.txt","r").read().splitlines())
                if Process_Name == "test":
                    self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
                    self.bot.register_next_step_handler(message, self.Set_Parameters)
        except:pass
    def Set_Parameters(self,message):
            if message.text == "Start Program":
                cmd = f"test.exe {self.Threads} {self.Target}"
                self.Start_Process(message,cmd)
            elif message.text == "Terminate Program":
                self.Terminate_Process(message,"test.exe")
            elif message.text == "Suspend Program":
                self.Suspend_Process("test.exe")
            elif message.text == "Resume Program":
                self.Resume_Process("test.exe")
            elif message.text == "Number of windows":
                Set = self.bot.reply_to(message, text ='Number of windows : ')
                self.bot.register_next_step_handler(Set,self.Set_NumberOfWindow,"test")
            elif message.text == "Set Threads":
                Set = self.bot.reply_to(message, text ='Enter Threads : ')
                self.bot.register_next_step_handler(Set,self.Set_Threads,"test")
            elif message.text == "Set Target":
                Set = self.bot.reply_to(message, text ='Enter Target : ')
                self.bot.register_next_step_handler(Set,self.Set_Target,"test")
            elif message.text == "Set Proxy (Writing)":
                Set = self.bot.reply_to(message, text ='Set Proxies')
                self.bot.register_next_step_handler(Set,self.Set_Proxy_Writing,"test")
            elif message.text == "Set Proxy (text File)":
                    Set = self.bot.reply_to(message, text ='Set Proxies File')
                    self.bot.register_next_step_handler(Set,self.Set_Accounts_TextFile,"test")
            elif message.text == "Set Accounts (Writing)":
                Set = self.bot.reply_to(message, text ='Set Account/s')
                self.bot.register_next_step_handler(Set,self.Set_Accounts_Writing,"test")
            elif message.text == "Set Accounts (text File)":
                    Set = self.bot.reply_to(message, text ='Set Account/s File')
                    self.bot.register_next_step_handler(Set,self.Set_Accounts_TextFile,"test")
            elif message.text == "Back To Main Page":
                 self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.main())

        
    def run(self):
        @self.bot.message_handler(commands=['start'])
        def start_handler(message):
            self.bot.send_message(self.id, text = "Started", reply_markup = self.main())
        @self.bot.message_handler(content_types = ['text'])
        def App_Pages(message):
            if message.text == "My Program":
                self.bot.send_message(self.id, text = f'Target : {self.Target}\nThreads : {self.Threads}\nLength Accounts : {self.LengthAcc}\nLength Proxy : {self.LengthProxy}\nWindows : {self.NumberOfWindow}', reply_markup = self.ButtonsProgram() )
                self.bot.register_next_step_handler(message, self.Set_Parameters)

       
if __name__ == '__main__':
    id = "Your Id"
    BotTele = TeleBot("Your Token")
    x = Center(id,BotTele)
    x.run()
    x.bot.polling()


