#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import main

"""
Diese Datei soll nur durch die Lehrperson abgeändert werden!
Sie dient zum automatisierten Testen.
"""

def test():
  assert main.gruesse("Roland") == "Hallo Roland"
  assert main.gruesse("Simon") == "Hallo Simon"
  assert main.gruesse("Lara") == "Hallo Lara"
  assert main.gruesse("Christopherus") == "Ach, dieser Name ist mir zu lang!"
  assert main.gruesse("Margrit") == "Ach, dieser Name ist mir zu lang!"
