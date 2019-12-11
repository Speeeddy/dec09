"""single thread ssh client"""
import paramiko


class CustomSSHClient:
    def __init__(self, host, port, user, pwd):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.host, self.port, self.user, self.pwd)

    def check_output(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        output = stdout.read()
        response = output if output else stderr.read()
        return response.decode()

    def __del__(self):
        self.ssh.close()


if __name__ == '__main__':
    from sys import argv
    print(argv)
    # host, port, user, pwd, job = argv[1:]
    # '13.233.155.234', 22, 'training', 'training'
    ssh = CustomSSHClient(*argv[1:-1])
    op = ssh.check_output(argv[-1])
    print(op)
