# Python bytecode 2.6 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/SystemMessages.py
# Compiled at: 2011-06-27 20:58:16
from abc import ABCMeta, abstractmethod
from enumerations import Enumeration
SM_TYPE = Enumeration('System message type', ['Error',
 'Warning',
 'Information',
 'GameGreeting',
 'PowerLevel',
 'FinancialTransactionWithGold',
 'FinancialTransactionWithCredits',
 'PurchaseForGold',
 'DismantlingForGold',
 'PurchaseForCredits',
 'Selling',
 'Repair',
 'CustomizationForGold',
 'CustomizationForCredits'])

class BaseSystemMessages(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def destroy(self):
        pass

    @abstractmethod
    def pushMessage(self, text, type=SM_TYPE.Information):
        pass

    @abstractmethod
    def pushI18nMessage(self, key, *args, **kwargs):
        pass


g_instance = None

def pushMessage(text, type=SM_TYPE.Information):
    if g_instance:
        g_instance.pushMessage(text, type)


def pushI18nMessage(key, *args, **kwargs):
    if g_instance:
        g_instance.pushI18nMessage(key, *args, **kwargs)
