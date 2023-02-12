#!/usr/bin/env python3
#----------------------------------------------------------#
import ssl
from uuid import uuid4
from datetime import datetime
import sys
from argparse import ArgumentParser
from aiohttp import ClientSession,TCPConnector
#----------------------------------------------------------#
#@similardisaster@wearehackerone.com
#----------------------------------------------------------#
uuid = uuid4()
#----------------------------------------------------------#
def startup():
    if sys.version_info.major > 2 and sys.version_info.minor > 6:
        print(f'[ACTIVE] UUID: {uuid}')
        print(f'[ACTIVE] {datetime.now()}')
    else:
        print(f'[ERROR] PYTHON 3.7x REQUIRED {uuid}')
        print(f'[ERROR] {datetime.now()}')
        sys.exit()
#----------------------------------------------------------#
async def module(*modules):
    ssl._create_default_https_context = ssl._create_unverified_context
    parser = ArgumentParser()
    parser.add_argument('-t')
    t = parser.parse_args().t
    if t:
        async with ClientSession() as session:
            targets = [url for url in open(t)]
            for target in targets:
                for module in modules:
                    await module(target,session)
    else:
        async with ClientSession() as session:
            targets = [url for url in open('/Users/similar/Desktop/echo/core/log.txt')]
            for target in targets:
                for module in modules:
                    await module(target,session)
#----------------------------------------------------------#
def shutdown():
    print(f'[DEAD] UUID: {uuid}')
    print(f'[DEAD] {datetime.now()}')
    sys.exit()
#----------------------------------------------------------#
