#!/usr/bin/env python3
from pathlib import Path
import os
try:
    import traci
    import sumolib
    print('ok', traci.__version__, sumolib.__version__)
except Exception as e:
    print('err', e)
