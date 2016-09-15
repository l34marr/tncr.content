from zope.interface import implementer
from plone.dexterity.content import Container
from Products.CMFCore.utils import getToolByName

from tncr.content.interfaces import IMonument


@implementer(IMonument)
class Monument(Container):
    """Container Subclass for Monument
    """

#   def __init__(self, image=None):
#       self.image = image

    @property
    def image(self):
        catalog = getToolByName(self, 'portal_catalog')
        path = '/'.join(self.getPhysicalPath())
        brain = catalog(path={"query": path}, portal_type=['Image'])
        obj = brain[0].getObject()
        return obj.image

