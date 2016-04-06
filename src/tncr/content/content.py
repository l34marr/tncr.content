from zope.interface import implementer
from plone.dexterity.content import Container
from plone.dexterity.content import Item

from tncr.content.interfaces import IMonument
from tncr.content.interfaces import IRelic
from tncr.content.interfaces import IRuin
from tncr.content.interfaces import ILandscape
from tncr.content.interfaces import ISettlement
from tncr.content.interfaces import ITemple
from tncr.content.interfaces import IPhoto
from tncr.content.interfaces import IHouse


@implementer(IMonument)
class Monument(Container):
    """Container Subclass for Monument
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'

@implementer(IRelic)
class Relic(Container):
    """Container Subclass for Relic
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'

@implementer(IRuin)
class Ruin(Container):
    """Container Subclass for Ruin
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'


@implementer(ILandscape)
class Landscape(Container):
    """Container Subclass for Landscape
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'

@implementer(ISettlement)
class Settlement(Container):
    """Container Subclass for Settlement
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'

@implementer(ITemple)
class Temple(Container):
    """Container Subclass for Temple
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'

@implementer(IPhoto)
class Photo(Item):
    """Item Subclass for Photo
    """

@implementer(IHouse)
class House(Container):
    """Container Subclass for House
    """

    def dstrct(self):
        try:
            head = self.address.split(u'\u5340')[0]
            dstr = head.split(u'\u5e02', 1)[1]
        except:
            return 'Unknown'
        return dstr + u'\u5340'

