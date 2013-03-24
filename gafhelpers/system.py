# -*- coding: utf-8 -*- 
'''
Created on 23 mars 2013

@author: gabriel
'''
import os
import grp
import pwd

def is_root():
    return os.getuid() is 0

def chgrp(filename, groupname):
    gid = grp.getgrnam(groupname)[2]
    os.chown(filename, -1, gid)
    
def chown(filename, username):
    uid = pwd.getpwnam(username)[2]
    os.chown(filename, uid, -1)
    
def chmod(filename, mode):
    if isinstance(mode, basestring):
        mode = int(mode, 8)
    os.chmod(filename, mode)