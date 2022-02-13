# ht-getter
Searches a document for hash tags. Supports multiple natural languages. Works in various contexts.

This package uses a non-regex approach and supports both halfwidth and fullwidth alphanumeric characters as well as various writing systems.

## Function

### def get_hash_tags(source, mode = "strings")

**Arguments:**

source -> The source text to be searched. Must be passed as a str type.

mode -> Specifies the mode of the results. The default value is “strings”

mode = “strings” -> The results are returned as a list of strings

mode = “indices” -> The results are returned as a list of lists of the start and end indices of the hash tags.

## Code Sample

```python
from ht_getter.getter import get_hash_tags

source_text = '''This simple package helps find you find #hash_tags in various types of #documents#. It also works with other languages like #日本語 or #한국어.
It supports #ｆｕｌｌｗｉｄｔｈ #alpha-numeric characters. You can get a #list of the #hash_tags or a list of their #indices in the #####source_text."
'''

hash_tags = get_hash_tags(source_text)
hash_tag_indices = get_hash_tags(source_text, mode = "indices")

print(hash_tags)
print(hash_tag_indices)

```

## Things to Keep in Mind:

1.	This package can be used in various contexts. (Social media posts, news articles, etc.)
2.	This package looks for substrings that have the structure of a hash tag but does not check that the substring is a valid hash tag on any platform. 

