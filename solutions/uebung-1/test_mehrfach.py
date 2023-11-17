#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import main

"""
Diese Datei soll nur durch die Lehrperson abgeändert werden!
Sie dient zum automatisierten Testen.
"""

def test():
  assert main.mehrfach("Roland") == False
  assert main.mehrfach("Simon") == False
  assert main.mehrfach("Lara") == True
  assert main.mehrfach("Christopherus") == True
  assert main.mehrfach("Margrit") == True
  assert main.mehrfach("Susi") == True
