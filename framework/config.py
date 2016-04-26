"""Load logging and test settings"""

import ConfigParser
import json
import logging
import logging.config
import os


logging.config.fileConfig('framework/logging.cfg')
log = logging.getLogger(__name__)

cp = ConfigParser.SafeConfigParser(allow_no_value=True)
cp.read('framework/test_settings.cfg')
test_env = os.getenv('PY_TEST_ENV')
settings = dict(cp.items(test_env))

log.info('Loaded test settings for %s: %s', test_env, json.dumps(settings, indent=4, sort_keys=True))
