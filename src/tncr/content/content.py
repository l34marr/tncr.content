from zope.interface import implementer
from plone.dexterity.content import Container
from plone.dexterity.content import Item

from tncr.content.interfaces import IMonument
from tncr.content.interfaces import IRelic
from tncr.content.interfaces import IRuin
from tncr.content.interfaces import ILandscape


@implementer(IMonument)
class Monument(Container):
    """Container Subclass for Monument
    """

@implementer(IRelic)
class Relic(Container):
    """Container Subclass for Relic
    """

@implementer(IRuin)
class Ruin(Container):
    """Container Subclass for Ruin
    """

@implementer(ILandscape)
class Landscape(Container):
    """Container Subclass for Landscape
    """

