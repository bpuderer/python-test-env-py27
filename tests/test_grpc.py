"""Demo basics of using test environment"""

import grpc

from framework.config import settings
from framework.testbase import BaseTestCase
from services.doubler.doubler_pb2_grpc import DoublerStub
from services.doubler.doubler_pb2 import Number
from utils.builders.number_builder import build_number, build_number_from_file


class ExampleGrpcTestCase(BaseTestCase):
    """Demo basics of using test environment. Tests use server from grpc-demo/doubler"""

    @classmethod
    def setUpClass(cls):
        """test class setup"""
        cls._channel = grpc.insecure_channel(settings["grpc_server"])
        cls._stub = DoublerStub(cls._channel)

    def test_grpc_call1(self):
        """grpc call test1"""
        number = Number(value=3.0)
        response = self._stub.Double(number)
        self.assertEqual(response.value, 6.0)

    def test_grpc_call2(self):
        """grpc call test2"""
        response = self._stub.Double(build_number(-4.0))
        self.assertEqual(response.value, -8.0)

    def test_grpc_call3(self):
        """grpc call test3"""
        response = self._stub.Double(build_number_from_file("resources/requests/doubler/request1.json"))
        self.assertEqual(response.value, 10.0)
