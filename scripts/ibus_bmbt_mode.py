import time
from ibusutil import *

sendRawHex('f004684823')
time.sleep(0.1)
sendRawHex('f0046848a3')
