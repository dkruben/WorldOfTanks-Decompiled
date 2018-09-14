# Python bytecode 2.7 (decompiled from Python 2.7)
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/FortBattleResultsWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class FortBattleResultsWindowMeta(AbstractWindowView):
    """
    DO NOT MODIFY!
    Generated with yaml.
    __author__ = 'yaml_processor'
    @extends AbstractWindowView
    null
    """

    def getMoreInfo(self, battleID):
        """
        :param battleID:
        :return :
        """
        self._printOverrideError('getMoreInfo')

    def getClanEmblem(self):
        """
        :return :
        """
        self._printOverrideError('getClanEmblem')

    def as_setDataS(self, data):
        """
        :param data:
        :return :
        """
        return self.flashObject.as_setData(data) if self._isDAAPIInited() else None

    def as_notAvailableInfoS(self, battleID):
        """
        :param battleID:
        :return :
        """
        return self.flashObject.as_notAvailableInfo(battleID) if self._isDAAPIInited() else None

    def as_setClanEmblemS(self, iconTag):
        """
        :param iconTag:
        :return :
        """
        return self.flashObject.as_setClanEmblem(iconTag) if self._isDAAPIInited() else None