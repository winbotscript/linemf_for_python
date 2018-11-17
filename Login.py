# -*- coding: utf-8 -*-
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
import json,re,requests,rsa
from Session import *
from Types import LoginRequest
class Login(object):
    #setting
    #==Auth==#
    isLogin=False#Auth[bool]
    authToken=""#Auth[string]
    certificate=""#Auth[string]
    #==Config==#
    LINE_HOST_DOMAIN="https://gd2.line.naver.jp"#Config[string]
    #LINE_OBS_DOMAIN="https://obs-sg.line-apps.com"#Config[string]
    #LINE_TIMELINE_API="https://gd2.line.naver.jp/mh/api"#Config[string]
    #LINE_TIMELINE_MH="https://gd2.line.naver.jp/mh"#Config[string]
    LINE_LOGIN_QUERY_PATH="/api/v4p/rs"#Config[string]
    LINE_AUTH_QUERY_PATH="/api/v4/TalkService.do"#Config[string]
    LINE_API_QUERY_PATH_FIR="/S4"#Config[string]
    LINE_POLL_QUERY_PATH_FIR="/P4"#Config[string]
    #LINE_CALL_QUERY_PATH="/V4"#Config[string]
    LINE_CERTIFICATE_PATH="/Q"#Config[string]
    #LINE_CHAN_QUERY_PATH="/CH4"#Config[string]
    #LINE_SQUARE_QUERY_PATH="/SQS1"#Config[string]
    #LINE_SHOP_QUERY_PATH="/SHOP4"#Config[string]
    APP_TYPE="IOSIPAD"#Config[string]
    APP_VER="8.9.1"#Config[string]
    CARRIER="51089, 1-0"#Config[string]
    SYSTEM_NAME="_mafusuke_"#Config[string]
    SYSTEM_VER="12.1.1"#Config[string]
    IP_ADDR="8.8.8.8"#Config[string]
    EMAIL_REGEX=re.compile(r"[^@]+@[^@]+\.[^@]+")#Config[re-match]
    #USER_AGENT="Line/%s"%(APP_VER)#Config[string]
    #APP_NAME="%s\t%s\t%s\t%s"%(APP_TYPE,APP_VER,SYSTEM_NAME,SYSTEM_VER)#Config[string]
    #==Server==#
    getSession=requests.session()#Server[requests-session]
    Headers={}#Server[dict]
    channelHeaders={}#Server[dict]
    timelineHeaders={}#Server[dict]
    #method
    def __init__(self,lt,iot=None,pswd=None,cert=None,sn=None,an=None,kl=None):
        self.USER_AGENT="Line/%s"%(self.APP_VER)
        self.APP_NAME="%s\t%s\t%s\t%s"%(self.APP_TYPE,self.APP_VER,self.SYSTEM_NAME,self.SYSTEM_VER)
        self.Headers["User-Agent"]=self.USER_AGENT
        self.Headers["X-Line-Application"]=self.APP_NAME
        self.Headers["X-Line-Carrier"]=self.CARRIER
        if lt=="1" or lt=="url":self.loginWithQrCode(keepLoggedIn=kl,systemName=sn,appName=an)
        elif lt=="2" or lt=="mail":self.loginWithCredential(_id=iot,passwd=pswd,certificate=cert,systemName=sn,appName=an,keepLoggedIn=kl)
        elif lt=="3" or lt=="token":self.loginWithAuthToken(authToken=iot,appName=an)
        else:raise Exception("mistaken login type")
        if self.isLogin==True:print("LoginSuccess[%s]\n[%s]"%(self.talk.getProfile().displayName,self.talk.getProfile().mid))
    def __loginRequest(self,type,data):
        lr=LoginRequest()
        if type=="0":
            lr.type=0#LoginType.ID_CREDENTIAL=0
            lr.identityProvider=data["identityProvider"]
            lr.identifier=data["identifier"]
            lr.password=data["password"]
            lr.keepLoggedIn=data["keepLoggedIn"]
            lr.accessLocation=data["accessLocation"]
            lr.systemName=data["systemName"]
            lr.certificate=data["certificate"]
            lr.e2eeVersion=data["e2eeVersion"]
        elif type=="1":
            lr.type=1#LoginType.QRCODE=1
            lr.keepLoggedIn=data["keepLoggedIn"]
            if "identityProvider" in data:lr.identityProvider=data["identityProvider"]
            if "accessLocation" in data:lr.accessLocation=data["accessLocation"]
            if "systemName" in data:lr.systemName=data["systemName"]
            lr.verifier=data["verifier"]
            lr.e2eeVersion=data["e2eeVersion"]
        else:lr=False
        return lr
    def loginWithQrCode(self,keepLoggedIn=True,systemName=None,appName=False):
        if systemName==None:systemName=self.SYSTEM_NAME
        if appName==None:appName=self.APP_NAME
        self.Headers["X-Line-Access"]=appName
        self.tauth=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_AUTH_QUERY_PATH).Talk(isopen=False)
        qrCode=self.tauth.getAuthQrcode(keepLoggedIn,systemName)
        print("Please login by this url.\nline://au/q/"+qrCode.verifier)
        self.Headers["X-Line-Access"]=qrCode.verifier
        getAccessKey=json.loads(self.getSession.get(self.LINE_HOST_DOMAIN+self.LINE_CERTIFICATE_PATH,headers=self.Headers).text)
        self.auth=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)
        try:
            lr=self.__loginRequest("1",{"keepLoggedIn":keepLoggedIn,"systemName":systemName,"identityProvider":1,"verifier":getAccessKey["result"]["verifier"],"accessLocation":self.IP_ADDR,"e2eeVersion":0})
            result=self.auth.loginZ(lr)
        except:raise Exception("error")
        if result.type==1:#LoginResultType=1
            if result.authToken!=None:self.loginWithAuthToken(result.authToken,appName)
            else:return False
        else:raise Exception("error")
    def loginWithCredential(self,_id,passwd,certificate=None,systemName=None,appName=None,keepLoggedIn=True):
        if systemName==None:systemName=self.SYSTEM_NAME
        if self.EMAIL_REGEX.match(_id):self.provider=1#IdentityProvider.LINE=1
        else:self.provider=2#IdentityProvider.NAVER_KR=2
        if appName==None:appName=self.APP_NAME
        self.Headers["X-Line-Application"]=appName
        self.tauth=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_AUTH_QUERY_PATH).Talk(isopen=False)
        rsaKey=self.tauth.getRSAKeyInfo(self.provider)
        message=(chr(len(rsaKey.sessionKey))+rsaKey.sessionKey+chr(len(_id))+_id+chr(len(passwd))+passwd).encode("utf-8")
        pub_key=rsa.PublicKey(int(rsaKey.nvalue,16),int(rsaKey.evalue,16))
        crypto=rsa.encrypt(message,pub_key).hex()
        try:
            with open(_id+".crt","r") as f:
                self.certificate=f.read()
        except:
            if certificate!=None:
                self.certificate=certificate
                if os.path.exists(certificate):
                    with open(certificate,"r") as f:
                        self.certificate=f.read()
        self.auth=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)
        lr=self.__loginRequest("0",{"identityProvider":self.provider,"identifier":rsaKey.keynm,"password":crypto,"keepLoggedIn":keepLoggedIn,"accessLocation":self.IP_ADDR,"systemName":systemName,"certificate":self.certificate,"e2eeVersion":0})
        result=self.auth.loginZ(lr)
        if result.type==3:#LoginRequestType.REQUIRE_DEVICE_CONFIRM=3
            print("Please input this pincode.\n"+result.pinCode)
            self.Headers["X-Line-Access"]=result.verifier
            getAccessKey=json.loads(self.getSession.get(self.LINE_HOST_DOMAIN+self.LINE_CERTIFICATE_PATH,headers=self.Headers).text)
            self.auth=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)
            try:
                lr=self.__loginRequest("1",{"keepLoggedIn":keepLoggedIn,"verifier":getAccessKey["result"]["verifier"],"e2eeVersion":0})
                result=self.auth.loginZ(lr)
            except:raise Exception("error")
            if result.type==1:#LoginResultType.SUCCESS==1
                if result.certificate!=None:
                    with open(_id+".crt","w") as f:
                        f.write(result.certificate)
                    self.certificate=result.certificate
                if result.authToken!=None:self.loginWithAuthToken(result.authToken,appName)
                else:return False
        elif result.type==2:#LoginRequestType.REQUIRE_QRCODE=2
            self.loginWithQrCode(keepLoggedIn,systemName,appName)
            pass
        elif result.type==1:#LoginRequestType.SUCCESS=1
            self.certificate=result.certificate
            self.loginWithAuthToken(result.authToken,appName)
    def loginWithAuthToken(self,authToken=None,appName=None):
        if authToken==None:raise Exception("Please set authToken")
        if appName==None:appName=self.APP_NAME
        self.Headers["X-Line-Application"]=appName
        self.Headers["X-Line-access"]=authToken
        self.authToken=authToken
        self.talk=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_API_QUERY_PATH_FIR).Talk()
        self.poll=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_POLL_QUERY_PATH_FIR).Talk()
        #self.call=Sesion(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_CALL_QUERY_PATH).Call()
        #self.channel=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_CHAN_QUERY_PATH).Channel()
        #self.square=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_SQUARE_QUERY_PATH).Square()
        #self.shop=Session(self.LINE_HOST_DOMAIN,self.Headers,self.LINE_SHOP_QUERY_PATH).Shop()
        self.isLogin=True
