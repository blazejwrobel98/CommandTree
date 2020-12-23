import telnetlib

    #Nawiązanie połączenia
def OpenConnection(IP,login,password):
    try:
        tn = telnetlib.Telnet(IP)
        tn.read_until(b'login:')
        tn.write(login.encode('ascii') + b"\n")
        tn.read_until(b'Password:')
        tn.write(password.encode('ascii') + b"\n")
        return tn
    except Exception as e:
        print(e)
        return False