import re

pattern = r'\b[5-9]\d\d\b|\b[1-9]\d{3,}\b'
matched_lines = filter(lambda line: re.search(pattern, line, re.I), open('/etc/passwd'))

m = map(lambda line: print(line, end=''), matched_lines)
list(m)
# print()

for match_line in matched_lines:
     print(match_line, end='')