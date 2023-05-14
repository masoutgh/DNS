import socket

#making a connection:
port = 53
ip = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, port))

#DataBase
database = open("adress.txt", "r")
database = open("F:\address.txt", "r")

#listening line:
while (True):
    data, addr = sock.recvfrom(512)
    response = buildresponse(data)
    sock.sendto(response,addr)

def buildresponse(data):
    
    # Header:
    
    #1st byte:
    ID = data[:2]

    #2nd byte:
    Flags = (int('1000010000000000',2)).to_bytes(2, byteorder='big')

    #3rd byte
    QDCOUNT = (1).to_bytes(2, byteorder='big')
    
    #4th byte:
    ANCOUNT = (1).to_bytes(2, byteorder='big')
    
    #5th byte:
    NSCOUNT = (0).to_bytes(2, byteorder='big')
    
    #6th byte:
    ARCOUNT = (0).to_bytes(2, byteorder='big')

    Header = ID+Flags+QDCOUNT+ANCOUNT+NSCOUNT+ARCOUNT

    #Question:
    #QNAME
    QNAME = data[12:-4]
    temp = QNAME[1:-1].decode('utf-8', 'slashescape')
    request = ''
    for letter in temp:
    	if letter.capitalize() == letter:
		    letter = '.'
        request += letter

    #QTYPE
    QTYPE = (1).to_bytes(2, byteorder='big')

    #QCLASS
    QCLASS = (1).to_bytes(2, byteorder='big')

    Question = QNAME+QTYPE+QCLASS


    #Answer:
    #NAME
    NAME = (int('1100000000001100',2)).to_bytes(2, byteorder='big')

    #TYPE
    TYPE = (1).to_bytes(2, byteorder='big')

    #CLASS
    CLASS = (1).to_bytes(2, byteorder='big')
    
    #TTL
    TTL = (1000).to_bytes(4,byteorder='big')

    #RDLENGTH
    RDLENGTH = (4).to_bytes(2,byteorder='big')

    #RDATA
    RDATA = ''
    database.seek(0)
    for query in database:
        if request in query:
            RDATA = query[query.find(' ')+1:].strip()
            break
    if not RDATA:
        RDATA = '94.232.175.55'
    RDATA = bytes(map(int,RDATA.split('.')))

    Answer = NAME+TYPE+CLASS+TTL+RDLENGTH+RDATA
    
    return Header+Question+Answer