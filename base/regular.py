import re

s1 = "Error 404. 10086. server controller k181"

# pattern = re.compile(r"\d+")
# matches = pattern.finditer(s1)

# for match in matches:
#   print(match.group())

print(re.findall("\d+", s1, re.IGNORECASE))
