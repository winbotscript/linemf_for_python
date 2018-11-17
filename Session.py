# -*- coding: utf-8 -*-
#======================================
#This library is protected by license.
#Please check LINCENSE for details.
#@file:linemf/Login.py
#@author=mafusuke
#@copyright=Copyright 2018 by mafusuke
#@license=BSD-3-Clause
#@version=1.0.0
#======================================
#                 ╭╶╶╶╶╶╮
#                 │  ╭╶╶╯
#  ╭╶╮╭╶╮╭╶╮ ╭╶╶╶╶╯  ╰╶╶╶╶╶╮
#  ╷ ╭╮ ╭╮ ╷ ╷ ╭╶╶╮  ╭╶╶╶╶╶╯
#  │_││_││_╰╶╯_╯  │  │
#                 │  │
#               ╭╶╯  │
#               ╰╶╶╶╶╯
#======================================
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
import AuthService,TalkService
class Session:
    def __init__(self, url, headers, path=''):
        self.host = url + path
        self.headers = headers
    def Auth(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._auth  = AuthService.Client(self.protocol)
        if isopen:self.transport.open()
        return self._auth
    def Talk(self, isopen=True):
        self.transport = THttpClient.THttpClient(self.host)
        self.transport.setCustomHeaders(self.headers)
        self.protocol = TCompactProtocol.TCompactProtocol(self.transport)
        self._talk  = TalkService.Client(self.protocol)
        if isopen:self.transport.open()
        return self._talk
