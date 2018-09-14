# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/miniclient/dynamic_squads.py
from gui import GUI_SETTINGS
from account_helpers.settings_core.settings_constants import GAME
from helpers import aop
if not GUI_SETTINGS.useAS3Battle:

    class _ParametrizeInitAspect(aop.Aspect):

        def atCall(self, cd):
            cd.avoid()
            return [False, False, False]


    class ParametrizeInitPointcut(aop.Pointcut):

        def __init__(self):
            aop.Pointcut.__init__(self, 'gui.Scaleform.Battle', 'Battle', '_Battle__getDynamicSquadsInitParams', aspects=(_ParametrizeInitAspect,))


else:

    class _ParametrizeInitAspect(aop.Aspect):

        def atCall(self, cd):
            cd.avoid()
            return False


    class ParametrizeInitPointcut(aop.Pointcut):

        def __init__(self):
            aop.Pointcut.__init__(self, 'gui.battle_control.battle_ctx', 'BattleContext', 'isInvitationEnabled', aspects=(_ParametrizeInitAspect,))


class _DisableGameSettingAspect(aop.Aspect):

    def atCall(self, cd):
        if cd.self.settingName == GAME.RECEIVE_INVITES_IN_BATTLE:
            cd.avoid()
        return None


class DisableGameSettingPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'account_helpers.settings_core.options', 'MessengerSetting', '_get', aspects=(_DisableGameSettingAspect,))


class InviteReceivedMessagePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, 'gui.battle_control.controllers.dyn_squad_functional', 'DynSquadMessagesController', '_inviteReceived', aspects=(aop.DummyAspect,))