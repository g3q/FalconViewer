import asyncio
import aiohttp
import time
import socket
from aiohttp import ClientSession
print(""" \33[97;1m   
   ___     _                        
  / __\_ _| | ___ ___  _ __/\   /(_) _____      _____ _ __ 
 / _\/ _` | |/ __/ _ \| '_ \ \ / / |/ _ \ \ /\ / / _ \ '__|
/ / | (_| | | (_| (_) | | | \ V /| |  __/\ V  V /  __/ |   
\/   \__,_|_|\___\___/|_| |_|\_/ |_|\___| \_/\_/ \___|_|   
                                                                                                     \33[95;1mCreator: ProponentHacker
                                                                                              \33[95;1mCredits: WeebSec Crew for 1 function.
                                                                                    \33[95;1mCheck out my Instagram: https://instagram.com/loctang
\33[91;1mFalconViewer is made to find the admin panel/control panel of a website.
This is for penetration testers ONLY and any illegal actions done with this software is not my responsibility. 
An update will be out with a credential bruteforce soon.
""")


target = input("\33[93;1mEnter The URL To Find The Admin Panel: \33[1;0m")
print("")
target = target.replace('https://', '')
target = target.replace('http://', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target
start = time.time()
yay = []

conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
        verify_ssl=False,
    ) 
async def fetch(url, session):
    async with session.get(url) as response: 
        status = response.status
        if status == 200:
            print("\33[97;1mSearching directories -->  \33[1;0m{}\33[97;1m {}".format(response.url, status))
            yay.append(response.url)
        elif status == 404:
            print("\33[91;1m\33[94;1m{}\33[91;1m DEAD {}".format(response.url, status))
        elif status == 403:
            print("\33[91;1m\33[94;1m{}\33[91;1m DEAD \33[95;1m{}".format(response.url, status))
        else:
            print("\33[95;1m??? {} ?/? {}".format(response.url, status))
        return await response.read()

async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('admin.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)
    async with ClientSession(connector=conn) as session: 
        for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = asyncio.gather(*tasks)
        await responses
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)
end = time.time()
script_time = end - start
print("\33[93;1mScan was completed in {} seconds.\n".format(script_time))
print("\33[91;1m \33[93;1mAdmin Panels: \33[91;1m\33[1;0m")
if len(yay) == 0:
    print("\33[94;1mNo Panels Found.")
else:
    for y in yay:
        print(y)
