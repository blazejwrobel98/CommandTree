import telnet
import re
import time

class Device:
    def __init__(self):
        self.ip = str(input("Podaj IP: "))
        self.login = str(input("Podaj login: "))
        self.password = str(input("Podaj hasło: "))
        self.tn = telnet.OpenConnection(self.ip,self.login,self.password)
        result = self.CheckAll()
        self.fw = result[0]
        self.boot = result[1]
        self.id = result[2]
        self.sn = result[3]
        self.pn = result[4]
    def CheckAll(self):
        try:
            tn = self.tn
            tn.write(b"terminal length 0\n")
            tn.read_until(b'#')
            #devtype id
            try:
                tn.write(b'show vendor | include DevType \n')
                tn.read_until(b'DevType(ID)')
                s = (tn.read_until(b'\n').decode('ascii').strip())
                id = (s[-3:])
            except Exception as e:
                print("id: ")
                print(e)
            #get show version
            try:
                tn.write(b'show version\n')
                string = str(tn.read_until(b'minutes').decode('ascii'))
            except Exception as e:
                print("show version: ")
                print(e)
            #fw
            try:
                FWare = re.findall("SoftWare.*.Version(.*)",string)
                for i in FWare:
                    fw=i.strip()
            except Exception as e:
                print("fw: ")
                print(e)
            #boot
            try:
                boot = re.search("BootRom.Version(.*)",string)
                boot = (boot.group(0)[15:]).strip()
            except Exception as e:
                print("boot: ")
                print(e)
            #pn
            try:
                pn = re.search('^(.*).Device',string, re.MULTILINE)
                pn = (pn.group(0)[1:]).strip()
            except Exception as e:
                print("pn: ")
                print(e)
            #sn
            try:
                sn = re.search("No.:.*",string)
                sn = (sn.group(0)[4:])
            except Exception as e:
                print("sn: ")
                print(e)
            #result
            try:
                result = [fw ,boot ,id ,sn , pn ]
            except Exception as e:
                print(e)
            return result
        except Exception as e:
            print(e)
    def Print(self):
        print("IP: "+self.ip)
        print("login: "+self.login)
        print("password: "+self.password)
        print("fw: "+self.fw)
        print("boot: "+self.boot)
        print("id: "+self.id)
        print("sn: "+self.sn)
        print("pn: "+self.pn)
    
    def CommandTree(self, command=""):
        try:
           tn = self.tn
           test = command+" ?"
           time.sleep(1)
           tn.write((test).encode('ascii'))
           time.sleep(1)
           line = tn.read_very_eager().decode('ascii')
           lines = line.split('\n')
           comms = []
           for tekst in lines:
               splited = tekst.split('  ')
               try:
                   comms.append(splited[1])
               except:
                   pass
           for comm in comms:
               if "<cr>" in comm:
                   print(comm)
                   return
               else:
                   print(comm)
                   self.CommandTree(comm)
               return
           input()
        except Exception as e:
            print(e)
