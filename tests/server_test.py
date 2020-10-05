#!/usr/bin/env python3

import pytest
import sys

from xprocess import ProcessStarter

from xprocess_test import client


@pytest.fixture(scope="session", autouse=True)
def host_sim_server(xprocess):
    python_executable_full_path = sys.executable

    class Starter(ProcessStarter):
        pattern = "HostSim server running"
        args = [python_executable_full_path, '-m', 'xprocess_test.host_sim']

    logfile = xprocess.ensure("host_sim", Starter)  # noqa: F841
    yield
    xprocess.getinfo("host_sim").terminate()


@pytest.fixture(scope="class")
def client_connect(request):
    try:
        cl = client.Client('127.0.0.1')  # noqa: F841
        assert True
    except ConnectionRefusedError:
        raise AssertionError()

    request.cls.cl = cl
    yield

    del request.cls.cl
    assert True


@pytest.mark.usefixtures("client_connect")
class TestClient():
    def test_client_a(self):
        try:
            resp = self.cl.communicate(b"\x12\x34\x56")
            print(resp)
            assert True
        except ConnectionError:
            raise AssertionError()
