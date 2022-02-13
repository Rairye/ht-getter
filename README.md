# ht-getter
Searches a document for hash tags. Supports multiple natural languages. Works in various contexts.

## Functions

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

## Notes
