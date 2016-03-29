from zope.interface import implementer
from plone.dexterity.content import Container
from Products.CMFCore.utils import getToolByName

from tncr.content.interfaces import IMonument
from tncr.content.interfaces import IRelic


@implementer(IMonument)
class Monument(Container):
    """Container Subclass for Monument
    """

@implementer(IRelic)
class Relic(Container):
    """Container Subclass for Relic
    """

