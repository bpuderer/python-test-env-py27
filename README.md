# python_test_env

Just a lightweight functional test environment utilizing [nose](https://github.com/nose-devs/nose), unittest, logging and ConfigParser.

Not much to it really...

Test cases are added to *tests* and extend BaseTestCase from framework.testbase.  Test utilities are added to *utils*.

Settings are defined in *framework/test_settings.cfg* and are accessible as a dictionary from the *settings* class variable.  The case-sensitive section name is specified as an argument to *run_tests.py*.

Test cases log to *log/test.log* using the *log* class variable.  Logging is configured using *framework/logging.cfg* and by default sets a log level of DEBUG and auto-rotates (5) 1 MB files.  Timestamps are in local time.

    2016-04-29 20:22:43,200 - test_example.test_str_ends_in_r - INFO - executing ExampleTestCase.test_str_ends_in_r

The *run_tests.py* script wraps nose, sets PYTHONPATH, sets PY_TEST_ENV to the section name in *framework/test_settings.cfg* to be used by *config.py* and can optionally create a simple html test summary report, *results.html* which renders fine in [lynx](http://lynx.invisible-island.net/).  Reports (*nosetests.xml* and *results.html*) are located in *reports*.

    $ python run_tests.py
    $ python run_tests.py --testenv sim2_settings
    $ python run_tests.py --testenv sim2_settings --xml_out
    $ python run_tests.py --testenv sim2_settings --html_out --tests tests/test_example.py tests.test_example:ExampleTestCase.test_str_ends_in_r
    $ python run_tests.py --help
    
