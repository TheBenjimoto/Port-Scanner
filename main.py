import socket
from colorama import init, Fore

# slow way of doing this

# init()
# GREEN = Fore.GREEN
# RESET = Fore.RESET
# GRAY = Fore.LIGHTBLACK_EX

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