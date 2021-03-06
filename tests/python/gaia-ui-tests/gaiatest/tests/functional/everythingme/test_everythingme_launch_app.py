# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from gaiatest import GaiaTestCase
from gaiatest.apps.homescreen.app import Homescreen


class TestEverythingMeLaunchApp(GaiaTestCase):

    def setUp(self):
        GaiaTestCase.setUp(self)
        # Force disable rocketbar
        self.data_layer.set_setting('rocketbar.enabled', False)
        self.apps.set_permission('Homescreen', 'geolocation', 'deny')
        self.connect_to_network()

    def test_launch_everything_me_app(self):
        app_name = 'Twitter'
        homescreen = Homescreen(self.marionette)
        self.apps.switch_to_displayed_app()
        homescreen.wait_for_homescreen_to_load()

        search_panel = homescreen.tap_search_bar()
        search_panel.wait_for_everything_me_loaded()
        search_panel.type_into_search_box(app_name)

        search_panel.wait_for_everything_me_results_to_load()

        self.assertGreater(len(search_panel.results), 0)

        search_panel.results[0].tap()
        self.assertIn(app_name, self.marionette.title)
