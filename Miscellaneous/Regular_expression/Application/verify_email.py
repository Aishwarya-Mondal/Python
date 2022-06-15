import re

email = "sk@aol.com md@.com @seo.com dc@.com"

ematch = re.findall("\w+@\w+.[A-Z | a-z]{3}",email)
print(ematch)