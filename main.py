import socket
from colorama import init, Fore
import argparse
from threading import Thread, Lock
from queue import Queue


# slow way of doing this

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
RED = Fore.RED

# def is_port_open(host, port):
#     # creates a new socket
#     s = socket.socket()
#     try:
#         # tries to connect to host using that port
#         s.connect((host, port))
#         # make timeout if you want it a little faster ( less accuracy )
#         # s.settimeout(0.2)
#     except:
#         # cannot connect, port is closed
#         return False
#     else:
#         return True

# host = input("Enter the host:")
# # iterate over ports, from 1 to 1024
# for port in range(1, 6000):
#     if is_port_open(host, port):
#         print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
#     else:
#         print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")

N_THREADS = 180
q = Queue()
print_lock = Lock()

def port_scan(port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        with print_lock:
             print(f"{RED}{host:15}:{port:5} is closed  {RESET}", end='\r')
    else:
        with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
    finally:
        s.close()

def scan_thread():
    global q
    while True:
        # get the port number from the queue
        worker = q.get()
        # scan that port number
        port_scan(worker)
        # tells the queue that the scanning for that port 
        # is done
        q.task_done()


def main(host, ports):
    global q
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)
        # when we set daemon to true, that thread will end when the main thread ends
        t.daemon = True
        # start the daemon thread
        t.start()
    for worker in ports:
        # for each port, put that port into the queue
        # to start scanning
        q.put(worker)
    # wait the threads ( port scanners ) to finish
    q.join()

if __name__ == "__main__":
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("host", help="Host scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, ports)