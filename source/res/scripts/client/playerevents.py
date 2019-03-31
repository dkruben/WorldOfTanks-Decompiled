# Python bytecode 2.6 (decompiled from Python 2.7)
# Embedded file name: scripts/client/PlayerEvents.py
# Compiled at: 2011-11-21 20:52:13
import Event
from constants import ARENA_PERIOD
from debug_utils import *

class DeprecatedEvent(Event.Event):

    def __iadd__(self, delegate):
        LOG_WARNING('Event deprecated')
        self._Event__delegates.add(delegate)
        return self


class _PlayerEvents(object):

    def __init__(self):
        self.onPlayerEntityChanging = Event.Event()
        self.onPlayerEntityChangeCanceled = Event.Event()
        self.isPlayerEntityChanging = True
        self.onAccountBecomePlayer = Event.Event()
        self.onAccountBecomeNonPlayer = Event.Event()
        self.onAccountShowGUI = Event.Event()
        self.onClientUpdated = Event.Event()
        self.onEnqueued = Event.Event()
        self.onDequeued = Event.Event()
        self.onEnqueueFailure = Event.Event()
        self.onPrebattleJoined = Event.Event()
        self.onPrebattleLeft = Event.Event()
        self.onPrebattleJoinFailure = Event.Event()
        self.onArenaCreated = Event.Event()
        self.onArenaJoinFailure = Event.Event()
        self.onKickedFromQueue = Event.Event()
        self.onKickedFromPrebattle = Event.Event()
        self.onKickedFromArena = Event.Event()
        self.onQueueInfoReceived = Event.Event()
        self.onPrebattlesListReceived = Event.Event()
        self.onPrebattleAutoInvitesChanged = Event.Event()
        self.onPrebattleInvitesChanged = Event.Event()
        self.onClanMembersListChanged = Event.Event()
        self.onPrebattleRosterReceived = Event.Event()
        self.onArenaListReceived = Event.Event()
        self.onServerStatsReceived = Event.Event()
        self.onInventoryResync = Event.Event()
        self.onStatsResync = Event.Event()
        self.onShopResyncStarted = Event.Event()
        self.onShopResync = Event.Event()
        self.onDossiersResync = Event.Event()
        self.onOffersResync = Event.Event()
        self.onVehicleLockChanged = Event.Event()
        self.onVehicleBecomeElite = Event.Event()
        self.onCenterIsLongDisconnected = Event.Event()
        self.onAvatarBecomePlayer = Event.Event()
        self.onAvatarBecomeNonPlayer = Event.Event()
        self.onArenaPeriodChange = Event.Event()
        self.onAvatarReady = Event.Event()
        self.onBattleResultsReceived = Event.Event()
        self.onLoginQueueNumberReceived = Event.Event()
        self.onKickWhileLoginReceived = Event.Event()


g_playerEvents = _PlayerEvents()
