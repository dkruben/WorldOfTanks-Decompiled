# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/game_control/special_sound_ctrl.py
from collections import namedtuple
import logging
import ResMgr
import SoundGroups
import nations
from account_helpers.settings_core import settings_constants
from account_helpers.settings_core.options import AltVoicesSetting
from helpers import dependency
from SoundGroups import CREW_GENDER_SWITCHES
from items import tankmen
from constants import ITEM_DEFS_PATH
from items.components.crew_skins_constants import NO_CREW_SKIN_ID, NO_CREW_SKIN_SOUND_SET
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.game_control import ISpecialSoundCtrl
from items.vehicles import VehicleDescr
from gui.battle_control import avatar_getter
from PlayerEvents import g_playerEvents
from gui.shared.gui_items.customization.outfit import Outfit
from skeletons.gui.battle_session import IBattleSessionProvider
_logger = logging.getLogger(__name__)
_XML_PATH = ITEM_DEFS_PATH + 'special_voices.xml'
_VoiceoverParams = namedtuple('_VoiceoverParams', ['languageMode', 'genderSwitch', 'onlyInNational'])
_genderStrToSwitch = {'male': CREW_GENDER_SWITCHES.MALE,
 'female': CREW_GENDER_SWITCHES.FEMALE}

class SpecialSoundCtrl(ISpecialSoundCtrl):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __settingsCore = dependency.descriptor(ISettingsCore)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        self.__voiceoverByVehicle = {}
        self.__voiceoverByTankman = {}
        self.__arenaMusicByStyle = {}
        self.__currentMode = None
        self.__arenaMusicSetup = None
        return

    @property
    def arenaMusicSetup(self):
        if self.__arenaMusicSetup is not None:
            return self.__arenaMusicSetup
        else:
            arena = avatar_getter.getArena()
            return arena.arenaType.wwmusicSetup if arena is not None else None

    @property
    def specialVoice(self):
        return self.__currentMode

    def init(self):
        self.__readSpecialVoices()
        g_playerEvents.onAvatarBecomeNonPlayer += self.__onAvatarBecomeNonPlayer

    def fini(self):
        self.__voiceoverByVehicle = None
        self.__voiceoverByTankman = None
        self.__arenaMusicByStyle = None
        self.__arenaMusicSetup = None
        self.__currentMode = None
        g_playerEvents.onAvatarBecomeNonPlayer -= self.__onAvatarBecomeNonPlayer
        return

    def setPlayerVehicle(self, vehiclePublicInfo, isPlayerVehicle):
        self.__setVoiceoverByVehicleOrTankman(vehiclePublicInfo, isPlayerVehicle)
        self.__setArenaMusicByStyle(vehiclePublicInfo, isPlayerVehicle)

    def __setVoiceoverByVehicleOrTankman(self, vehiclePublicInfo, isPlayerVehicle):
        vehicleType = VehicleDescr(vehiclePublicInfo.compDescr).type
        if self.__setSpecialVoiceByVehicle(vehicleType.name, isPlayerVehicle):
            return
        else:
            groupID, isFemale, isPremium = tankmen.unpackCrewParams(vehiclePublicInfo.crewGroup)
            nationID, _ = vehicleType.id
            if self.__setSpecialVoiceByTankmen(nationID, groupID, isPremium):
                return
            preset = SoundGroups.g_instance.soundModes.currentNationalPreset
            isNationalPreset = preset[1] if preset is not None else False
            if isNationalPreset:
                commanderSkinID = vehiclePublicInfo.commanderSkinID
                if self.__setSpecialVoiceByCommanderSkinID(isFemale, commanderSkinID):
                    return
            genderSwitch = CREW_GENDER_SWITCHES.FEMALE if isFemale and isNationalPreset else CREW_GENDER_SWITCHES.DEFAULT
            SoundGroups.g_instance.soundModes.setCurrentNation(nations.NAMES[nationID], genderSwitch)
            return

    def __setArenaMusicByStyle(self, vehiclePublicInfo, isPlayerVehicle):
        self.__arenaMusicSetup = None
        arena = avatar_getter.getArena()
        if arena is None:
            return
        else:
            arenaVisitor = self.__sessionProvider.arenaVisitor
            if arenaVisitor.bonus.hasRespawns():
                _logger.debug('Skip special arena sound according to game mode')
                return
            if isPlayerVehicle and vehiclePublicInfo.outfit:
                outfit = Outfit(vehiclePublicInfo.outfit)
                if outfit.style and outfit.style.tags:
                    for tag, arenaMusic in self.__arenaMusicByStyle.iteritems():
                        if tag in outfit.style.tags:
                            self.__arenaMusicSetup = arena.arenaType.wwmusicSetup.copy()
                            self.__arenaMusicSetup.update(arenaMusic)
                            return

            return

    def __onAvatarBecomeNonPlayer(self):
        self.__arenaMusicSetup = None
        self.__currentMode = None
        return

    def __readSpecialVoices(self):
        rootSection = ResMgr.openSection(_XML_PATH)
        if rootSection is None:
            _logger.error('Could not open special voices xml: %s', _XML_PATH)
            return
        else:
            voiceoverSection = rootSection['voiceover']
            if voiceoverSection is not None:
                for source, paramSection in voiceoverSection.items():
                    tag = paramSection.readString('tag')
                    mode = paramSection.readString('languageMode')
                    onlyInNational = paramSection.readBool('onlyInNational')
                    genderStr = paramSection.readString('gender')
                    gender = _genderStrToSwitch.get(genderStr, CREW_GENDER_SWITCHES.DEFAULT)
                    if source == 'tankman':
                        self.__voiceoverByTankman[tag] = _VoiceoverParams(mode, gender, onlyInNational)
                    if source == 'vehicle':
                        self.__voiceoverByVehicle[tag] = _VoiceoverParams(mode, gender, onlyInNational)

            arenaMusicSection = rootSection['arenaMusic']
            if arenaMusicSection is not None:
                for source, paramSection in arenaMusicSection.items():
                    if source != 'style':
                        continue
                    tag = paramSection.readString('tag')
                    arenaMusic = {}
                    musicSetupSection = paramSection['wwmusicSetup']
                    if musicSetupSection is not None:
                        for name, value in musicSetupSection.items():
                            arenaMusic[name] = value.asString

                    self.__arenaMusicByStyle[tag] = arenaMusic

            return

    def __setSpecialVoiceByVehicle(self, vehicleName, isPlayerVehicle):
        if isPlayerVehicle:
            params = self.__voiceoverByVehicle.get(vehicleName)
            if params is not None:
                self.__setSpecialVoice(params)
                return True
        return False

    def __setSpecialVoiceByTankmen(self, nationID, groupID, isPremium):
        for tag, params in self.__voiceoverByTankman.iteritems():
            if tankmen.hasTagInTankmenGroup(nationID, groupID, isPremium, tag):
                self.__setSpecialVoice(params)
                return True

        return False

    def __setSpecialVoiceByCommanderSkinID(self, isFemale, commanderSkinID):
        if commanderSkinID != NO_CREW_SKIN_ID and self.__lobbyContext.getServerSettings().isCrewSkinsEnabled():
            skin = tankmen.g_cache.crewSkins().skins.get(commanderSkinID)
            if skin is not None and skin.soundSetID != NO_CREW_SKIN_SOUND_SET:
                params = _VoiceoverParams(languageMode=skin.soundSetID, genderSwitch=CREW_GENDER_SWITCHES.GENDER_ALL[isFemale], onlyInNational=False)
                self.__setSpecialVoice(params)
                return True
        return False

    def __setSpecialVoice(self, params):
        setting = self.__settingsCore.options.getSetting(settings_constants.SOUND.ALT_VOICES)
        if params.onlyInNational and setting.getSystemModeType() == AltVoicesSetting.SOUND_MODE_TYPE.REGULAR:
            _logger.debug('%s can be used only in national sound mode', params.languageMode)
            return
        if not SoundGroups.g_instance.soundModes.setMode(params.languageMode):
            _logger.warning('Could not set special voice: %s', params.languageMode)
            return
        self.__currentMode = params
        if params.genderSwitch != CREW_GENDER_SWITCHES.DEFAULT:
            SoundGroups.g_instance.setSwitch(CREW_GENDER_SWITCHES.GROUP, params.genderSwitch)
