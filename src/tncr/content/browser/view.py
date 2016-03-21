from Products.Five import BrowserView
from plone.app.contenttypes.interfaces import IImage
from plone.memoize.view import memoize
import random


class MyView(BrowserView):

    def __init__(self, context, request):
        super(MyView, self).__init__(context, request)

    def results(self, **kwargs):
        """Return a content listing based result set with contents of the
        folder.
        """
        results = self.context.restrictedTraverse('@@folderListing')(**kwargs)
        return results

    @property
    @memoize
    def images_within(self):
        """Get All Images within This Folder.
        """
        images = self.results(
            batch=False,
            object_provides=IImage.__identifier__
        )
        return images

    @property
    def random_image(self):
        """Get Random Image from This Folder.
        """
        img = None
        images = self.images_within
        if images:
            img = random.choice(images)
        return img

