import xbmcgui
import time
import os
import socket

from ibusutil import *

xbmcgui.Dialog().notification('BMW', 'Sending wake DSP message', xbmcgui.NOTIFICATION_INFO, 2000)
sendRawHex('f0036801')
