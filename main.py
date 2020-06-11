from playsound import playsound
import logging
import time
import threading

# playsound('start.wav')

import io, sys

def play_log():
	playsound('end.wav')

# sound_thread = threading.Thread( target = play_log )
# sound_thread.start()

class StdoutCatcher(io.TextIOBase):
	def __init__(self):
		pass

	def write(self, message):
		# sys.stderr.write( str(sound_thread.is_alive()) )

		# if sound_thread.is_alive():
		# 	sound_thread.join()

		sys.stderr.write( message )
		# sound_thread.run()
		play_log()

class Error(Exception):
	pass

import sys
sys.stdout = StdoutCatcher()

for i in range(10):
	print('foo')
	time.sleep(0.5)
	print('hello world!')

# time.sleep(2)
handler = Handler()

# sys.stderr.write(''.join(sys.stdout.data))

# import io, sys

# class StdoutCatcher( io.TextIOBase ):

# 	def __init__(self):
# 		pass

# 	def write(self,stuff):
# 		sys.stderr.write("extra stuff")	
# 		sys.stderr.write(sys.stdout.getvalue())	

# sys.stdout = io.StringIO()
# print('foo')
# time.sleep(5)
# print('hello world!')
# sys.stderr.write(sys.stdout.getvalue())

# class Handler(logging.Handler):

# 	def __init__(self):
# 		super(Handler, self ).__init__()
	
# 	def handle(self,record):
# 		playsound('end.wav')
# 		print("Wasssup")

# handler = Handler()

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
# logger.addHandler( handler )
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

# for i in range(2000):
# 	time.sleep(0.001)
# 	if i==200:
# 		raise error





















