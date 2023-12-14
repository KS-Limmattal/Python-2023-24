#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from main2 import schnittbuch

"""
Diese Datei darf nur durch die Lehrperson abgeändert werden!
Sie wird für automatische Tests der Lösungen verwendet.
"""


def test():
    assert schnittbuch(
        {"key1": "val1", "key2": "val2", "key3": "val3"},
        {"key1": "val2", "key2": "val1", "key3": "val3"},
    ) == {"key3": "val3"}
    assert schnittbuch(
        {"a": 1, "b": 5, "c": 2, "d": 11}, {"a": 1, "b": 5, "c": 2, "d": 11}
    ) == {"a": 1, "b": 5, "c": 2, "d": 11}
    assert schnittbuch(
        {"a": 1, "b": 5, "c": 2, "d": 11}, {"a": 1, "b": 2, "c": 3, "d": 11}
    ) == {"a": 1, "d": 11}
    assert schnittbuch({"a": 1, "b": 5, "c": 2}, {"a": 1, "b": 2, "c": 3}) == {"a": 1}
    assert schnittbuch({"a": 3, "b": 5, "c": 2}, {"a": 1, "b": 2, "c": 3}) == {}
    assert schnittbuch({}, {"a": 1, "b": 2, "c": 3}) == {}
    assert schnittbuch({"a": 1, "b": 2, "c": 3}, {}) == {}
    assert schnittbuch({}, {}) == {}
