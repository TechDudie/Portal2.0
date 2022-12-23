import socket
HOSTA = "chat.freenode.net"
HOSTB = "us.xeroxirc.net"
PORT = 6667
NICK = "Nothingness"
CHANNELA = "##techdudeserver"
CHANNELB = "#techdudeserver"
SERVERA = ""
SERVERB = ""
readbuffera = ""
readbufferb = ""
sa = socket.socket()
sa.connect((HOSTA, PORT))
sa.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
sa.send(bytes("USER %s %s %s :%s\r\n" % (NICK, NICK, NICK, NICK), "UTF-8"))
sa.send(bytes("JOIN {}\r\n".format(CHANNELA), "UTF-8"))
readbuffera = readbuffera + sa.recv(1024).decode("UTF-8")
temp = str.split(readbuffera, "\n")
readbuffera = temp.pop()
for line in temp:
  SERVERA = str.rstrip(line)[1:].split()[0]
  print(str.rstrip(line))
sb = socket.socket()
sb.connect((HOSTB, PORT))
sb.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
sb.send(bytes("USER %s %s %s :%s\r\n" % (NICK, NICK, NICK, NICK), "UTF-8"))
sb.send(bytes("JOIN {}\r\n".format(CHANNELB), "UTF-8"))
readbuffera = readbuffera + sb.recv(1024).decode("UTF-8")
temp = str.split(readbuffera, "\n")
readbuffera = temp.pop()
for line in temp:
  SERVERB = str.rstrip(line)[1:].split()[0]
  print(str.rstrip(line))
while 1:
  readbuffera = readbuffera + sa.recv(1024).decode("UTF-8")
  temp = str.split(readbuffera, "\n")
  readbuffera = temp.pop()
  for line in temp:
    #print(str.rstrip(line))
    message = str.rstrip(line).split(" PRIVMSG {} :".format(CHANNELA))
    if "PING" in line:
      sa.send("PONG :{}\r\n".format(SERVERA).encode("utf-8"))
    msg = message[-1]
    print(msg)
    continue
    if msg.find(".net") != 0 - 1:
      try:
        sb.send("PRIVMSG {} :{}\r\n".format(CHANNELB,msg).encode("utf-8"))
      except:
        pass
      #print("hello")
  continue
  readbufferb = readbufferb + sb.recv(1024).decode("UTF-8")
  temp = str.split(readbufferb, "\n")
  readbufferb = temp.pop()
  for line in temp:
    #print(str.rstrip(line))
    message = str.rstrip(line).split(" PRIVMSG {} :".format(CHANNELB))
    if "PING" in line:
      sb.send("PONG :{}\r\n".format(SERVERB).encode("utf-8"))
    msg = message[-1]
    #print(msg)
    if msg:
      try:
        sa.send("PRIVMSG {} :{}\r\n".format(CHANNELA,msg).encode("utf-8"))
      except:
        pass
      #print("world")