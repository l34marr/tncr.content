from zope.interface import implementer
from plone.dexterity.content import Container

from tncr.content.interfaces import IMonument


@implementer(IMonument)
class Monument(Container):
    """Item Subclass for Monument
    """

