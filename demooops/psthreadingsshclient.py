import threading
import logging
import pyexcel
from time import sleep
from demooops.pssshclient import CustomSSHClient

target_file = 'sshresponse.log'
logging.basicConfig(format='%(threadName)s : %(message)s')


class ThreadedSSHClient(CustomSSHClient):
    lock = threading.Lock()  # class variable, sync using lock

    def __init__(self, host, port, user, pwd, job):
        super().__init__(host, port, user, pwd)
        self.job = job
        self.t_name = threading.current_thread().name
        self.task_runner()

    def task_runner(self):
        payload = self.check_output(self.job)
        caption = f'{self.t_name} ran {self.job} @ {self.host}'

        logging.warning('waits for the lock')

        with ThreadedSSHClient.lock:
            logging.warning('acquired the lock')

            with open(target_file, 'a') as fw:
                """critical section"""
                fw.write(caption.center(80, '-') + '\n')
                fw.write(payload + '\n')
                logging.warning('done with the critical section')
            sleep(1)
            logging.warning('release the lock')


def parse_shreadsheet():
    """generator"""
    sheet = pyexcel.get_sheet(file_name='hosts.xlsx')

    for row in sheet:
        yield row


def main():
    for ssh_host in parse_shreadsheet():
        t = threading.Thread(target=ThreadedSSHClient, args=ssh_host)
        t.start()


if __name__ == '__main__':
    main()
