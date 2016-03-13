# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s tncr.content -t test_monument.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src tncr.content.testing.TNCR_CONTENT_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot src/plonetraining/testing/tests/robot/test_monument.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Monument
  Given a logged-in site administrator
    and an add monument form
   When I type 'My Monument' into the title field
    and I submit the form
   Then a monument with the title 'My Monument' has been created

Scenario: As a site administrator I can view a Monument
  Given a logged-in site administrator
    and a monument 'My Monument'
   When I go to the monument view
   Then I can see the monument title 'My Monument'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add monument form
  Go To  ${PLONE_URL}/++add++Monument

a monument 'My Monument'
  Create content  type=Monument  id=my-monument  title=My Monument


# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.title  ${title}

I submit the form
  Click Button  Save

I go to the monument view
  Go To  ${PLONE_URL}/my-monument
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a monument with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the monument title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
