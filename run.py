import device
import telnet
import repository
import time

if __name__=="__main__":
    try:
        Dev = device.Device()
        repository.cls()
        while True:
            repository.cls()
            Dev.Print()
            ask = str(input("START? T/N => "))
            if ask.lower() == "t":
                repository.cls()
                print("zaczynam")
                Dev.CommandTree()
            elif ask.lower() == "n":
                print("kończę")
                time.sleep(3)
                break;
            else:
                repository.cls()
                print("Nie rozpoznano polecenia >> "+ask+" << spróbuj jeszcze raz.")
                time.sleep(3)
    except Exception as e:
        print(e)
