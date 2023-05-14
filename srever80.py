import socket

host = '127.0.0.1'
port = 80

# TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

while (True):
	info, addr = sock.accept()
	data = info.recv(1000)

	# request analysing
	httpRequest = list()
	for line in data.decode("UTF-8").split('\r\n'):
		httpRequest.append(line.split())
	Method, URL, Ver = httpRequest[0]

	# answer to GET
	if Method == "GET":
		if URL == "/":
			fileDirectory = "myserver/index.html"
		else:
			fileDirectory = "myServer"+URL


		try:
			htmlData = open(fileDirectory).read()
			htmlHeader = "HTTP/1.1 200 OK\r\n\r\n"
		except:
			htmlData = open("myserver/error.html").read()
			htmlHeader = "HTTP/1.1 404 Not Found\r\n\r\n"

		htmlResponse = htmlHeader + htmlData
		info.send(htmlResponse.encode("UTF-8"))
		info.close()

	# finding password
	elif Method == "POST":
		password = str(httpRequest[-1][0].split('&')[1])
		htmlRes = "<!DOCTYPE html><html><head><title>-_-</title><style></style></head><body><h1>You Are Hacked !</h1><p>We found your <b>"+password+" !</b></p></body></html>"
		info.send(htmlRes.encode("UTF-8"))
		info.close()

	#unsuported Method
	else:
		info.close()