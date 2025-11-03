import socket
import subprocess
from datetime import datetime

target = (input("Enter the ip address to scan: "))

def port_scan(target,):
    try:
        ip = socket.gethostbyname(target)

        print(f"scanning target {ip}")
        print("Time started: " + str(datetime.datetime.now()))
        
        for port in range(20, 90):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved")
        return False   
    
    except socket.error:
        print("Couldn't connect to the server")
        return False
    return result == 0