#https://docs.python.org/3/howto/ipaddress.html
from ipaddress import IPv4Network
from ipaddress import ip_address
import random

random.seed()
random.randint(0x0B000000,0xDF000000)
random.randint(2,5)

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                             random.randint(p_start, p_end), False),
                             strict=False
                             )

class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                              random.randint(p_start, p_end), False)
                             )

random_network = IPv4RandomNetwork(8)
ipaddress.ip_address(random.randint(0x0B000000,0xDF000000))
net2=IPv4RandomNetwork(1,2)
IPv4RandomNetwork()
her=IPv4Network('192.0.2.0/24')
type(hee)
dir(hee)
help(IPv4Network)
IPv4Network(random.randint(0x0B000000,0xDF000000), 30, strict=False)
IPv4Network(random.randint(0x0B000000,0xDF000000), strict=False)

IPv4Network.