import aiohttp
import json
import asyncio

"""
    Reference link for this codebase:
    https://www.pythontutorial.net/python-concurrency/python-asyncio-gather/
    
"""

class Receiver:
    def __init__(self, sensor_url, request_period):
        self.sensor_url = sensor_url
        self.request_period = request_period
    
    def _set_online_status(self, is_online):
        if is_online:
            print("|-----------------------------------------------------------------------|")
            print("| " + self.sensor_url + " is online")
        else:
            print(self.sensor_url + " is offline")
            print("|-----------------------------------------------------------------------|")
    
    async def receive(self):
        """ Periodically pull sensor data from aircraftlist.json """

        remote_sensor_url = "http://" + self.sensor_url + "/aircraftlist.json"

        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(5)) as session:
            while True:
                try:
                    async with session.get(remote_sensor_url) as response:
                        if response.status == 200:
                            self._set_online_status(True)
                            data_json = json.loads(await response.text())
                            # check that response is in fact json
                            for line in data_json:
                                yield line
                        else:
                            self._set_online_status(False)
                except TimeoutError:
                    self._set_online_status(False)
                await asyncio.sleep(self.request_period)

    async def process(self):
        """Get and process incoming JSON"""
        async for line in self.receive():
            print(f"|CALL SIGN {line['fli']} ------ LAT {line['lat']} ------ LON {line['lon']}")

async def main():
    """Instantiate receiver and run forever"""
    dhaka = Receiver("192.168.30.27", 1)
    chittagong = Receiver("192.168.101.3", 1)
    await asyncio.gather(dhaka.process(),chittagong.process())
    # asyncio.run(dhaka.process())

if __name__ == "__main__":
    asyncio.run(main())
