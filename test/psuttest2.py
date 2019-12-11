import unittest
from demooops.pssshclient import CustomSSHClient


class TestCaseToTestSSHClient(unittest.TestCase):
    # fixtures setup, teardown
    def setUp(self):
        self.ssh = CustomSSHClient('localhost', 22, 'training', 'training')
        print('setting up...')

    def tearDown(self):
        print('clean-up')
        del self.ssh

    def test_ssh_client(self):
        op = self.ssh.check_output('whoami')
        self.assertIn('training', op, 'ssh client failed')

    def test_ssh_client_2(self):
        op = self.ssh.check_output('whoami')
        self.assertEqual('training', op.strip(), 'ssh client failed_2')


if __name__ == '__main__':
    unittest.main()
