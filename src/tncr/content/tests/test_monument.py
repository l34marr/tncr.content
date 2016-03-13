# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from tncr.content.testing import TNCR_CONTENT_INTEGRATION_TESTING  # noqa
from tncr.content.interfaces import IMonument

import unittest2 as unittest


class MonumentIntegrationTest(unittest.TestCase):

    layer = TNCR_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Monument')
        schema = fti.lookupSchema()
        self.assertEqual(IMonument, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Monument')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Monument')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IMonument.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Monument', 'Monument')
        self.assertTrue(
            IMonument.providedBy(self.portal['Monument'])
        )
