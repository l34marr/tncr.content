# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import tncr.content


class TncrContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=tncr.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'tncr.content:default')


TNCR_CONTENT_FIXTURE = TncrContentLayer()


TNCR_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(TNCR_CONTENT_FIXTURE,),
    name='TncrContentLayer:IntegrationTesting'
)


TNCR_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(TNCR_CONTENT_FIXTURE,),
    name='TncrContentLayer:FunctionalTesting'
)


TNCR_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        TNCR_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='TncrContentLayer:AcceptanceTesting'
)
