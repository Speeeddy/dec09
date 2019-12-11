from demooops.pssshclient import CustomSSHClient
from demooops.psmakearchive import MarkArchive, glob


class SFTPClient(CustomSSHClient):
    def __init__(self, host, port, user, pwd):
        super().__init__(host, port, user, pwd)  # invoke base class __init__
        self.sftp = self.ssh.open_sftp()

    def upload(self, src, dest):
        self.sftp.put(src, dest)
        print(f'{src} uploaded as {dest}')

    def __del__(self):
        self.sftp.close()
        super().__del__()  # invoke overridden method


if __name__ == '__main__':
    archive_name = 'samples.zip'
    MarkArchive(archive_name).save(*glob('../*.py'))
    ftp = SFTPClient('13.233.155.234', 22, 'training', 'training')
    ftp.upload(archive_name, 'source.zip')
