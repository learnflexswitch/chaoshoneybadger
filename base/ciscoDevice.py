#!/usr/bin/python
import unittest
import paramiko
import time 
import sys 
import logging

logging.basicConfig( stream=sys.stderr )
log = logging.getLogger( " Monkey.TestCisco" )                                                              
log.setLevel( logging.DEBUG )

class CiscoSwitch(object):
    """Test case testing link failures while BGP is running"""

    def __init__ (self, ip, username, passwd):
        self.ip = ip
        self.username = username
        self.passwd = passwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.shell = None

    def connect (self) :
        self.ssh.connect(self.ip, username=self.username, password=self.passwd)
        self.shell = self.ssh.invoke_shell()
        self.sendCommandInteractive("", "#", False)
        self.sendCommandInteractive("terminal length 0\n", "#", False)
 
    def executeCommand(self, cmd):
        """Execute command """
        inpt, outpt, err = self.ssh.exec_command('show interface brief') 
        inpt, outpt, err = self.ssh.exec_command(cmd)
        for line in outpt.readlines():
            print line

    def sendCommandInteractive(self, command, wait_string, should_print):
        # Send the su command
        self.shell.send(command)
        # Create a new receive buffer
        receive_buffer = ""
        while not wait_string in receive_buffer:
            # Flush the receive buffer
            receive_buffer += self.shell.recv(1024)
        # Print the receive buffer, if necessary
        if should_print:
            print receive_buffer
        return receive_buffer
