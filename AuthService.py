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
from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import logging
from Types import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(object):
    def normalizePhoneNumber(self, countryCode, phoneNumber, countryCodeHint):
        """
        Parameters:
         - countryCode
         - phoneNumber
         - countryCodeHint
        """
        pass

    def respondE2EELoginRequest(self, verifier, publicKey, encryptedKeyChain, hashKeyChain, errorCode):
        """
        Parameters:
         - verifier
         - publicKey
         - encryptedKeyChain
         - hashKeyChain
         - errorCode
        """
        pass

    def confirmE2EELogin(self, verifier, deviceSecret):
        """
        Parameters:
         - verifier
         - deviceSecret
        """
        pass

    def logoutZ(self):
        pass

    def loginZ(self, loginRequest):
        """
        Parameters:
         - loginRequest
        """
        pass

    def issueTokenForAccountMigrationSettings(self, enforce):
        """
        Parameters:
         - enforce
        """
        pass

    def issueTokenForAccountMigration(self, migrationSessionId):
        """
        Parameters:
         - migrationSessionId
        """
        pass

    def verifyQrcodeWithE2EE(self, verifier, pinCode, errorCode, publicKey, encryptedKeyChain, hashKeyChain):
        """
        Parameters:
         - verifier
         - pinCode
         - errorCode
         - publicKey
         - encryptedKeyChain
         - hashKeyChain
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def normalizePhoneNumber(self, countryCode, phoneNumber, countryCodeHint):
        """
        Parameters:
         - countryCode
         - phoneNumber
         - countryCodeHint
        """
        self.send_normalizePhoneNumber(countryCode, phoneNumber, countryCodeHint)
        return self.recv_normalizePhoneNumber()

    def send_normalizePhoneNumber(self, countryCode, phoneNumber, countryCodeHint):
        self._oprot.writeMessageBegin('normalizePhoneNumber', TMessageType.CALL, self._seqid)
        args = normalizePhoneNumber_args()
        args.countryCode = countryCode
        args.phoneNumber = phoneNumber
        args.countryCodeHint = countryCodeHint
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_normalizePhoneNumber(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = normalizePhoneNumber_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "normalizePhoneNumber failed: unknown result")

    def respondE2EELoginRequest(self, verifier, publicKey, encryptedKeyChain, hashKeyChain, errorCode):
        """
        Parameters:
         - verifier
         - publicKey
         - encryptedKeyChain
         - hashKeyChain
         - errorCode
        """
        self.send_respondE2EELoginRequest(verifier, publicKey, encryptedKeyChain, hashKeyChain, errorCode)
        self.recv_respondE2EELoginRequest()

    def send_respondE2EELoginRequest(self, verifier, publicKey, encryptedKeyChain, hashKeyChain, errorCode):
        self._oprot.writeMessageBegin('respondE2EELoginRequest', TMessageType.CALL, self._seqid)
        args = respondE2EELoginRequest_args()
        args.verifier = verifier
        args.publicKey = publicKey
        args.encryptedKeyChain = encryptedKeyChain
        args.hashKeyChain = hashKeyChain
        args.errorCode = errorCode
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_respondE2EELoginRequest(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = respondE2EELoginRequest_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def confirmE2EELogin(self, verifier, deviceSecret):
        """
        Parameters:
         - verifier
         - deviceSecret
        """
        self.send_confirmE2EELogin(verifier, deviceSecret)
        return self.recv_confirmE2EELogin()

    def send_confirmE2EELogin(self, verifier, deviceSecret):
        self._oprot.writeMessageBegin('confirmE2EELogin', TMessageType.CALL, self._seqid)
        args = confirmE2EELogin_args()
        args.verifier = verifier
        args.deviceSecret = deviceSecret
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_confirmE2EELogin(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = confirmE2EELogin_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "confirmE2EELogin failed: unknown result")

    def logoutZ(self):
        self.send_logoutZ()
        self.recv_logoutZ()

    def send_logoutZ(self):
        self._oprot.writeMessageBegin('logoutZ', TMessageType.CALL, self._seqid)
        args = logoutZ_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_logoutZ(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = logoutZ_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.e is not None:
            raise result.e
        return

    def loginZ(self, loginRequest):
        """
        Parameters:
         - loginRequest
        """
        self.send_loginZ(loginRequest)
        return self.recv_loginZ()

    def send_loginZ(self, loginRequest):
        self._oprot.writeMessageBegin('loginZ', TMessageType.CALL, self._seqid)
        args = loginZ_args()
        args.loginRequest = loginRequest
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_loginZ(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = loginZ_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "loginZ failed: unknown result")

    def issueTokenForAccountMigrationSettings(self, enforce):
        """
        Parameters:
         - enforce
        """
        self.send_issueTokenForAccountMigrationSettings(enforce)
        return self.recv_issueTokenForAccountMigrationSettings()

    def send_issueTokenForAccountMigrationSettings(self, enforce):
        self._oprot.writeMessageBegin('issueTokenForAccountMigrationSettings', TMessageType.CALL, self._seqid)
        args = issueTokenForAccountMigrationSettings_args()
        args.enforce = enforce
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueTokenForAccountMigrationSettings(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueTokenForAccountMigrationSettings_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueTokenForAccountMigrationSettings failed: unknown result")

    def issueTokenForAccountMigration(self, migrationSessionId):
        """
        Parameters:
         - migrationSessionId
        """
        self.send_issueTokenForAccountMigration(migrationSessionId)
        return self.recv_issueTokenForAccountMigration()

    def send_issueTokenForAccountMigration(self, migrationSessionId):
        self._oprot.writeMessageBegin('issueTokenForAccountMigration', TMessageType.CALL, self._seqid)
        args = issueTokenForAccountMigration_args()
        args.migrationSessionId = migrationSessionId
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_issueTokenForAccountMigration(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = issueTokenForAccountMigration_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "issueTokenForAccountMigration failed: unknown result")

    def verifyQrcodeWithE2EE(self, verifier, pinCode, errorCode, publicKey, encryptedKeyChain, hashKeyChain):
        """
        Parameters:
         - verifier
         - pinCode
         - errorCode
         - publicKey
         - encryptedKeyChain
         - hashKeyChain
        """
        self.send_verifyQrcodeWithE2EE(verifier, pinCode, errorCode, publicKey, encryptedKeyChain, hashKeyChain)
        return self.recv_verifyQrcodeWithE2EE()

    def send_verifyQrcodeWithE2EE(self, verifier, pinCode, errorCode, publicKey, encryptedKeyChain, hashKeyChain):
        self._oprot.writeMessageBegin('verifyQrcodeWithE2EE', TMessageType.CALL, self._seqid)
        args = verifyQrcodeWithE2EE_args()
        args.verifier = verifier
        args.pinCode = pinCode
        args.errorCode = errorCode
        args.publicKey = publicKey
        args.encryptedKeyChain = encryptedKeyChain
        args.hashKeyChain = hashKeyChain
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_verifyQrcodeWithE2EE(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = verifyQrcodeWithE2EE_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.e is not None:
            raise result.e
        raise TApplicationException(TApplicationException.MISSING_RESULT, "verifyQrcodeWithE2EE failed: unknown result")


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["normalizePhoneNumber"] = Processor.process_normalizePhoneNumber
        self._processMap["respondE2EELoginRequest"] = Processor.process_respondE2EELoginRequest
        self._processMap["confirmE2EELogin"] = Processor.process_confirmE2EELogin
        self._processMap["logoutZ"] = Processor.process_logoutZ
        self._processMap["loginZ"] = Processor.process_loginZ
        self._processMap["issueTokenForAccountMigrationSettings"] = Processor.process_issueTokenForAccountMigrationSettings
        self._processMap["issueTokenForAccountMigration"] = Processor.process_issueTokenForAccountMigration
        self._processMap["verifyQrcodeWithE2EE"] = Processor.process_verifyQrcodeWithE2EE

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_normalizePhoneNumber(self, seqid, iprot, oprot):
        args = normalizePhoneNumber_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = normalizePhoneNumber_result()
        try:
            result.success = self._handler.normalizePhoneNumber(args.countryCode, args.phoneNumber, args.countryCodeHint)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("normalizePhoneNumber", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_respondE2EELoginRequest(self, seqid, iprot, oprot):
        args = respondE2EELoginRequest_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = respondE2EELoginRequest_result()
        try:
            self._handler.respondE2EELoginRequest(args.verifier, args.publicKey, args.encryptedKeyChain, args.hashKeyChain, args.errorCode)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("respondE2EELoginRequest", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_confirmE2EELogin(self, seqid, iprot, oprot):
        args = confirmE2EELogin_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = confirmE2EELogin_result()
        try:
            result.success = self._handler.confirmE2EELogin(args.verifier, args.deviceSecret)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("confirmE2EELogin", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_logoutZ(self, seqid, iprot, oprot):
        args = logoutZ_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = logoutZ_result()
        try:
            self._handler.logoutZ()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("logoutZ", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_loginZ(self, seqid, iprot, oprot):
        args = loginZ_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = loginZ_result()
        try:
            result.success = self._handler.loginZ(args.loginRequest)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("loginZ", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_issueTokenForAccountMigrationSettings(self, seqid, iprot, oprot):
        args = issueTokenForAccountMigrationSettings_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueTokenForAccountMigrationSettings_result()
        try:
            result.success = self._handler.issueTokenForAccountMigrationSettings(args.enforce)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueTokenForAccountMigrationSettings", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_issueTokenForAccountMigration(self, seqid, iprot, oprot):
        args = issueTokenForAccountMigration_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = issueTokenForAccountMigration_result()
        try:
            result.success = self._handler.issueTokenForAccountMigration(args.migrationSessionId)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("issueTokenForAccountMigration", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def process_verifyQrcodeWithE2EE(self, seqid, iprot, oprot):
        args = verifyQrcodeWithE2EE_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = verifyQrcodeWithE2EE_result()
        try:
            result.success = self._handler.verifyQrcodeWithE2EE(args.verifier, args.pinCode, args.errorCode, args.publicKey, args.encryptedKeyChain, args.hashKeyChain)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except TalkException as e:
            msg_type = TMessageType.REPLY
            result.e = e
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("verifyQrcodeWithE2EE", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class normalizePhoneNumber_args(object):
    """
    Attributes:
     - countryCode
     - phoneNumber
     - countryCodeHint
    """


    def __init__(self, countryCode=None, phoneNumber=None, countryCodeHint=None,):
        self.countryCode = countryCode
        self.phoneNumber = phoneNumber
        self.countryCodeHint = countryCodeHint

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.countryCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.phoneNumber = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.countryCodeHint = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('normalizePhoneNumber_args')
        if self.countryCode is not None:
            oprot.writeFieldBegin('countryCode', TType.STRING, 2)
            oprot.writeString(self.countryCode.encode('utf-8') if sys.version_info[0] == 2 else self.countryCode)
            oprot.writeFieldEnd()
        if self.phoneNumber is not None:
            oprot.writeFieldBegin('phoneNumber', TType.STRING, 3)
            oprot.writeString(self.phoneNumber.encode('utf-8') if sys.version_info[0] == 2 else self.phoneNumber)
            oprot.writeFieldEnd()
        if self.countryCodeHint is not None:
            oprot.writeFieldBegin('countryCodeHint', TType.STRING, 4)
            oprot.writeString(self.countryCodeHint.encode('utf-8') if sys.version_info[0] == 2 else self.countryCodeHint)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(normalizePhoneNumber_args)
normalizePhoneNumber_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'countryCode', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'phoneNumber', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'countryCodeHint', 'UTF8', None, ),  # 4
)


class normalizePhoneNumber_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('normalizePhoneNumber_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(normalizePhoneNumber_result)
normalizePhoneNumber_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class respondE2EELoginRequest_args(object):
    """
    Attributes:
     - verifier
     - publicKey
     - encryptedKeyChain
     - hashKeyChain
     - errorCode
    """


    def __init__(self, verifier=None, publicKey=None, encryptedKeyChain=None, hashKeyChain=None, errorCode=None,):
        self.verifier = verifier
        self.publicKey = publicKey
        self.encryptedKeyChain = encryptedKeyChain
        self.hashKeyChain = hashKeyChain
        self.errorCode = errorCode

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.publicKey = E2EEPublicKey()
                    self.publicKey.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.encryptedKeyChain = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.hashKeyChain = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I32:
                    self.errorCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('respondE2EELoginRequest_args')
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 1)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.publicKey is not None:
            oprot.writeFieldBegin('publicKey', TType.STRUCT, 2)
            self.publicKey.write(oprot)
            oprot.writeFieldEnd()
        if self.encryptedKeyChain is not None:
            oprot.writeFieldBegin('encryptedKeyChain', TType.STRING, 3)
            oprot.writeBinary(self.encryptedKeyChain)
            oprot.writeFieldEnd()
        if self.hashKeyChain is not None:
            oprot.writeFieldBegin('hashKeyChain', TType.STRING, 4)
            oprot.writeBinary(self.hashKeyChain)
            oprot.writeFieldEnd()
        if self.errorCode is not None:
            oprot.writeFieldBegin('errorCode', TType.I32, 5)
            oprot.writeI32(self.errorCode)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(respondE2EELoginRequest_args)
respondE2EELoginRequest_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'verifier', 'UTF8', None, ),  # 1
    (2, TType.STRUCT, 'publicKey', [E2EEPublicKey, None], None, ),  # 2
    (3, TType.STRING, 'encryptedKeyChain', 'BINARY', None, ),  # 3
    (4, TType.STRING, 'hashKeyChain', 'BINARY', None, ),  # 4
    (5, TType.I32, 'errorCode', None, None, ),  # 5
)


class respondE2EELoginRequest_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('respondE2EELoginRequest_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(respondE2EELoginRequest_result)
respondE2EELoginRequest_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class confirmE2EELogin_args(object):
    """
    Attributes:
     - verifier
     - deviceSecret
    """


    def __init__(self, verifier=None, deviceSecret=None,):
        self.verifier = verifier
        self.deviceSecret = deviceSecret

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.deviceSecret = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('confirmE2EELogin_args')
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 1)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.deviceSecret is not None:
            oprot.writeFieldBegin('deviceSecret', TType.STRING, 2)
            oprot.writeBinary(self.deviceSecret)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(confirmE2EELogin_args)
confirmE2EELogin_args.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'verifier', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'deviceSecret', 'BINARY', None, ),  # 2
)


class confirmE2EELogin_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('confirmE2EELogin_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(confirmE2EELogin_result)
confirmE2EELogin_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class logoutZ_args(object):


    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('logoutZ_args')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(logoutZ_args)
logoutZ_args.thrift_spec = (
)


class logoutZ_result(object):
    """
    Attributes:
     - e
    """


    def __init__(self, e=None,):
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('logoutZ_result')
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(logoutZ_result)
logoutZ_result.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class loginZ_args(object):
    """
    Attributes:
     - loginRequest
    """


    def __init__(self, loginRequest=None,):
        self.loginRequest = loginRequest

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRUCT:
                    self.loginRequest = LoginRequest()
                    self.loginRequest.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('loginZ_args')
        if self.loginRequest is not None:
            oprot.writeFieldBegin('loginRequest', TType.STRUCT, 2)
            self.loginRequest.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(loginZ_args)
loginZ_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRUCT, 'loginRequest', [LoginRequest, None], None, ),  # 2
)


class loginZ_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = LoginResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('loginZ_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(loginZ_result)
loginZ_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [LoginResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class issueTokenForAccountMigrationSettings_args(object):
    """
    Attributes:
     - enforce
    """


    def __init__(self, enforce=None,):
        self.enforce = enforce

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.BOOL:
                    self.enforce = iprot.readBool()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueTokenForAccountMigrationSettings_args')
        if self.enforce is not None:
            oprot.writeFieldBegin('enforce', TType.BOOL, 2)
            oprot.writeBool(self.enforce)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueTokenForAccountMigrationSettings_args)
issueTokenForAccountMigrationSettings_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.BOOL, 'enforce', None, None, ),  # 2
)


class issueTokenForAccountMigrationSettings_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SecurityCenterResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueTokenForAccountMigrationSettings_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueTokenForAccountMigrationSettings_result)
issueTokenForAccountMigrationSettings_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SecurityCenterResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class issueTokenForAccountMigration_args(object):
    """
    Attributes:
     - migrationSessionId
    """


    def __init__(self, migrationSessionId=None,):
        self.migrationSessionId = migrationSessionId

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.migrationSessionId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueTokenForAccountMigration_args')
        if self.migrationSessionId is not None:
            oprot.writeFieldBegin('migrationSessionId', TType.STRING, 2)
            oprot.writeString(self.migrationSessionId.encode('utf-8') if sys.version_info[0] == 2 else self.migrationSessionId)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueTokenForAccountMigration_args)
issueTokenForAccountMigration_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'migrationSessionId', 'UTF8', None, ),  # 2
)


class issueTokenForAccountMigration_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = SecurityCenterResult()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('issueTokenForAccountMigration_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(issueTokenForAccountMigration_result)
issueTokenForAccountMigration_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [SecurityCenterResult, None], None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)


class verifyQrcodeWithE2EE_args(object):
    """
    Attributes:
     - verifier
     - pinCode
     - errorCode
     - publicKey
     - encryptedKeyChain
     - hashKeyChain
    """


    def __init__(self, verifier=None, pinCode=None, errorCode=None, publicKey=None, encryptedKeyChain=None, hashKeyChain=None,):
        self.verifier = verifier
        self.pinCode = pinCode
        self.errorCode = errorCode
        self.publicKey = publicKey
        self.encryptedKeyChain = encryptedKeyChain
        self.hashKeyChain = hashKeyChain

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 2:
                if ftype == TType.STRING:
                    self.verifier = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.pinCode = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.errorCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRUCT:
                    self.publicKey = E2EEPublicKey()
                    self.publicKey.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.encryptedKeyChain = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.hashKeyChain = iprot.readBinary()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('verifyQrcodeWithE2EE_args')
        if self.verifier is not None:
            oprot.writeFieldBegin('verifier', TType.STRING, 2)
            oprot.writeString(self.verifier.encode('utf-8') if sys.version_info[0] == 2 else self.verifier)
            oprot.writeFieldEnd()
        if self.pinCode is not None:
            oprot.writeFieldBegin('pinCode', TType.STRING, 3)
            oprot.writeString(self.pinCode.encode('utf-8') if sys.version_info[0] == 2 else self.pinCode)
            oprot.writeFieldEnd()
        if self.errorCode is not None:
            oprot.writeFieldBegin('errorCode', TType.I32, 4)
            oprot.writeI32(self.errorCode)
            oprot.writeFieldEnd()
        if self.publicKey is not None:
            oprot.writeFieldBegin('publicKey', TType.STRUCT, 5)
            self.publicKey.write(oprot)
            oprot.writeFieldEnd()
        if self.encryptedKeyChain is not None:
            oprot.writeFieldBegin('encryptedKeyChain', TType.STRING, 6)
            oprot.writeBinary(self.encryptedKeyChain)
            oprot.writeFieldEnd()
        if self.hashKeyChain is not None:
            oprot.writeFieldBegin('hashKeyChain', TType.STRING, 7)
            oprot.writeBinary(self.hashKeyChain)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(verifyQrcodeWithE2EE_args)
verifyQrcodeWithE2EE_args.thrift_spec = (
    None,  # 0
    None,  # 1
    (2, TType.STRING, 'verifier', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'pinCode', 'UTF8', None, ),  # 3
    (4, TType.I32, 'errorCode', None, None, ),  # 4
    (5, TType.STRUCT, 'publicKey', [E2EEPublicKey, None], None, ),  # 5
    (6, TType.STRING, 'encryptedKeyChain', 'BINARY', None, ),  # 6
    (7, TType.STRING, 'hashKeyChain', 'BINARY', None, ),  # 7
)


class verifyQrcodeWithE2EE_result(object):
    """
    Attributes:
     - success
     - e
    """


    def __init__(self, success=None, e=None,):
        self.success = success
        self.e = e

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRING:
                    self.success = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.e = TalkException()
                    self.e.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('verifyQrcodeWithE2EE_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRING, 0)
            oprot.writeString(self.success.encode('utf-8') if sys.version_info[0] == 2 else self.success)
            oprot.writeFieldEnd()
        if self.e is not None:
            oprot.writeFieldBegin('e', TType.STRUCT, 1)
            self.e.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(verifyQrcodeWithE2EE_result)
verifyQrcodeWithE2EE_result.thrift_spec = (
    (0, TType.STRING, 'success', 'UTF8', None, ),  # 0
    (1, TType.STRUCT, 'e', [TalkException, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
