""" ASL Systems Ltd 2024
    Author: Shuvo
    Purpose: Demonstrate asyncio techniques
"""

# Library modules
import asyncio
import json

# Third party modules
import aiohttp
# Local Modules

class Jetvision:


    def __init__(self, sensor_name, sensor_url):
        self.sensor_name = sensor_name
        self.sensor_url = sensor_url
        self.aircraft_list = {}
    
    
    async def fetch_data(self):
        """ To receive data from the sensor """
        async with aiohttp.ClientSession() as session:
                async with session.get(self.sensor_url) as response:
                    data = await response.json()
                    return data

    async def process(self):
        """ To process data """
        while True:
            data = await self.fetch_data()
            print("Previous Flight: "+str(len(self.aircraft_list)))
            print("Current Flight Stream: "+str(len(data)))
            numberOfUpdatedData = 0;

            for json_msg in data:
                if self.aircraft_list.get(json_msg['hex']) != json_msg:
                    self.aircraft_list[json_msg['hex']] = json_msg
                    numberOfUpdatedData = numberOfUpdatedData + 1
            print("Updated Data: "+str(numberOfUpdatedData))
            # print(self.aircraft_list)
            await asyncio.sleep(1)

if __name__ == "__main__":
    dhaka_sensor = "http://192.168.30.27/aircraftlist.json"
    dhaka = Jetvision("Dhaka",dhaka_sensor)
    asyncio.run(dhaka.process())