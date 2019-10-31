import re
from collections import Counter

words = open('words.txt').read().lower().split()
count = Counter(words).most_common(500)
print(count)