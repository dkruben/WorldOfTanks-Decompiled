# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/hangar/ammunition_panel.py
import logging
import typing
import SoundGroups
from CurrentVehicle import g_currentVehicle
from account_helpers.AccountSettings import AccountSettings
from account_helpers.AccountSettings import BOOSTERS_FOR_CREDITS_SLOT_COUNTER
from constants import QUEUE_TYPE, PREBATTLE_TYPE
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.shared.fitting_slot_vo import HangarFittingSlotVO
from gui.Scaleform.daapi.view.meta.AmmunitionPanelMeta import AmmunitionPanelMeta
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.ITEM_TYPES import ITEM_TYPES
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared import event_dispatcher as shared_events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.shared.events import LoadViewEvent, ItemRemovalByDemountKitEvent
from gui.shared.gui_items import GUI_ITEM_TYPE, GUI_ITEM_TYPE_NAMES
from gui.shared.gui_items.Vehicle import Vehicle
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.gui_items.vehicle_equipment import BATTLE_BOOSTER_LAYOUT_SIZE
from gui.shared.utils.requesters import REQ_CRITERIA
from helpers import i18n, dependency, int2roman
from items.vehicles import NUM_OPTIONAL_DEVICE_SLOTS
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import List, Tuple, Optional
    from gui.Scaleform.daapi.view.lobby.shared.fitting_slot_vo import FittingSlotVO
ARTEFACTS_SLOTS = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.OPTIONALDEVICE], GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.EQUIPMENT])
_BOOSTERS_SLOTS = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.BATTLE_BOOSTER],)
_ABILITY_SLOTS = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.BATTLE_ABILITY],)
FITTING_MODULES = (GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.CHASSIS],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.TURRET],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.GUN],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.ENGINE],
 GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.RADIO])
FITTING_SLOTS = FITTING_MODULES + ARTEFACTS_SLOTS
HANGAR_FITTING_SLOTS = FITTING_SLOTS + _BOOSTERS_SLOTS + _ABILITY_SLOTS
VEHICLE_FITTING_SLOTS = FITTING_SLOTS + _BOOSTERS_SLOTS
_EMPTY_ID = -1
_logger = logging.getLogger(__name__)
ANIMATION_REMOVE_DK = ('animations/ammunitionPanel/removedDK.swf', 'gui_hangar_ammunition_panel_removed_dk')

def getFittingSlotsData(vehicle, slotsRange, voClass=None):
    devices = []
    voClass = voClass or FittingSlotVO
    modulesData = _getVehicleModulesBySlotType(vehicle)
    for slotType in slotsRange:
        if slotType in ARTEFACTS_SLOTS:
            for slotId in xrange(NUM_OPTIONAL_DEVICE_SLOTS):
                devices.append(voClass(modulesData[slotType], vehicle, slotType, slotId, TOOLTIPS_CONSTANTS.HANGAR_MODULE))

        if slotType in _BOOSTERS_SLOTS:
            for slotId in xrange(BATTLE_BOOSTER_LAYOUT_SIZE):
                devices.append(voClass(modulesData[slotType], vehicle, slotType, slotId, tooltipType=TOOLTIPS_CONSTANTS.BATTLE_BOOSTER))

        if slotType in _ABILITY_SLOTS:
            for slotId, _ in enumerate(vehicle.equipment.battleAbilityConsumables.getIntCDs()):
                devices.append(voClass(modulesData[slotType], vehicle, slotType, slotId, tooltipType=TOOLTIPS_CONSTANTS.EPIC_SKILL_SLOT_INFO))

        devices.append(voClass(modulesData[slotType], vehicle, slotType, tooltipType=TOOLTIPS_CONSTANTS.HANGAR_MODULE))

    return devices


def _getVehicleModulesBySlotType(vehicle):
    equipment = vehicle.equipment.regularConsumables.getInstalledItems()
    battleBoosters = vehicle.equipment.battleBoosterConsumables.getInstalledItems()
    battleAbilities = vehicle.equipment.battleAbilityConsumables.getInstalledItems()
    modules = {GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.CHASSIS]: (vehicle.chassis,),
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.TURRET]: (vehicle.turret,),
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.GUN]: (vehicle.gun,),
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.ENGINE]: (vehicle.engine,),
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.RADIO]: (vehicle.radio,),
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.OPTIONALDEVICE]: filter(None, vehicle.optDevices),
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.EQUIPMENT]: equipment,
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.BATTLE_BOOSTER]: battleBoosters,
     GUI_ITEM_TYPE_NAMES[GUI_ITEM_TYPE.BATTLE_ABILITY]: battleAbilities}
    return modules


def getAmmo(shells):
    outcome = []
    for shell in shells:
        if shell.isHidden:
            continue
        outcome.append({'id': str(shell.intCD),
         'type': shell.type,
         'label': ITEM_TYPES.shell_kindsabbreviation(shell.type),
         'icon': '../maps/icons/ammopanel/ammo/%s' % shell.descriptor.icon[0],
         'count': shell.count,
         'tooltip': '',
         'tooltipType': TOOLTIPS_CONSTANTS.HANGAR_SHELL})

    return outcome


class AmmunitionPanel(AmmunitionPanelMeta, IGlobalListener):
    __slots__ = ('__hangarMessage', '__declaredItemRemovalByDKSlotIndex')
    itemsCache = dependency.descriptor(IItemsCache)
    service = dependency.descriptor(ICustomizationService)

    def __init__(self):
        super(AmmunitionPanel, self).__init__()
        self.__hangarMessage = None
        self.__declaredItemRemovalByDKSlotIndex = None
        return

    def update(self):
        self._update()

    def showTechnicalMaintenance(self):
        self.fireEvent(LoadViewEvent(VIEW_ALIAS.TECHNICAL_MAINTENANCE), EVENT_BUS_SCOPE.LOBBY)

    def showCustomization(self):
        self.service.showCustomization()

    def toRentContinue(self):
        if g_currentVehicle.isPresent():
            vehicle = g_currentVehicle.item
            canBuyOrRent, _ = vehicle.mayObtainForMoney(self.itemsCache.items.stats.money)
            if vehicle.isRentable and vehicle.rentalIsOver and canBuyOrRent:
                shared_events.showVehicleBuyDialog(vehicle)

    def showChangeNation(self):
        if g_currentVehicle.isPresent() and g_currentVehicle.item.hasNationGroup:
            ItemsActionsFactory.doAction(ItemsActionsFactory.CHANGE_NATION, g_currentVehicle.item.intCD)

    def showModuleInfo(self, itemCD):
        if itemCD is not None and int(itemCD) > 0:
            shared_events.showModuleInfo(itemCD, g_currentVehicle.item.descriptor)
        return

    def _populate(self):
        super(AmmunitionPanel, self)._populate()
        self.startGlobalListening()
        g_clientUpdateManager.addMoneyCallback(self.__moneyUpdateCallback)
        g_clientUpdateManager.addCallbacks({'inventory': self.__inventoryUpdateCallBack})
        g_eventBus.addListener(ItemRemovalByDemountKitEvent.DECLARED, self.__itemRemovalByDKDeclareHandler, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(ItemRemovalByDemountKitEvent.CANCELED, self.__itemRemovalByDKCancelHandler, EVENT_BUS_SCOPE.LOBBY)
        self.update()
        AccountSettings.onSettingsChanging += self.__onAccountSettingsChanging

    def _dispose(self):
        self.stopGlobalListening()
        g_clientUpdateManager.removeObjectCallbacks(self)
        g_eventBus.removeListener(ItemRemovalByDemountKitEvent.DECLARED, self.__itemRemovalByDKDeclareHandler, EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(ItemRemovalByDemountKitEvent.CANCELED, self.__itemRemovalByDKCancelHandler, EVENT_BUS_SCOPE.LOBBY)
        self.__hangarMessage = None
        AccountSettings.onSettingsChanging -= self.__onAccountSettingsChanging
        self.__declaredItemRemovalByDK = None
        super(AmmunitionPanel, self)._dispose()
        return

    def _update(self, onlyMoneyUpdate=False):
        if g_currentVehicle.isPresent():
            hangarMessage = g_currentVehicle.getHangarMessage()
            if onlyMoneyUpdate and self.__hangarMessage == hangarMessage:
                return
            vehicle = g_currentVehicle.item
            self.__hangarMessage = hangarMessage
            statusId, msg, msgLvl = hangarMessage
            rentAvailable = False
            if statusId in (Vehicle.VEHICLE_STATE.RENTAL_IS_OVER, Vehicle.VEHICLE_STATE.RENTABLE_AGAIN):
                canBuyOrRent, _ = vehicle.mayObtainForMoney(self.itemsCache.items.stats.money)
                rentAvailable = vehicle.isRentable and canBuyOrRent
            if msgLvl == Vehicle.VEHICLE_STATE_LEVEL.RENTABLE:
                msgLvl = Vehicle.VEHICLE_STATE_LEVEL.INFO
            self.__applyCustomizationNewCounter(vehicle)
            self.__applyBoosterNewCounter()
            msgString = ''
            if statusId != Vehicle.VEHICLE_STATE.UNDAMAGED:
                msgString = makeHtmlString('html_templates:vehicleStatus', msgLvl, {'message': i18n.makeString(msg)})
            self.__updateDevices(vehicle)
            self.as_updateVehicleStatusS({'message': msgString,
             'rentAvailable': rentAvailable,
             'isElite': vehicle.isElite,
             'tankType': '{}_elite'.format(vehicle.type) if vehicle.isElite else vehicle.type,
             'vehicleLevel': '{}'.format(int2roman(vehicle.level)),
             'vehicleName': '{}'.format(vehicle.shortUserName)})

    def __inventoryUpdateCallBack(self, *args):
        self.update()

    def __applyCustomizationNewCounter(self, vehicle):
        counter = vehicle.getC11nItemsNoveltyCounter(self.itemsCache.items) if vehicle.isCustomizationEnabled() else 0
        self.as_setCustomizationBtnCounterS(counter)

    def __applyBoosterNewCounter(self):
        counter = AccountSettings.getCounters(BOOSTERS_FOR_CREDITS_SLOT_COUNTER)
        self.as_setBoosterBtnCounterS(counter)

    def __moneyUpdateCallback(self, *_):
        self._update(onlyMoneyUpdate=True)

    def __updateDevices(self, vehicle):
        shells = []
        stateWarning = False
        if g_currentVehicle.isPresent():
            stateWarning = vehicle.isBroken or not vehicle.isAmmoFull or not g_currentVehicle.isAutoLoadFull() or not g_currentVehicle.isAutoEquipFull()
            shells = getAmmo(vehicle.shells)
        self.as_setAmmoS(shells, stateWarning)
        self.as_setModulesEnabledS(True)
        self.as_setVehicleHasTurretS(vehicle.hasTurrets)
        slotsRange = self.__getSlotsRange()
        devices = getFittingSlotsData(vehicle, slotsRange, voClass=HangarFittingSlotVO)
        self.__handleAnimationsForDemountKitRemoval(devices)
        self.as_setDataS({'devices': devices})
        if slotsRange == HANGAR_FITTING_SLOTS and self.itemsCache.items.getItems(GUI_ITEM_TYPE.BATTLE_ABILITY, REQ_CRITERIA.UNLOCKED):
            showAlert = True
            for slot in devices:
                if slot['slotType'] in _ABILITY_SLOTS and slot['id'] != -1:
                    showAlert = False
                    break

            self.as_showBattleAbilitiesAlertS(showAlert)
        else:
            self.as_showBattleAbilitiesAlertS(False)

    def __getSlotsRange(self):
        return HANGAR_FITTING_SLOTS if self.prbDispatcher is not None and self.prbDispatcher.getFunctionalState().isInPreQueue(QUEUE_TYPE.EPIC) or self.prbDispatcher.getFunctionalState().isInUnit(PREBATTLE_TYPE.EPIC) else VEHICLE_FITTING_SLOTS

    def __onAccountSettingsChanging(self, key, _):
        if key == BOOSTERS_FOR_CREDITS_SLOT_COUNTER:
            self.__applyBoosterNewCounter()

    def __itemRemovalByDKDeclareHandler(self, event):
        self.__declaredItemRemovalByDKSlotIndex = event.slotIndex

    def __itemRemovalByDKCancelHandler(self, _):
        self.__declaredItemRemovalByDKSlotIndex = None
        return

    def __handleAnimationsForDemountKitRemoval(self, items):
        if self.__declaredItemRemovalByDKSlotIndex is None:
            return
        else:
            for item in items:
                slotType = item['slotType']
                slotIndex = item['slotIndex']
                if slotType == FITTING_TYPES.OPTIONAL_DEVICE and self.__declaredItemRemovalByDKSlotIndex == slotIndex:
                    self.__declaredItemRemovalByDKSlotIndex = None
                    self.__playAnimation(slotType, slotIndex, ANIMATION_REMOVE_DK)

            return

    def __playAnimation(self, slotType, slotIndex, animData):
        swfPath = animData[0]
        soundID = animData[1]
        self.as_showAnimationS(slotType, slotIndex, swfPath)
        SoundGroups.g_instance.playSound2D(soundID)
