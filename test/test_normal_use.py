import nose.tools as ns
import os.path as op
import os
import sys
import time
from multiprocessing import Process
import signal

wkspace_root = op.normpath(op.join(__file__, '../../../'))
sys.path.insert(0, op.join(wkspace_root, 'datacube'))

import src.datacube.dataserver.run_server as serv
from test.datacube_test_harness.logfile_handler import LogTestHandler
from test.datacube_test_harness.test_harness import DatacubeTestHarness

from DQTools.dataset import Dataset

# TODO this is the starter class for proper tests of DQTools in normal use

class TestDQToolNormalUse(object):
    keyfile = None

    @classmethod
    def setup_class(cls):
        # Set up the test harness - this will use the test system settings
        # i.e. a prise_test database on localhost
        cls.dth = DatacubeTestHarness()
        # Create a clean test database
        cls.dth.rebuild_database(cls.dth.get_test_config_yaml(), level='full')
        # Put the dummy product and its sub-products into the database
        cls.dth.load_test_data(dataset='dummy')
        # Add a load of test users
        cls.dth.load_test_users()

        cls.log_helper = LogTestHandler(
                op.abspath(op.join(op.dirname(__file__),
                                   "../connect/log/logging_config.yml")))
        # back up the original file, load, alter and write back out
        cls.log_helper.setup_test_logging('Test_DQTools_NormalUse')

        # Set up a test server
        # =================================================================== #
        # comment out the following four lines to allow independent
        # server start, also edit teardown_class() and run_server.py
        p = Process(target=cls.start_server)
        p.start()
        cls.server_pid = p.pid
        time.sleep(2)   # Allow server to start up
        # =================================================================== #

        # Our tests will need a full permission keyfile
        cls.keyfile = op.abspath(op.join(
                wkspace_root, "datacube/test/http_tests/.assimila_dq"))

    @classmethod
    def start_server(cls):
        # Start server on localhost
        serv.run(test=True)

    @classmethod
    def teardown_class(cls):
        """This method is run once for each class _after_ all tests are run"""
        # =================================================================== #
        # comment out the following line to allow independent server stop.
        os.kill(cls.server_pid, signal.SIGTERM)
        # =================================================================== #

        # Reinstate the logging config file
        cls.log_helper.teardown_test_logging()

        # Remove the DQ_TESTS environment variable
        cls.dth = None

    def test_retrieve_dataset(self):
        d = Dataset('dummy_product', 'subdummy1')
        expected_tiles = ['dummy_east', 'dummy_west']
        ns.assert_list_equal(expected_tiles.sort(),
                             d.all_subproduct_tiles.sort())
        ns.assert_equal('1D',
                        d.time_resolution)
