# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_page.py
from account_helpers import AccountSettings
from account_helpers.AccountSettings import GUI_START_BEHAVIOR, RANKED_AWARDS_COUNTER, RANKED_INFO_COUNTER, RANKED_AWARDS_BUBBLE_YEAR_REACHED
from gui.ranked_battles.ranked_helpers.sound_manager import RANKED_MAIN_PAGE_SOUND_SPACE
from gui.ranked_battles.constants import RankedDossierKeys
from gui.ranked_battles.ranked_builders import main_page_vos
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.RankedBattlesPageMeta import RankedBattlesPageMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.utils.scheduled_notifications import PeriodicNotifier
from helpers import time_utils, dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.game_control import IRankedBattlesController
from skeletons.gui.shared import IItemsCache
_RANKED_BATTLES_VIEW_TO_ITEM_ID = {RANKEDBATTLES_ALIASES.RANKED_BATTLES_LEAGUES_VIEW_UI: RANKEDBATTLES_CONSTS.RANKED_BATTLES_RANKS_ID,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_DIVISIONS_VIEW_UI: RANKEDBATTLES_CONSTS.RANKED_BATTLES_RANKS_ID,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_SEASON_GAP_VIEW_UI: RANKEDBATTLES_CONSTS.RANKED_BATTLES_RANKS_ID,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_UI: RANKEDBATTLES_CONSTS.RANKED_BATTLES_REWARDS_ID,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_SEASON_OFF_ALIAS: RANKEDBATTLES_CONSTS.RANKED_BATTLES_REWARDS_ID,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_RAITING_ALIAS: RANKEDBATTLES_CONSTS.RANKED_BATTLES_RATING_ID,
 RANKEDBATTLES_ALIASES.RANKED_BATTLES_INFO_ALIAS: RANKEDBATTLES_CONSTS.RANKED_BATTLES_INFO_ID}

class IResetablePage(object):

    def reset(self):
        raise NotImplementedError


class RankedMainPage(LobbySubView, RankedBattlesPageMeta):
    _rankedController = dependency.descriptor(IRankedBattlesController)
    _settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, ctx):
        super(RankedMainPage, self).__init__(ctx)
        self._selectedItemID = RANKEDBATTLES_CONSTS.RANKED_BATTLES_RANKS_ID
        self._processContext(ctx)

    def onClose(self):
        self.fireEvent(events.LoadViewEvent(VIEW_ALIAS.LOBBY_HANGAR), scope=EVENT_BUS_SCOPE.LOBBY)

    def onPageChanged(self, viewId):
        newSelectedID = _RANKED_BATTLES_VIEW_TO_ITEM_ID.get(viewId, self._selectedItemID)
        if self._selectedItemID != newSelectedID:
            self._selectedItemID = newSelectedID
            self._updateSounds()
            viewComponent = self.getComponent(viewId)
            if viewComponent is not None:
                viewComponent.reset()
            self._update()
            self.__resetCounters(newSelectedID)
        return

    def _dispose(self):
        self._rankedController.onUpdated -= self._update
        self._rankedController.onYearPointsChanges -= self.__onYearAwardPointsUpdate
        super(RankedMainPage, self)._dispose()

    def _getSelectedIdx(self, menuItems):
        for idx, item in enumerate(menuItems):
            if item['id'] == self._selectedItemID:
                return idx

    def _processContext(self, ctx):
        self._selectedItemID = ctx.get('selectedItemID', self._selectedItemID)
        if self._selectedItemID == RANKEDBATTLES_CONSTS.RANKED_BATTLES_INFO_ID and ctx.get('showedFromWeb', False):
            stateFlags = self.__getShowStateFlags()
            stateFlags['isRankedWelcomeViewShowed'] = True
            self.__setShowStateFlags(stateFlags)

    def _populate(self):
        super(RankedMainPage, self)._populate()
        self._rankedController.onYearPointsChanges += self.__onYearAwardPointsUpdate
        self._rankedController.onUpdated += self._update
        self.__onYearAwardPointsUpdate()
        self.__resetCounters(self._selectedItemID)
        self._updateSounds()
        self._update()

    def _invalidate(self, ctx=None):
        self._processContext(ctx)
        self.__resetCounters(self._selectedItemID)
        self._updateSounds()
        self._update()

    def _update(self):
        self._updateHeader()
        self._updateMenuItems()

    def _updateHeader(self):
        raise NotImplementedError

    def _updateMenuItems(self):
        raise NotImplementedError

    def _updateSounds(self):
        self._rankedController.getSoundManager().setAmbient()

    def __getShowStateFlags(self):
        defaults = AccountSettings.getFilterDefault(GUI_START_BEHAVIOR)
        return self._settingsCore.serverSettings.getSection(GUI_START_BEHAVIOR, defaults)

    def __onYearAwardPointsUpdate(self):
        if not AccountSettings.getSettings(RANKED_AWARDS_BUBBLE_YEAR_REACHED):
            points = self._rankedController.getYearRewardPoints()
            for minPoints, maxPoints in self._rankedController.getYearAwardsPointsMap().itervalues():
                if maxPoints >= points >= minPoints:
                    AccountSettings.setCounters(RANKED_AWARDS_COUNTER, 1)
                    AccountSettings.setSettings(RANKED_AWARDS_BUBBLE_YEAR_REACHED, True)
                    self.__updateCounters()
                    break

    def __resetCounters(self, selectedItemID):
        if selectedItemID == RANKEDBATTLES_CONSTS.RANKED_BATTLES_REWARDS_ID:
            if AccountSettings.getCounters(RANKED_AWARDS_COUNTER) > 0:
                AccountSettings.setCounters(RANKED_AWARDS_COUNTER, 0)
        elif selectedItemID == RANKEDBATTLES_CONSTS.RANKED_BATTLES_INFO_ID:
            AccountSettings.setCounters(RANKED_INFO_COUNTER, 0)
        self.__updateCounters()

    def __setShowStateFlags(self, filters):
        self._settingsCore.serverSettings.setSectionSettings(GUI_START_BEHAVIOR, filters)

    def __updateCounters(self):
        awardsCounter = main_page_vos.getBubbleLabel(AccountSettings.getCounters(RANKED_AWARDS_COUNTER))
        infoCounter = main_page_vos.getBubbleLabel(AccountSettings.getCounters(RANKED_INFO_COUNTER))
        self.as_setCountersS(main_page_vos.getCountersData(awardsCounter, infoCounter))


class RankedMainSeasonOffPage(RankedMainPage):
    _COMMON_SOUND_SPACE = RANKED_MAIN_PAGE_SOUND_SPACE
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, ctx):
        super(RankedMainSeasonOffPage, self).__init__(ctx)
        self.__nextSeason = None
        return

    def _dispose(self):
        self._rankedController.getSoundManager().onSoundModeChanged(False)
        super(RankedMainSeasonOffPage, self)._dispose()

    def _populate(self):
        super(RankedMainSeasonOffPage, self)._populate()
        self._rankedController.getSoundManager().onSoundModeChanged(True)

    def _processContext(self, ctx):
        super(RankedMainSeasonOffPage, self)._processContext(ctx)
        self.__prevSeason = ctx['prevSeason']
        self.__achievedRankID = self.__itemsCache.items.getAccountDossier().getSeasonRankedStats(RankedDossierKeys.SEASON % self.__prevSeason.getNumber(), self.__prevSeason.getSeasonID()).getAchievedRank()

    def _update(self):
        self.__checkDestroy()
        self.__nextSeason = self._rankedController.getNextSeason()
        super(RankedMainSeasonOffPage, self)._update()

    def _updateHeader(self):
        self.as_setHeaderDataS(main_page_vos.getRankedMainSeasonOffHeader(self.__prevSeason, self.__nextSeason, self._selectedItemID))

    def _updateMenuItems(self):
        menuItems = main_page_vos.getRankedMainSeasonOffItems()
        self.as_setDataS({'menuItems': menuItems,
         'selectedIndex': self._getSelectedIdx(menuItems)})

    def _updateSounds(self):
        super(RankedMainSeasonOffPage, self)._updateSounds()
        soundManager = self._rankedController.getSoundManager()
        if self._rankedController.getMaxPossibleRank() == self.__achievedRankID:
            soundManager.setProgressSound()
        else:
            soundManager.setProgressSound(self._rankedController.getDivision(self.__achievedRankID).getUserID())

    def __checkDestroy(self):
        ctrlPrevSeason = self._rankedController.getPreviousSeason()
        isPrevValid = ctrlPrevSeason is not None and ctrlPrevSeason.getSeasonID() == self.__prevSeason.getSeasonID()
        if self._rankedController.getCurrentSeason() is not None or not isPrevValid:
            self.onClose()
        return


class RankedMainSeasonOnPage(RankedMainPage):
    _COMMON_SOUND_SPACE = RANKED_MAIN_PAGE_SOUND_SPACE

    def __init__(self, ctx):
        super(RankedMainSeasonOnPage, self).__init__(ctx)
        self.__currentSeason = None
        self.__periodicNotifier = PeriodicNotifier(self.__getTimeTillCurrentSeasonEnd, self._updateHeader)
        return

    def _dispose(self):
        self._updateSounds(True)
        self.__periodicNotifier.stopNotification()
        self.__periodicNotifier.clear()
        super(RankedMainSeasonOnPage, self)._dispose()

    def _populate(self):
        super(RankedMainSeasonOnPage, self)._populate()
        self.__periodicNotifier.startNotification()

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_UI and self.__selectedRewardsItemID is not None:
            viewPy.setActiveTab(self.__selectedRewardsItemID)
            self.__selectedRewardsItemID = None
        return

    def _update(self):
        self.__currentSeason = self._rankedController.getCurrentSeason()
        self.__periodicNotifier.startNotification()
        super(RankedMainSeasonOnPage, self)._update()

    def _updateHeader(self):
        self.as_setHeaderDataS(main_page_vos.getRankedMainSeasonOnHeader(self.__currentSeason, self._selectedItemID))

    def _updateMenuItems(self):
        menuItems = main_page_vos.getRankedMainSeasonOnItems(self._rankedController.isAccountMastered())
        self.as_setDataS({'menuItems': menuItems,
         'selectedIndex': self._getSelectedIdx(menuItems)})

    def _updateSounds(self, onClose=False):
        super(RankedMainSeasonOnPage, self)._updateSounds()
        soundManager = self._rankedController.getSoundManager()
        if self._rankedController.isAccountMastered():
            soundManager.setProgressSound()
        elif onClose:
            soundManager.setDefaultProgressSound()
        else:
            soundManager.setProgressSound(self._rankedController.getCurrentDivision().getUserID())

    def _processContext(self, ctx):
        super(RankedMainSeasonOnPage, self)._processContext(ctx)
        self.__selectedRewardsItemID = ctx.get('rewardsSelectedTab', None)
        return

    def __getTimeTillCurrentSeasonEnd(self):
        return time_utils.getTimeDeltaFromNowInLocal(time_utils.makeLocalServerTime(self.__currentSeason.getEndDate())) if self.__currentSeason else time_utils.ONE_MINUTE
