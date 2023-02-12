#!/usr/bin/env python3
#----------------------------------------------------------#
from core.core import startup,module,shutdown
import asyncio
from modules.interact import interact
#----------------------------------------------------------#
#@similardisaster@wearehackerone.com
#----------------------------------------------------------#
startup()
#----------------------------------------------------------#
asyncio.run(module(interact))
#----------------------------------------------------------#
shutdown()
#----------------------------------------------------------#  
