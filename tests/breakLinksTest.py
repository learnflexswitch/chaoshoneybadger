#!/usr/bin/python
import sys 
import os
import unittest 
import logging
import time
import random
from ciscoNwConfig import configInfo
from ciscoDevice import CiscoSwitch

logging.basicConfig(stream=sys.stderr)
log = logging.getLogger("Break Links:")
log.setLevel(logging.DEBUG)

class BreakLinksTest(unittest.TestCase):
    def setUp(self):
        self.nw = {}
        self.passwd = os.getenv('DEV_PASSWD', None)
        for name, dtls in configInfo.iteritems():
            self.nw [name] = CiscoSwitch ( dtls['switchip'], dtls['switchUsr'], self.passwd)
            self.nw [name].connect()

    def testBreakLinks(self):
        totalBreakCount = 100
        devices = self.nw.items()
        while  totalBreakCount > 0:
            randNum  = random.randrange(0,len(devices))
            randTime = random.randrange(1, 10)
            (name, device) = (devices[randNum][0], devices[randNum][1])
            log.debug( 'Sleeping for %s seconds before breaking %s links' %(randTime, name))
            time.sleep(randTime)
            device.sendCommandInteractive('conf t\n', '(config)#', True)
            device.sendCommandInteractive('interface Eth1/25\n', '(config-if)#', True)
            device.sendCommandInteractive('shut\n','(config-if)#', True)
            time.sleep(10) 
            device.sendCommandInteractive('no shut\n','(config-if)#', True)

        print 'Break Links'

if __name__ =='__main__':
    unittest.main()
