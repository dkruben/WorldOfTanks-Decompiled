# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/settings/tooltips.py
from gui.Scaleform.daapi.view.lobby.customization.tooltips import ElementTooltip as CustomizationElementTooltip, QuestElementTooltip as CustomizationQuestElementTooltip
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_calendar_day_tooltip import RankedCalendarDayTooltip
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_calendar_steps_tooltip import RankedCalendarStepsTooltip
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_selector_tooltip import RankedSelectorTooltip
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_step_tooltip import RankedStepTooltip
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.tooltips import vehicle, tankman, skill, shell, module, achievement, cybersport, common, contexts, battle_consumable, tutorial, fortifications, boosters, veh_cmp, quests, ranked, battle_booster, bootcamp, personal_missions, elen
from gui.shared.tooltips.filter import VehicleFilterTooltip
from gui.shared.tooltips.wgm_currency import WGMGoldCurrencyTooltip, WGMCreditsCurrencyTooltip
DYNAMIC_TOOLTIPS = {TOOLTIPS_CONSTANTS.GOLD_STATS: WGMGoldCurrencyTooltip(contexts.ToolTipContext(None)),
 TOOLTIPS_CONSTANTS.CREDITS_STATS: WGMCreditsCurrencyTooltip(contexts.ToolTipContext(None))}
TOOLTIPS = {TOOLTIPS_CONSTANTS.TANKMAN: {'tooltip': TOOLTIPS_CONSTANTS.TANKMEN_UI,
                              'method': lambda invID, isCurrentVehicle=None: tankman.TankmanTooltipData(contexts.TankmanHangarContext()).buildToolTip(invID),
                              'complex': None},
 TOOLTIPS_CONSTANTS.TANKMAN_SKILL: {'tooltip': TOOLTIPS_CONSTANTS.TANKMEN_SKILL_UI,
                                    'method': skill.SkillTooltipData(contexts.PersonalCaseContext(fieldsToExclude=('count',))).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.TANKMAN_NEW_SKILL: {'tooltip': TOOLTIPS_CONSTANTS.TANKMEN_BUY_SKILL_UI,
                                        'method': skill.BuySkillTooltipData(contexts.NewSkillContext()).buildToolTip,
                                        'complex': lambda tooltipData: tooltipData['count'] > 1 or tooltipData['level'] > 0},
 TOOLTIPS_CONSTANTS.BATTLE_STATS_ACHIEVS: {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                                           'method': achievement.AchievementTooltipData(contexts.BattleResultContext()).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.ACHIEVEMENT: {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                                  'method': achievement.AchievementTooltipData(contexts.ProfileContext()).buildToolTip,
                                  'complex': None},
 TOOLTIPS_CONSTANTS.MARKS_ON_GUN_ACHIEVEMENT: {'tooltip': TOOLTIPS_CONSTANTS.MARKS_ON_GUN_UI,
                                               'method': achievement.AchievementTooltipData(contexts.ProfileContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.BATTLE_STATS_MARKS_ON_GUN_ACHIEVEMENT: {'tooltip': TOOLTIPS_CONSTANTS.MARKS_ON_GUN_UI,
                                                            'method': achievement.AchievementTooltipData(contexts.BattleResultMarksOnGunContext()).buildToolTip,
                                                            'complex': None},
 TOOLTIPS_CONSTANTS.GLOBAL_RATING: {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                                    'method': achievement.GlobalRatingTooltipData(contexts.ProfileContext()).buildToolTip,
                                    'complex': None},
 'achievementAttr': {'tooltip': TOOLTIPS_CONSTANTS.ACHIEVEMENT_UI,
                     'method': None,
                     'complex': None},
 TOOLTIPS_CONSTANTS.MARK_OF_MASTERY: {'tooltip': TOOLTIPS_CONSTANTS.MARK_OF_MASTERY_UI,
                                      'method': achievement.AchievementTooltipData(contexts.BattleResultMarkOfMasteryContext(fieldsToExclude=('showCondSeparator',))).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.CAROUSEL_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                       'method': vehicle.VehicleInfoTooltipData(contexts.CarouselContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                        'method': lambda intCD, sellPrice=0, sellCurrency=0, inventoryCount=0, vehicleCount=0: vehicle.VehicleInfoTooltipData(contexts.InventoryContext()).buildToolTip(intCD),
                                        'complex': None},
 TOOLTIPS_CONSTANTS.TECHTREE_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                       'method': vehicle.VehicleInfoTooltipData(contexts.TechTreeContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                   'method': lambda intCD, inventoryCount=0, vehicleCount=0: vehicle.VehicleInfoTooltipData(contexts.ShopContext()).buildToolTip(intCD),
                                   'complex': None},
 TOOLTIPS_CONSTANTS.AWARD_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                    'method': vehicle.VehicleInfoTooltipData(contexts.AwardContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.TRADE_IN: {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
                               'method': vehicle.VehicleTradeInTooltipData(contexts.HangarContext()).buildToolTip,
                               'complex': lambda data: False},
 TOOLTIPS_CONSTANTS.TRADE_IN_PRICE: {'tooltip': TOOLTIPS_CONSTANTS.TRADE_IN_PRICE,
                                     'method': vehicle.VehicleTradeInPriceTooltipData(contexts.HangarContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                       'method': lambda intCD, sellPrice=0, sellCurrency=0, inventoryCount=0, vehicleCount=0: module.ModuleBlockTooltipData(contexts.InventoryContext()).buildToolTip(intCD),
                                       'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_BATTLE_BOOSTER: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                               'method': battle_booster.BattleBoosterBlockTooltipData(contexts.InventoryBattleBoosterContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.TECH_MAIN_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                       'method': lambda intCD, buyPrice=None, inventoryCount=0, vehicleCount=0, slotIdx=0, eqs=None: module.ModuleBlockTooltipData(contexts.TechMainContext()).buildToolTip(intCD, slotIdx, eqs),
                                       'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                    'method': module.ModuleBlockTooltipData(contexts.HangarContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.BATTLE_BOOSTER: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': battle_booster.BattleBoosterBlockTooltipData(contexts.HangarContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.BATTLE_BOOSTER_COMPARE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                             'method': battle_booster.BattleBoosterBlockTooltipData(contexts.VehCmpConfigurationContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.COMPARE_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': module.ModuleBlockTooltipData(contexts.VehCmpConfigurationContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.PREVIEW_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': module.ModuleBlockTooltipData(contexts.PreviewContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.TECHTREE_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': module.ModuleBlockTooltipData(contexts.TechTreeContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.VEH_COMPARE_TECHTREE_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                  'method': module.ModuleBlockTooltipData(contexts.VehCmpModulesContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                  'method': lambda intCD, inventoryCount=0, vehicleCount=0: module.ModuleBlockTooltipData(contexts.ShopContext()).buildToolTip(intCD),
                                  'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_BATTLE_BOOSTER: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                          'method': battle_booster.BattleBoosterBlockTooltipData(contexts.ShopBattleBoosterContext()).buildToolTip,
                                          'complex': None},
 TOOLTIPS_CONSTANTS.AWARD_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                   'method': module.ModuleBlockTooltipData(contexts.AwardContext()).buildToolTip,
                                   'complex': None},
 TOOLTIPS_CONSTANTS.SHOP_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                 'method': lambda intCD, inventoryCount=0, vehicleCount=0: shell.ShellBlockToolTipData(contexts.ShopContext()).buildToolTip(intCD),
                                 'complex': None},
 TOOLTIPS_CONSTANTS.AWARD_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                  'method': lambda intCD, inventoryCount=0, vehicleCount=0: shell.ShellBlockToolTipData(contexts.AwardContext()).buildToolTip(intCD),
                                  'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                   'method': lambda intCD, historicalBattleID=-1: shell.ShellBlockToolTipData(contexts.HangarContext()).buildToolTip(intCD, historicalBattleID=historicalBattleID),
                                   'complex': None},
 TOOLTIPS_CONSTANTS.COMPARE_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                    'method': lambda intCD, historicalBattleID=-1: shell.ShellBlockToolTipData(contexts.VehCmpConfigurationContext(), basicDataAllowed=False).buildToolTip(intCD, historicalBattleID=historicalBattleID),
                                    'complex': None},
 TOOLTIPS_CONSTANTS.INVENTORY_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': lambda intCD, sellPrice=0, sellCurrency=0, inventoryCount=0, vehicleCount=0: shell.ShellBlockToolTipData(contexts.InventoryContext()).buildToolTip(intCD),
                                      'complex': None},
 TOOLTIPS_CONSTANTS.TECH_MAIN_SHELL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': lambda intCD, buyPrice=None, inventoryCount=0, vehicleCount=0, slotIdx=0, eqs=None: shell.ShellBlockToolTipData(contexts.TechMainContext()).buildToolTip(intCD, slotIdx, eqs),
                                      'complex': None},
 TOOLTIPS_CONSTANTS.EFFICIENCY_PARAM: {'tooltip': TOOLTIPS_CONSTANTS.FINAL_STSTS_UI,
                                       'method': common.EfficiencyTooltipData(contexts.FinalStatisticContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_VEHICLE_INFO: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_VEHICLE_INFO_UI,
                                                            'method': tutorial.ResearchVehicleInfoPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                            'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES_PREMIUM: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES_PREMIUM_UI,
                                                               'method': tutorial.ResearchModulesPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                               'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_MODULES_UI,
                                                       'method': tutorial.ResearchModulesPackerEx(contexts.HangarTutorialContext()).buildToolTip,
                                                       'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_CUSTOMIZATION_TYPES: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_CUSTOMIZATION_TYPES_UI,
                                                          'method': tutorial.CustomizationTypesPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                          'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_NATIONS: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_NATIONS_UI,
                                              'method': tutorial.NationsPacker(contexts.HangarTutorialContext()).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_TREE: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_RESEARCH_TREE_UI,
                                                    'method': tutorial.ResearchTreePacker(contexts.HangarTutorialContext()).buildToolTip,
                                                    'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_SKILLS: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_SKILLS_UI,
                                                           'method': tutorial.PersonalCaseSkillsPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                           'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_PERKS: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_PERKS_UI,
                                                          'method': tutorial.PersonalCasePerksPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                          'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_ADDITIONAL: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_PERSONAL_CASE_ADDITIONAL_UI,
                                                               'method': tutorial.PersonalCaseAdditionalPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                               'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_AMMUNITION: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_AMMUNITION_UI,
                                                 'method': tutorial.AmmunitionPacker(contexts.HangarTutorialContext()).buildToolTip,
                                                 'complex': None},
 TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_EQUPMENT: {'tooltip': TOOLTIPS_CONSTANTS.HANGAR_TUTORIAL_EQUPMENT_UI,
                                               'method': tutorial.EquipmentPacker(contexts.HangarTutorialContext()).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.IGR_INFO: {'tooltip': TOOLTIPS_CONSTANTS.IGR_INFO_UI,
                               'method': common.IgrTooltipData(contexts.HangarContext()).buildToolTip,
                               'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_SLOT: {'tooltip': TOOLTIPS_CONSTANTS.SUITABLE_VEHICLE_UI,
                                       'method': cybersport.CybersportSlotToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_SELECTED_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                   'method': cybersport.CybersportSelectedVehicleToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                   'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_SLOT_SELECTED: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                'method': cybersport.CybersportSlotSelectedToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_TEAM: {'tooltip': TOOLTIPS_CONSTANTS.UNIT_COMMAND,
                                       'method': cybersport.CybersportUnitToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.CONTACT: {'tooltip': TOOLTIPS_CONSTANTS.CONTACT_UI,
                              'method': common.ContactTooltipData(contexts.ContactContext()).buildToolTip,
                              'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_UNIT_LEVEL: {'tooltip': TOOLTIPS_CONSTANTS.UNIT_LEVEL_UI,
                                             'method': cybersport.CybersportUnitLevelToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.CYBER_SPORT_VEHICLE_NOT_READY: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                    'method': cybersport.CybersportSlotSelectedToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                    'complex': None},
 TOOLTIPS_CONSTANTS.RSS_NEWS: {'tooltip': TOOLTIPS_CONSTANTS.RSS_NEWS_UI,
                               'method': None,
                               'complex': None},
 TOOLTIPS_CONSTANTS.SORTIE_DIVISION: {'tooltip': TOOLTIPS_CONSTANTS.SORTIE_DIVISION_UI,
                                      'method': common.SortieDivisionTooltipData(contexts.FortificationContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.MAP: {'tooltip': TOOLTIPS_CONSTANTS.MAP_UI,
                          'method': common.MapTooltipData(contexts.HangarContext()).buildToolTip,
                          'complex': None},
 TOOLTIPS_CONSTANTS.HISTORICAL_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_INFO_UI,
                                         'method': vehicle.VehicleInfoTooltipData(contexts.HangarContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_SIMPLE_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                                'method': vehicle.VehicleSimpleParametersTooltipData(contexts.HangarParamContext()).buildToolTip,
                                                'complex': None},
 TOOLTIPS_CONSTANTS.BASE_VEHICLE_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                              'method': vehicle.BaseVehicleAdvancedParametersTooltipData(contexts.BaseHangarParamContext()).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_CMP_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                             'method': vehicle.BaseVehicleAdvancedParametersTooltipData(contexts.CmpParamContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_AVG_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                             'method': vehicle.VehicleAvgParameterTooltipData(contexts.HangarParamContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                                  'method': vehicle.VehicleAdvancedParametersTooltipData(contexts.HangarParamContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_SIMPLE_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                                        'method': vehicle.VehicleSimpleParametersTooltipData(contexts.PreviewParamContext()).buildToolTip,
                                                        'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_AVG_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                                     'method': vehicle.VehicleAvgParameterTooltipData(contexts.PreviewParamContext()).buildToolTip,
                                                     'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_ADVANCED_PARAMETERS: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PARAMETERS_UI,
                                                          'method': vehicle.VehicleAdvancedParametersTooltipData(contexts.PreviewParamContext()).buildToolTip,
                                                          'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER: {'tooltip': TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_CREW_MEMBER_UI,
                                                  'method': vehicle.VehiclePreviewCrewMemberTooltipData(contexts.PreviewContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.VEH_CMP_CUSTOMIZATION: {'tooltip': TOOLTIPS_CONSTANTS.VEH_CMP_CUSTOMIZATION_UI,
                                            'method': veh_cmp.VehCmpCustomizationTooltip(contexts.HangarParamContext()).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.VEH_CMP_SKILLS: {'tooltip': TOOLTIPS_CONSTANTS.VEH_CMP_SKILLS_UI,
                                     'method': veh_cmp.VehCmpSkillsTooltip(contexts.HangarParamContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.TANKMAN_SKILL_EXTENDED: {'tooltip': TOOLTIPS_CONSTANTS.TANKMAN_SKILL_EXTENDED_UI,
                                             'method': skill.TankmanSkillTooltipData(contexts.HangarParamContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_CONTROL: {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
                                       'method': common.SettingsControlTooltipData(contexts.HangarContext()).buildToolTip,
                                       'complex': lambda data: False},
 TOOLTIPS_CONSTANTS.CLAN_COMMON_INFO: {'tooltip': TOOLTIPS_CONSTANTS.CLAN_COMMON_INFO_UI,
                                       'method': common.ClanCommonInfoTooltipData(contexts.HangarContext()).buildToolTip,
                                       'complex': None},
 TOOLTIPS_CONSTANTS.REF_SYS_AWARDS: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_AWARDS_UI,
                                     'method': common.ToolTipRefSysAwards(contexts.HangarContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.REF_SYS_DESCRIPTION: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_DESCRIPTION_UI,
                                          'method': common.ToolTipRefSysDescription(contexts.HangarContext()).buildToolTip,
                                          'complex': None},
 TOOLTIPS_CONSTANTS.REF_SYS_XP_MULTIPLIER: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_XP_MULTIPLIER_UI,
                                            'method': common.ToolTipRefSysXPMultiplier(contexts.HangarContext()).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.ACTION_PRICE: {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
                                   'method': common.ActionTooltipData(contexts.HangarContext()).buildToolTip,
                                   'complex': lambda data: False},
 TOOLTIPS_CONSTANTS.SQUAD_SLOT_VEHICLE_SELECTED: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                  'method': cybersport.SquadSlotSelectedToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_BUTTON: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_BUTTON_UI,
                                      'method': common.SettingsButtonTooltipData(contexts.HangarServerStatusContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.CUSTOMIZATION_ITEM: {'tooltip': TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI,
                                         'method': CustomizationQuestElementTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM: {'tooltip': TOOLTIPS_CONSTANTS.TECH_CUSTOMIZATION_ITEM_UI,
                                              'method': CustomizationElementTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.QUESTS_VEHICLE_BONUSES: {'tooltip': TOOLTIPS_CONSTANTS.COLUMN_FIELDS_UI,
                                             'method': common.QuestVehiclesBonusTooltipData(contexts.QuestContext()).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.MAP_SMALL: {'tooltip': TOOLTIPS_CONSTANTS.MAP_SMALL_UI,
                                'method': common.MapSmallTooltipData(contexts.FortificationContext()).buildToolTip,
                                'complex': None},
 TOOLTIPS_CONSTANTS.BATTLE_CONSUMABLE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                        'method': battle_consumable.BattleConsumableTooltipData(contexts.BattleConsumableContext()).buildToolTip,
                                        'complex': None},
 TOOLTIPS_CONSTANTS.ENVIRONMENT: {'tooltip': TOOLTIPS_CONSTANTS.ENVIRONMENT_UI,
                                  'method': common.EnvironmentTooltipData(contexts.HangarContext()).buildToolTip,
                                  'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_MINIMAP_CIRCLES: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_MINIMAP_CIRCLES_UI,
                                               'method': common.SettingsMinimapCircles(contexts.SettingsMinimapContext(None)).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.SQUAD_RESTRICTIONS_INFO: {'tooltip': TOOLTIPS_CONSTANTS.SQUAD_RESTRICTIONS_INFO_UI,
                                              'method': common.SquadRestrictionsInfo(contexts.SquadRestrictionContext(None)).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI,
                                            'method': boosters.BoosterTooltipData(contexts.BoosterContext()).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.BOOSTERS_SHOP: {'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI,
                                    'method': boosters.BoosterTooltipData(contexts.ShopBoosterContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.BOOSTERS_QUESTS: {'tooltip': TOOLTIPS_CONSTANTS.BOOSTERS_BOOSTER_INFO_UI,
                                      'method': boosters.BoosterTooltipData(contexts.QuestsBoosterContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.QUESTS_PREVIEW: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': quests.QuestsPreviewTooltipData(contexts.QuestsBoosterContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.PERSONAL_QUESTS_PREVIEW: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                              'method': personal_missions.PersonalMissionPreviewTooltipData(contexts.PersonalMissionContext()).buildToolTip,
                                              'complex': None},
 TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_TANKWOMAN: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                  'method': personal_missions.TankwomanTooltipData(contexts.PersonalMissionContext()).buildToolTip,
                                                  'complex': None},
 TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_TANKMODULE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                   'method': personal_missions.TankModuleTooltipData(contexts.PersonalMissionContext()).buildToolTip,
                                                   'complex': None},
 TOOLTIPS_CONSTANTS.SHEDULE_QUEST: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                    'method': quests.ScheduleQuestTooltipData(contexts.QuestContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.MISSION_VEHICLE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': quests.MissionVehiclesConditionTooltipData(contexts.QuestContext()).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.MISSION_VEHICLE_TYPE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                           'method': quests.MissionVehiclesTypeTooltipData(contexts.QuestContext()).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.ADDITIONAL_AWARDS: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                        'method': quests.AdditionalAwardTooltipData(contexts.QuestContext()).buildToolTip,
                                        'complex': None},
 TOOLTIPS_CONSTANTS.UNAVAILABLE_QUEST: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                        'method': quests.UnavailableQuestTooltipData(contexts.QuestContext()).buildToolTip,
                                        'complex': None},
 TOOLTIPS_CONSTANTS.VEHICLE_FILTER: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                     'method': VehicleFilterTooltip(contexts.TechCustomizationContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.DIRECT_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_DIRECTS_UI,
                                    'method': fortifications.ToolTipRefSysDirects(contexts.FortificationContext()).buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_KEY_FOLLOW_ME: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_KEY_FOLLOW_ME_UI,
                                             'method': common.SettingsKeyFollowMe(contexts.ToolTipContext(None)).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_KEY_TURN_BACK: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_KEY_TURN_BACK_UI,
                                             'method': common.SettingsKeyTurnBack(contexts.ToolTipContext(None)).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_KEY_NEED_HELP: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_KEY_NEED_HELP_UI,
                                             'method': common.SettingsKeyNeedHelp(contexts.ToolTipContext(None)).buildToolTip,
                                             'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_KEY_RELOAD: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_KEY_RELOAD_UI,
                                          'method': common.SettingsKeyReload(contexts.ToolTipContext(None)).buildToolTip,
                                          'complex': None},
 TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_TRADEOFF: {'tooltip': TOOLTIPS_CONSTANTS.SELECTED_VEHICLE_UI,
                                                'method': cybersport.CybersportSelectedVehicleToolTipData(contexts.CyberSportUnitContext()).buildToolTip,
                                                'complex': None},
 TOOLTIPS_CONSTANTS.RANKED_BATTLES_RANK: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                          'method': ranked.RankedTooltipData(contexts.RankedRankContext()).buildToolTip,
                                          'complex': None},
 TOOLTIPS_CONSTANTS.MISSIONS_TOKEN: {'tooltip': TOOLTIPS_CONSTANTS.MISSIONS_TOKEN_UI,
                                     'method': common.MissionsToken(contexts.QuestContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.RESERVE_MODULE: {'tooltip': TOOLTIPS_CONSTANTS.REF_SYS_RESERVES_UI,
                                     'method': common.ReserveTooltipData(contexts.ReserveContext()).buildToolTip,
                                     'complex': None},
 TOOLTIPS_CONSTANTS.RANKED_STEP: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                  'method': RankedStepTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                  'complex': None},
 'default': {'tooltip': TOOLTIPS_CONSTANTS.COMPLEX_UI,
             'method': None,
             'complex': None},
 TOOLTIPS_CONSTANTS.SETTINGS_KEY_SWITCH_MODE: {'tooltip': TOOLTIPS_CONSTANTS.SETTINGS_KEY_SWITCH_MODE_UI,
                                               'method': common.SettingKeySwitchMode(contexts.ToolTipContext(None)).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.GOLD_STATS: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                 'method': DYNAMIC_TOOLTIPS[TOOLTIPS_CONSTANTS.GOLD_STATS].buildToolTip,
                                 'complex': None},
 TOOLTIPS_CONSTANTS.CREDITS_STATS: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                    'method': DYNAMIC_TOOLTIPS[TOOLTIPS_CONSTANTS.CREDITS_STATS].buildToolTip,
                                    'complex': None},
 TOOLTIPS_CONSTANTS.CRYSTAL_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                   'method': common.HeaderCrystalInfo(contexts.ToolTipContext(None)).buildToolTip,
                                   'complex': None},
 TOOLTIPS_CONSTANTS.RANKED_CALENDAR_DAY_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                               'method': RankedCalendarDayTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                               'complex': None},
 TOOLTIPS_CONSTANTS.RANKED_CALENDAR_STEPS_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                 'method': RankedCalendarStepsTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                                 'complex': None},
 TOOLTIPS_CONSTANTS.RANKED_SELECTOR_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                           'method': RankedSelectorTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.BOOTCAMP_AWARD_MEDAL: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                           'method': bootcamp.StatsTooltipData(contexts.ToolTipContext(None)).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.EVENT_QUESTS_PREVIEW: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                           'method': elen.ElenPreviewTooltipData(contexts.QuestsBoosterContext()).buildToolTip,
                                           'complex': None},
 TOOLTIPS_CONSTANTS.FREE_SHEET: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                 'method': personal_missions.FreeSheetTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                 'complex': None},
 TOOLTIPS_CONSTANTS.FREE_SHEET_RETURN: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                        'method': personal_missions.FreeSheetReturnTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                        'complex': None},
 TOOLTIPS_CONSTANTS.FREE_SHEET_NOT_ENOUGH: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                            'method': personal_missions.FreeSheetNotEnoughTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.FREE_SHEET_USED: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                      'method': personal_missions.FreeSheetUsedTooltip(contexts.ToolTipContext(None)).buildToolTip,
                                      'complex': None},
 TOOLTIPS_CONSTANTS.BADGE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                            'method': personal_missions.BadgeTooltipData(contexts.ToolTipContext(None)).buildToolTip,
                            'complex': None},
 TOOLTIPS_CONSTANTS.OPERATION: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                'method': personal_missions.OperationTooltipData(contexts.PersonalMissionOperationContext()).buildToolTip,
                                'complex': None},
 TOOLTIPS_CONSTANTS.PERSONAL_MISSION_INFO: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                            'method': personal_missions.PersonalMissionInfoTooltipData(contexts.ToolTipContext(None)).buildToolTip,
                                            'complex': None},
 TOOLTIPS_CONSTANTS.PERSONAL_MISSIONS_MAP_REGION: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                   'method': personal_missions.PersonalMissionsMapRegionTooltipData(contexts.PersonalMissionContext()).buildToolTip,
                                                   'complex': None},
 TOOLTIPS_CONSTANTS.EVENT_BOARDS_BADGE: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                         'method': elen.BadgeTooltipData(contexts.ToolTipContext(None)).buildToolTip,
                                         'complex': None},
 TOOLTIPS_CONSTANTS.EVENT_BOARDS_BADGES_GROUP: {'tooltip': TOOLTIPS_CONSTANTS.BLOCKS_DEFAULT_UI,
                                                'method': elen.BabgesGroupTooltipData(contexts.QuestContext()).buildToolTip,
                                                'complex': None}}
