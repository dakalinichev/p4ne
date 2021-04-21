#Слайд 106
from pysnmp.hlapi import * # Импортировать только High-level API
"""
10.31.70.107
SNMPv1
Community public
MIB-переменная для версии SNMPv2-MIB/ sysDescr
MIB-переменная для списка интерфейсов 1.3.6.1.2.1.2.2.1.2
"""

result = getCmd(SnmpEngine(),
	CommunityData("public", mpModel=0),
	UdpTransportTarget(('10.31.70.107', 161)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))
print_snmp(result)


result2 = nextCmd (…, lexicographicMode=False) # Не идти в глубину


snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной

snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной


"""
result — последовательность кортежей (errorIndication, errorStatus, errorIndex, varBinds) Представляет собой генератор, 
реальные SNMP-запросы к устройству выполняются при обращении к элементам генератора
varBinds — список из строк, которые вернуло сетевое устройство в ответ на запрос

"""