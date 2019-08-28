import socket
import json
import sys

HOST = 'demo.jiguem.com'
PORT = 5040

def log_input(msg):
  try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  except socket.error as msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)

  try:
    sock.connect((HOST, PORT))
  except socket.error as msg:
    sock.connect((HOST, PORT))
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(2)

  sock.send(str(json.dumps(msg) ).encode('utf-8'))
  #
  # sock.close()
  # sys.exit(0)

# msg = {'@message': 'python test message', '@tags': ['python', 'test']}
# msg = {'attributes': {'friendly_name': 'Fibaro Temperature'},
#  'context': {'id': 'b7d3f5dbf81d406583545ecad2937337', 'user_id': None},
#  'device_type': 'sensor.fibaro_temperature',
#  'dt': '2019-04-01 17:27:54',
#  'entity_id': 'sensor.fibaro_temperature',
#  'last_changed': '2019-04-01T00:45:22.320564+00:00',
#  'last_updated': '2019-04-01T00:45:22.320564+00:00',
#  'state': '79.3',
#  'topic': '406/503'}