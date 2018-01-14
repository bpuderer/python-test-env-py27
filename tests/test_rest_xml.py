import httplib
import logging
import xml.etree.ElementTree as ET

import requests

from framework.config import settings
from framework.testbase import BaseTestCase


log = logging.getLogger(__name__)

class RestXmlExample(BaseTestCase):

    @staticmethod
    def send_xml(filename):
        with open(filename) as f:
            data = f.read()
        headers = {"Content-Type": "txt/xml"}
        return requests.post(settings["echoxml_url"], data=data, headers=headers, timeout=5)


    def test_xml(self):
        """xml test using echoxml uri on httpsim.py in python-test"""

        r = self.send_xml("resources/requests/echoxml/request1.xml")
        self.assertEqual(r.status_code, httplib.OK)
        log.debug("Received: " + r.text)

        root = ET.fromstring(r.text)
        b_elements = root.iterfind('b')
        b_vals = [b.text for b in b_elements]

        self.assertItemsEqual(b_vals, ["b val 2", "b val 1"])
