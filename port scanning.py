import sys
import socket

objetive = socket.gethostbyname(input("insert ip address: "))

print("scaning objetive: " + objetive)

try:
    for port in range(1,160):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((objetive, port))
        if result == 0:
            print("the port {} is open".format(port))
        s.close()
except:
    print("\n loging out..")
    sys.exit()        
