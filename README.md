# python_test_env

Just a lightweight functional test environment utilizing [nose](https://github.com/nose-devs/nose)/[nose2](https://github.com/nose-devs/nose2), unittest, logging and ConfigParser.

Not much to it really...

Test cases are added to *tests* and extend BaseTestCase from framework.testbase.  Test utilities are added to *utils*.

Settings are defined in *framework/test_settings.cfg* and are accessible as a dictionary from the *settings* class variable.  The case-sensitive section name is specified as an argument to *run_tests.py*.

Test cases log to *log/test.log* using the *log* class variable.  Logging is configured using *framework/logging.cfg* and by default sets a log level of DEBUG and auto-rotates (5) 1 MB files.  Timestamps are in local time.

    2016-04-29 20:22:43,200 - test_example.test_str_ends_in_r - INFO - executing ExampleTestCase.test_str_ends_in_r

Reports (*nosetests.xml*, *nose2-junit.xml* and *results.html*) are located in *reports* which is also a good place to store output from pylint (see Jenkins' [Violations plugin](https://wiki.jenkins-ci.org/display/JENKINS/Violations)) and coverage (see nose/nose2 coverage plugin and Jenkins [Cobertura plugin](https://wiki.jenkins-ci.org/display/JENKINS/Cobertura+Plugin)).

The resources directory is a place for various files needed by the tests.

The *run_tests.py* script wraps nose/nose2, sets PY_TEST_ENV environment variable to the section name in *framework/test_settings.cfg* to be used by *config.py* and can optionally create a simple html test summary report, *results.html* which renders fine in [lynx](http://lynx.invisible-island.net/).

    $ python run_tests.py
    $ python run_tests.py --testenv sim2_settings --nose2 --xml_out
    $ python run_tests.py --testenv sim2_settings -a tags=tag1 tags=tag3
    $ python run_tests.py --testenv sim2_settings --tests tests.test_example tests.test_example2
    $ python run_tests.py --help

#### Jenkins Integration

Manage Jenkins > Manage Plugins
* Git plugin
* Violations plugin
* Test Results Analyzer Plugin
* Cobertura Plugin
* Green Balls

New Item > Freestyle project

Source Code Management > Git > Repository URL

Build > Execute shell > Command

```
python run_tests.py --testenv sim2_settings --xml_out --nose2
nose2 --with-coverage --coverage utils --coverage-report xml tests.utils_tests
export PYTHONPATH='.'
pylint -f parseable utils tests | tee reports/pylint.out
```

Post-build Actions > Publish Cobertura Coverage Report > coverage.xml

Post-build Actions > Publish JUnit test result report > Test report XMLs > reports/nose2-junit.xml

Post-build Actions > Report Violations > pylint > reports/pylint.out

#### Links

[Nose documentation](http://nose.readthedocs.io/en/latest/index.html)

[Nose2 documentation](http://nose2.readthedocs.io/en/latest/index.html)

Great post from Steve Brettschneider titled [Automated python unit testing, code coverage and code quality analysis with Jenkins](http://bhfsteve.blogspot.com/2012/04/automated-python-unit-testing-code_27.html)

Alex Conrad's [Jenkins and Python](http://www.alexconrad.org/2011/10/jenkins-and-python.html) post
