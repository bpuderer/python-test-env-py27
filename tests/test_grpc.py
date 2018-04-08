"""Demo using test environment for grpc testing"""

import logging

import grpc
from google.protobuf import json_format

from framework.config import settings
from framework.testbase import BaseTestCase
from services.doubler.doubler_pb2_grpc import DoublerStub
from services.doubler.doubler_pb2 import Number
from utils.builders.number_builder import build_number_from_file, build_number_from_dict

log = logging.getLogger(__name__)


class ExampleGrpcTestCase(BaseTestCase):
    """Tests use server from grpc-demo/doubler"""

    @classmethod
    def setUpClass(cls):
        """test class setup"""
        cls._channel = grpc.insecure_channel(settings["grpc_server"])
        cls._stub = DoublerStub(cls._channel)


    def test_grpc_call1(self):
        """grpc call test1"""
        response = self._stub.Double(build_number_from_file("resources/requests/doubler/request1.json"))
        log.debug("response: {}".format(json_format.MessageToJson(response)))
        self.assertEqual(response.value, 10.0)

    def test_grpc_call2(self):
        """grpc call test2"""
        d = {'value': -4.0}
        response = self._stub.Double(build_number_from_dict(d))
        self.assertEqual(response.value, -8.0)

    def test_grpc_call3(self):
        """grpc call test3"""
        number = Number(value=3.0)
        response = self._stub.Double(number)
        self.assertEqual(response.value, 6.0)
