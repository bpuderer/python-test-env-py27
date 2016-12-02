"""Read test settings and init logger"""

import ConfigParser
import json
import logging
import logging.config
import os
import sys


logging.config.fileConfig('framework/logging.cfg')
log = logging.getLogger(__name__)

cp = ConfigParser.SafeConfigParser(allow_no_value=True)
cp.read('framework/test_settings.cfg')
test_env = os.getenv('PY_TEST_ENV', 'DEFAULT')
try:
    settings = dict(cp.items(test_env))
except ConfigParser.NoSectionError as e:
    print e
    print 'Test run aborted'
    sys.exit()

log.info('Loaded test settings for {}: {}'.format(test_env,
         json.dumps(settings, indent=4, sort_keys=True)))
