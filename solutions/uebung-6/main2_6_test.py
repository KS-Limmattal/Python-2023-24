#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main2 import teilbuch

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert teilbuch(
        {"key1": "val1", "key2": "val2", "key3": "val3"}, ["key1", "key2"]
    ) == {"key1": "val1", "key2": "val2"}
    assert teilbuch({"a": 1, "b": 5, "c": 2, "d": 11}, ["a", "b", "d", "e"]) == {
        "a": 1,
        "b": 5,
        "d": 11,
    }
    assert teilbuch({"a": 1, "b": 5, "c": 2, "d": 11}, ["c"]) == {"c": 2}
    assert teilbuch({"a": 1, "b": 5, "c": 2}, ["e", "a", 2]) == {"a": 1}
    assert teilbuch({"a": 3, "b": 5, "c": 2}, ["x", "y", "z", 3, 5, 2]) == {}
    assert teilbuch({}, ["a", "b"]) == {}
    assert teilbuch({"a": 1, "b": 2, "c": 3}, []) == {}
