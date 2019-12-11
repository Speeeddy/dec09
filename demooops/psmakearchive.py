from zipfile import ZipFile
from glob import glob


class MarkArchive:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def save(self, *args):
        with ZipFile(self.archive_name, mode='w') as zf:
            for file_name in args:
                zf.write(file_name)
                print(f'{file_name}: added')


if __name__ == '__main__':
    archive = MarkArchive('src.zip')
    archive.save(*glob('../*.py'))