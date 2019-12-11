"""inheritance"""

from demooops.psdirlisting import DirectoryListing
from json import dump


class DirectoryListing2JSON(DirectoryListing):
    def to_json(self, json_file):
        try:
            with open(json_file, 'w') as fw:
                dump(self.container, fw, indent=2)

        except (FileNotFoundError, IOError) as err:
            print(err)


if __name__ == '__main__':
    DirectoryListing2JSON(r'/tmp', r'/home/ravijaya', '/home/ravijaya/Downloads').to_json('tmp.json')
