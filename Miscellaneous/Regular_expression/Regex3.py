# Generate an iterator

import re

str = "we need to inform him with the latest information"

# get starting an ending index of the matching object

# If the search is successful, the finditer() function returns an iterator yielding the Match objects.
# Otherwise, the finditer() also returns an iterator that will yield no Match object.
for i in re.finditer("inform",str):
    location_tuple = i.span()

    print(location_tuple)
# span() method returns a tuple containing starting and ending index of the matched string.
# If group did not contribute to the match it returns(-1,-1).