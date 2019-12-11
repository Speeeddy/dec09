"""unix like pipe"""

import subprocess

cat = subprocess.Popen(['cat', '/etc/passwd'], stdout=subprocess.PIPE)
cut = subprocess.Popen(['cut', '-f', '1', '-d', ':'], stdin=cat.stdout, stdout=subprocess.PIPE)
sort = subprocess.Popen(['sort'], stdin=cut.stdout, stdout=subprocess.PIPE)


for response in sort.communicate():
    if response:
        print(response.decode())
