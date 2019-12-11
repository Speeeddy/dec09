import unittest
from demooops.pssshclient import CustomSSHClient


def power(x, n):
    return x ** n


class TestCaseToTestSSHClient(unittest.TestCase):
    def test_ssh_client(self):
        ssh = CustomSSHClient('localhost', 22, 'training', 'training')
        op = ssh.check_output('free -m')
        self.assertIn('training', op, 'ssh client failed')

        #assert 'training' in op, "failed to run"


class CustomTestCase(unittest.TestCase):
    def test_power(self):
        result = power(2, 3)
        self.assertEqual(result, 8)

    def test_failure(self):
        result = power(2, 3)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
