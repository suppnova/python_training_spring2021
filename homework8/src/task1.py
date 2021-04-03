"""
Homework 1:
============
We have a file that works as key-value storage, each like is represented as key and value separated by = symbol, example:

name=kek
last_name=top
song_name=shadilay
power=9001

Values can be strings or integer numbers. If a value can be treated both as a number and a string, it is treated as number.

Write a wrapper class for this key value storage that works like this:

storage = KeyValueStorage('path_to_file.txt')
that has its keys and values accessible as collection items and as attributes.
Example:
storage['name']  # will be string 'kek'
storage.song_name  # will be 'shadilay'
storage.power  # will be integer 9001

In case of attribute clash existing built-in attributes take precedence.
In case when value cannot be assigned to an attribute (for example when there's a line `1=something`) ValueError should be raised.
File size is expected to be small, you are permitted to read it entirely into memory.
"""
from string import ascii_letters


class KeyValueStorage(dict):
    def __init__(self, filepath):
        d = {}
        with open(filepath) as fi:
            for pair in fi.read().splitlines():
                key, value = pair.split("=")
                if key[0] not in ascii_letters:
                    raise ValueError(
                        f"value can't be assigned to an attribute in line: {pair}"
                    )
                d[key] = int(value) if value.isdigit() else value
        super().__init__(d)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)
