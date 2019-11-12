import socket
import os
import urllib2
import time
import csv
import getpass

#Listen on TCP
def tcp_sock(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), int(port)))
    s.listen(10)
    raw_input("Press Enter To Close")
    s.close()
    print("Sock closed")


#Open UDP sock
def udp_sock(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((socket.gethostname(), int(port)))
    while True:
        data, addr = s.recvfrom(1024)
        print data
        s.close()


#send UDP message to target
def send_udp(ip, port):
    msg = raw_input('Message: ')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg, (ip, port))

#Test UPD socket UNIX only
def test_udp_range_linux(ip, port_range):
    ports = []
    min_range = port_range[0]
    max_range = port_range[1]
    while min_range < max_range:
        ports.append(min_range)
        min_range += 1
        for port in ports:
            res = os.system("nc -vnzu " + str(ip) + " " + str(port) + " > /dev/null 2>&1")
            if res == 0:
                print("port " + str(port) + "  alive")
            else:
                print("port " + str(port) + " dead")

#Test Access to URLs
def urls_connectivity(url_list):
    failure_list = []

    for url in url_list:
        try:
            resp = urllib2.urlopen(url)
        except urllib2.HTTPError as e:
            print('{} has thrown {}'.format(url, e))
            if '401' in e:
                try_auth = raw_input('{} requires authentication, try again with username and password? (Y/N)'.format(url))
                if try_auth.lower() == 'y':
                    url_connectivity_with_auth(url)
                else:
                    print('Ignoring authentication for {}'.format(url))
            failure_list.append(url)
        except urllib2.URLError as e:
            print('{} could not be resolved. Exception: {}'.format(url, e))
            failure_list.append(url)
        else:
            resp_code = resp.getcode()
            if resp_code == 200:
                print('{} is reachable'.format(url))
            elif resp_code == 401:
                try_auth = raw_input('{} requires authentication, try again with username and password? (Y/N)'.format(url))
                if try_auth.lower() == 'y':
                    url_connectivity_with_auth(url)
                else:
                    print('Ignoring authentication for {}'.format(url))
            else:
                print('{} is unreachble with response code: {}'.format(url, resp_code))

def url_connectivity_with_auth(url):
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    p = urllib2.HTTPPasswordMgrWithDefaultRealm()
    p.add_password(None, url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(p)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    try:
        resp = urllib2.urlopen(url)
    except urllib2.HTTPError as e:
        print('{} has thrown {}'.format(url, e))
    except urllib2.URLError as e:
        print('{} could not be resolved. Exception: {}'.format(url, e))
    else:
        resp_code = resp.getcode()
        if resp_code == 200:
            print('{} is reachable'.format(url))
        else:
            print('{} is unreachble with response code: {}'.format(url, resp_code))

#Test connectivity on TCP socket
def connectivity_check(ip, port): #1
    e = "N/A"
    s = socket.socket()
    s.settimeout(15)
    status = bool
    try:
        s.connect((ip, int(port)))
        status = True
    except Exception as e:
        print("Could not connect to {0}:{1}. With exception: {2}").format(ip, port, e)
        status = False
    finally:
        s.close()
        return status, e

def write_to_csv(csv_name, to_write):
    with open(csv_name, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(to_write)

# Add test_ports.py from Maestro STB
def user_options():
    print("######################################################################### \n"
        "## Pick an option from the list:                                       ## \n"
        "## [1] TCP connectivity check on specified IPs and PORTS               ##\n"
        "## [2] Open TCP or UDP socket to test connectivity from a remote Host  ##\n" 
        "## [3] Test connectivity to specified URLs                             ##\n"
        "## [4] Send a message via UDP                                          ##\n" 
        "## [5] Test UDP port range connectivity (unix only)                    ##\n"
        "## [6] Exit                                                            ##\n"
        "#########################################################################\n"
          )
    choice = input(">> ")
    return choice

def ip_port_urls_to_test(usr_choice):
    if usr_choice == 1 or usr_choice == 4:
        ips = raw_input("Enter IPs. If multiple, separate with spaces: ").split(' ')
        ports = raw_input("Enter Ports nb. If multiple, separate with spaces: ").split(' ')
        return ips, ports
    if usr_choice == 2:
        port = input('Enter port to listen on: ')
        return port
    if usr_choice == 3:
        url_list = raw_input("Enter URLs to test, separate with spaces: ").split(' ')
        return url_list
    if usr_choice == 5:
        ip = raw_input("Enter IP: ").split(' ')
        port_range = raw_input('Port range [Example 5000-6000]: ').split('-')
        return ip, port_range

def main():
    while True:
        try:
            user_choice = user_options()
            if user_choice == 1:
                ips, ports = ip_port_urls_to_test(user_choice)
                for ip in ips:
                    for port in ports:
                        connectivity_check(ip, port)
            elif user_choice == 2:
                choice = input("TCP or UDP? \n >> ")
                if choice == 'UDP' or choice == 'udp':
                    port = ip_port_urls_to_test(user_choice)
                    udp_sock(port)
                elif choice == 'TCP' or choice == 'tcp':
                    port = ip_port_urls_to_test(user_choice)
                    tcp_sock(port)
            elif user_choice == 3:
                url_list = ip_port_urls_to_test(user_choice)
                urls_connectivity(url_list)
            elif user_choice == 4:
                ip, port = ip_port_urls_to_test(user_choice)
                send_udp(ip[0], port[0])
            elif user_choice == 5:
                ip, port_range = ip_port_urls_to_test(user_choice)
                test_udp_range_linux(ip, port_range)
            elif user_choice == 6:
                break
        except:
            print("Bad Input.")

main()
