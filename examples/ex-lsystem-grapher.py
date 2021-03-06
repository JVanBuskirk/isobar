#!/usr/bin/env python

# example-lsystem-grapher:
# generates an l-system and its ASCII representation

from isobar import *

import logging
logging.basicConfig(level = logging.INFO, format = "[%(asctime)s] %(message)s")

import random
import time

seq = PLSys("N[+N+N]?N[-N]+N", depth = 3)
notes = seq.all()
note_min = min(notes)
note_max = max(notes)

for note in seq:
    note = note - note_min
    print("#" * note)
