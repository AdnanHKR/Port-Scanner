import socket
from IPy import IP

# port_num represent if you want to scan specific port
def scan(target): # def scan(target, port_num):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning target] ' + str(target))
    for port in range(1, 500):
    # for port in range(1, port_num):
        scan_port(converted_ip, port)
def check_ip(ip):
    try:
        IP(ip)
        return ip
    except ValueError:
        return socket.gethostbyname(ip)
def get_banner(s):
    return s.recv(1024)
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print("[+] open Port " + str(port) + " : "+ str(banner.decode().strip()))
        except:
            print("[+] open Port " + str(port))
    except:
        pass
        #print("[-] Port " + str(port) + " is closed!.")

if __name__ == "__main__":
    targets = input("[+] Enter target/s to scan(split multiple targets with ,): ")
    #port_num = input("Enter port number you want to scan: ")
    if ',' in targets:
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)
    
