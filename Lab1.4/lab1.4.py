#https://docs.python.org/3/howto/ipaddress.html
from ipaddress import IPv4Network
from ipaddress import ip_address
import random

random.seed()
random.randint(0x0B000000,0xDF000000)
random.randint(2,5)
"""
Создаем класс, унаследованный от класса IPv4Network
dir(IPv4RandomNetwork)
   
"""
class IPv4RandomNetwork(IPv4Network):
    def __init__(self, p_start=0, p_end=32):
        IPv4Network.__init__(self,
                             (random.randint(0x0B000000, 0xDF000000),
                             random.randint(p_start, p_end)),
                             strict=False
                             )
    def regular(self):
        return self.is_global and not \
            (self.is_multicast or self.is_link_local or \
             self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)
    def not_regular(self):
        return self.is_private and \
            (self.is_multicast or self.is_link_local or \
             self.is_loopback or self.is_private or self.is_reserved or self.is_unspecified)
    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)

list_of_subnets=[]

for i in range (0,10):
    #print(IPv4RandomNetwork(8, 24).regular
    subnet_random_and_reg = IPv4RandomNetwork(8, 24).regular
    list_of_subnets.append(subnet_random_and_reg)
    

IPv4RandomNetwork(8, 24).regular
IPv4RandomNetwork(8, 24).not_regular
IPv4RandomNetwork(8, 24).is_private

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