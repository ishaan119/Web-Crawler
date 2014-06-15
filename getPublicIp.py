'''
Created on Sep 8, 2013

@author: ishaansutaria
'''
import os
cmd = 'curl ipecho.net/plain'
pubIp = os.system(cmd)
print pubIp