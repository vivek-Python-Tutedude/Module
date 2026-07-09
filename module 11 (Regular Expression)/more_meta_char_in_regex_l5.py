# ^ :- caret  ==> This carat symbol is basicaly matches at the beginning of the string only
# which means it check the string start with some given pattern or not

import re
s1 = "Python is a programming language"

pat = r"^[a-z]{8}"
match_obj = re.search(pat, s1)
print(match_obj) # None

# $ dollor ==> it matches the end of the string

pat = r"[a-z]{8}$"
match_obj = re.search(pat, s1)
print(match_obj) # <re.Match object; span=(24, 32), match='language'>

# () :-  group == it check all the character is matches inside the ()
# difference ==> [com] == c|o|m    (com) == com              | == or

email = "abc_123@example.com random words and characters . xyz_098.abc.edu"
pat = r"(com)"
match_obj = re.search(pat, email)
print(match_obj) # <re.Match object; span=(16, 19), match='com'>