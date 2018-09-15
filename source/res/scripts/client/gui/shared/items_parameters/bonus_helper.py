# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/shared/items_parameters/bonus_helper.py
from gui.shared.items_parameters.comparator import CONDITIONAL_BONUSES, getParamExtendedData
from gui.shared.items_parameters.params import VehicleParams
from gui.shared.items_parameters.params import EXTRAS_CAMOUFLAGE
from helpers import dependency
from skeletons.gui.shared import IItemsCache

def isSituationalBonus(bonusName):
    return bonusName in _SITUATIONAL_BONUSES


_SITUATIONAL_BONUSES = ('camouflageNet', 'stereoscope')

def _removeCamouflageModifier(vehicle, bonusID):
    """
    remove camouflage from vehicle copy
    """
    if bonusID == EXTRAS_CAMOUFLAGE:
        oldCamouflages = vehicle.descriptor.camouflages
        for pos, _ in enumerate(oldCamouflages):
            vehicle.descriptor.setCamouflage(pos, None, 0, 0)

    return vehicle


def _removeSkillModifier(vehicle, skillName):
    """
    set new crew in vehicle copy without selected skill
    """
    vehicle.crew = vehicle.getCrewWithoutSkill(skillName)
    return vehicle


def _removeBattleBoosterModifier(vehicle, boosterName):
    if vehicle.equipment.battleBoosterConsumables[0] is not None:
        vehicle.equipment.battleBoosterConsumables[0] = None
    return vehicle


def _removeOptionalDeviceModifier(vehicle, optDevName):
    """
    remove selected optional device from vehicle copy
    """
    for slotIdx, optDev in enumerate(vehicle.optDevices):
        if optDev and optDev.name == optDevName:
            vehicle.descriptor.removeOptionalDevice(slotIdx)
            vehicle.optDevices[slotIdx] = None

    return vehicle


def _removeEquipmentModifier(vehicle, eqName):
    """
    remove selected equipment device from vehicle copy
    """
    for slotIdx, equipment in enumerate(vehicle.equipment.regularConsumables):
        if equipment and equipment.name == eqName:
            vehicle.equipment.regularConsumables[slotIdx] = None

    return vehicle


_VEHICLE_MODIFIERS = {'skill': _removeSkillModifier,
 'extra': _removeCamouflageModifier,
 'equipment': _removeEquipmentModifier,
 'optionalDevice': _removeOptionalDeviceModifier,
 'battleBooster': _removeBattleBoosterModifier}

class _BonusSorter(object):

    def __init__(self, paramName):
        self.__paramName = paramName

    def sort(self, bonuses):
        sortedBonuses = self.__conditionsSorter(list(bonuses))
        sortedBonuses = self.__opticsSorter(sortedBonuses)
        return sortedBonuses

    def __conditionsSorter(self, bonuses):
        if self.__paramName in CONDITIONAL_BONUSES:
            condition, _ = CONDITIONAL_BONUSES[self.__paramName]
            if condition in bonuses:
                bonuses.remove(condition)
                bonuses.append(condition)
        return bonuses

    def __opticsSorter(self, bonuses):
        if self.__paramName == 'circularVisionRadius':
            optics = ('coatedOptics', 'optionalDevice')
            stereoscope = ('stereoscope', 'optionalDevice')
            if stereoscope in bonuses and optics in bonuses:
                stereoscopeIdx = bonuses.index(stereoscope)
                opticsIdx = bonuses.index(optics)
                if stereoscopeIdx > opticsIdx:
                    bonuses[stereoscopeIdx] = optics
                    bonuses[opticsIdx] = stereoscope
        return bonuses


class BonusExtractor(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, vehicle, bonuses, paramName):
        """
        step by step remove bonus influence factors from vehicle
        """
        self.__vehicle = self.itemsCache.items.getVehicleCopy(vehicle)
        self.__paramName = paramName
        self.__bonuses = _BonusSorter(self.__paramName).sort(bonuses)
        self.__removeCamouflage = False
        self.__updateCurrValue()

    def getBonusInfo(self):
        for bnsId, bnsGroup in self.__bonuses:
            yield (bnsGroup, bnsId, self.extractBonus(bnsGroup, bnsId))

    def extractBonus(self, bonusGroup, bonusID):
        """
        Remove bonus influence factor by vehicle modification and save previous params,
        return _ParameterInfo which contains parameters diffs
        """
        oldValue = self.__currValue
        self.__vehicle = _VEHICLE_MODIFIERS[bonusGroup](self.__vehicle, bonusID)
        if bonusGroup == 'extra' and bonusID == EXTRAS_CAMOUFLAGE:
            self.__removeCamouflage = True
        self.__updateCurrValue()
        return getParamExtendedData(self.__paramName, oldValue, self.__currValue)

    def __updateCurrValue(self):
        self.__currValue = getattr(_CustomizedVehicleParams(self.__vehicle, self.__removeCamouflage), self.__paramName)


class _CustomizedVehicleParams(VehicleParams):

    def __init__(self, vehicle, removeCamouflage):
        self.__removeCamouflage = removeCamouflage
        super(_CustomizedVehicleParams, self).__init__(vehicle)

    def _getVehicleDescriptor(self, vehicle):
        """
        removeCamouflage mean that we dont need use customized vehicle descriptor with camouflages influence
        """
        return vehicle.descriptor if self.__removeCamouflage else super(_CustomizedVehicleParams, self)._getVehicleDescriptor(vehicle)
