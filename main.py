# -*- coding: utf-8 -*-
#======================================
#This library is protected by license.
#Please check LINCENSE for details.
#@file:linemf/main.py
#@author=mafusuke
#@copyright=Copyright 2018 by mafusuke
#@license=BSD-3-Clause
#@version=1.0.0
#======================================
import traceback
from Login import Login
#=====================
#Login
mf=Login("1")
#1:url,2:mail,3:token
#=====================
#run
while True:
    try:
        ops=cl.poll.fetchOperations(cl.revision,50)
    except:
        continue
    if ops!=None:
        for op in ops:
            try:
                if op.type==0:
                    pass
            except KeyboardInterrupt:
                print("[exit]:KeyboardInterrupt")
            else:
                e=traceback.format_exc()
                print(str(e))
            finally:
                mf.revision=max(op.revision,mf.revision)
