from zope.interface import implementer
from plone.dexterity.content import Item

from tncr.content.interfaces import IMonument


@implementer(IMonument)
class Monument(Item):
    """Item Subclass for Monument
    """

