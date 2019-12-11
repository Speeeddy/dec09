import re
from pprint import pprint as pp

pattern = '^r'
matched_lines = [line for line in open('/etc/passwd') if re.search(pattern, line, re.I)]
pp(matched_lines)

