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

    def dstrct_number(self, arg):
        """District to Number
        """
        switcher = {
            u'\u4e2d\u897f\u5340': '2', #westcentral
            u'\u5317\u5340': '3', #north'
            u'\u5357\u5340': '4', #south'
            u'\u6771\u5340': '5', #east'
            u'\u5b89\u5357\u5340': '6', #annan
            u'\u5b89\u5e73\u5340': '7', #anping
            u'\u897f\u6e2f\u5340': '8', #shigang
            u'\u95dc\u5edf\u5340': '9', #guanmiau
            u'\u5927\u5167\u5340': '10', #danei
            u'\u5b98\u7530\u5340': '11', #guantian
            u'\u6b78\u4ec1\u5340': '12', #guiren
            u'\u516d\u7532\u5340': '13', #lioujia
            u'\u6c38\u5eb7\u5340': '14', #yungkang
            u'\u6771\u5c71\u5340': '15', #dungshan
            u'\u9f8d\u5d0e\u5340': '16', #lungchi
            u'\u5f8c\u58c1\u5340': '17', #houbi
            u'\u67f3\u71df\u5340': '18', #liouying
            u'\u5b78\u7532\u5340': '19', #shiuejia
            u'\u5de6\u93ae\u5340': '20', #tzuojen
            u'\u5584\u5316\u5340': '21', #shanhua
            u'\u65b0\u5316\u5340': '22', #sinhua
            u'\u6960\u897f\u5340': '23', #nanshi
            u'\u5357\u5316\u5340': '24', #nanhua
            u'\u9ebb\u8c46\u5340': '25', #madou
            u'\u7389\u4e95\u5340': '26', #yujing
            u'\u767d\u6cb3\u5340': '27', #baihe
            u'\u5c71\u4e0a\u5340': '28', #shanshang
            u'\u5b89\u5b9a\u5340': '29', #anding
            u'\u65b0\u5e02\u5340': '30', #sinshr
            u'\u5317\u9580\u5340': '31', #beimen
            u'\u4f73\u91cc\u5340': '32', #jiali
            u'\u5c07\u8ecd\u5340': '33', #jiangjiun
            u'\u9e7d\u6c34\u5340': '34', #yanshuei
            u'\u4e03\u80a1\u5340': '35', #chigu
            u'\u65b0\u71df\u5340': '36', #shinying
            u'\u4ec1\u5fb7\u5340': '37', #rende
            u'\u4e0b\u71df\u5340': '38', #shiaying
        }
        return switcher.get(arg, '2')

