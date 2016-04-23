"""Load test and logging config"""

import ConfigParser
import json
import logging
import logging.config
import os


# setup logging
logging.config.fileConfig('framework/logging.cfg')
log = logging.getLogger(__name__)

# setup test config
cp = ConfigParser.SafeConfigParser(allow_no_value=True)
cp.read('framework/test.cfg')
test_env = os.getenv('PY_TEST_ENV')
props = dict(cp.items(test_env))

log.info('Loaded test config for %s: %s', test_env, json.dumps(props, indent=4, sort_keys=True))
