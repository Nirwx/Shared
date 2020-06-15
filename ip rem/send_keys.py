# usage: python send_IP_keys.py Command_To_Send
import socket
import sys
from urllib2 import Request, urlopen
import json
import time
import logging
import os
from key_dict import keys

logging_done = False



key_dict = {
    #Placeholder
    
}

def send_one_key(s, key) :

    kc = key_dict.get(key)
    if kc is None :
      return False

    logging.debug("Sending keyCode: %s", kc.encode('hex'))
    
    mt = '\x04'
    kd = '\x01'
    ku = '\x00'
    p = '\x00\x00\x00\x00'
    code = True
    try :
      s.send( mt + kd + p + kc)
      s.send( mt + ku + p + kc)
    except: 
      code = False
    return code

def init_connect(host) :

   try :
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.connect((host, 5900))
       answer = s.recv(12)
       logging.debug("Version: %s", answer)
       s.send(answer)
       answer = s.recv(8)
       logging.debug("Security scheme: %s", answer.encode('hex'))
       s.send('\x01')
       answer = s.recv(4)
       logging.debug("Security result: %s", answer.encode('hex'))
       s.send('\x01')
       answer = s.recv(24)
       logging.debug(answer.encode('hex'))
       return s

   except :
       logging.exception("Error to init_connect")
       return None

def end_connect(s) :
    try: 
        close(s)
    except:
        pass
    return None
 
x = 1 
stbip = ''

if len(sys.argv) > 1:
	key = sys.argv[1]
	s = init_connect(stbip)
	send_one_key(s, key)
	end_connect(s)
else:
	while x:
		s = init_connect(stbip)
		key = raw_input("> ")
		if key == 'exit':
			end_connect(s)
			x=0
		send_one_key(s, key)
		end_connect(s)
