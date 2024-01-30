import asyncio
import json
import aiohttp
import mysql.connector

# class AircraftListProcessor:
#     def __init__(self, sensor_name, sensor_url):
#         self.sensor_name = sensor_name
#         self.sensor_url = sensor_url
#         self.aircraft_list = {}

#     async def fetch_data(self):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(self.sensor_url) as response:
#                 data = await response.json()
#                 return data

#     async def process_messages(self):
#         while True:
#             data = await self.fetch_data()
#             for json_msg in data:
#                 if self.aircraft_list.get(json_msg['hex_address']) != json_msg:
#                     self.aircraft_list[json_msg['hex_address']] = json_msg
#                     yield json_msg
#             await asyncio.sleep(1)  # Adjust the sleep interval as needed

# class StateUpdater:
#     def __init__(self):
#         self.aircraft_state = {}

#     async def update_state(self, sensor_stream):
#         async for update_state in sensor_stream:
#             current_state = self.aircraft_state.get(update_state['hex_address'], {})
#             if update_state['time_last_seen'] > current_state.get('time_last_seen', 0):
#                 # Update the database or perform other relevant actions
#                 await self.update_database(update_state)
#                 self.aircraft_state[update_state['hex_address']] = update_state

#     async def update_database(self, update_state):
#         # Update MySQL database with the new state information
#         connection = mysql.connector.connect(
#             host='your_db_host',
#             user='your_db_user',
#             password='your_db_password',
#             database='your_db_name'
#         )
#         cursor = connection.cursor()

#         # Example: Update AircraftState table
#         query = ("INSERT INTO AircraftState (hex_address, time_last_seen, squawk_code) "
#                  "VALUES (%s, %s, %s) "
#                  "ON DUPLICATE KEY UPDATE time_last_seen = VALUES(time_last_seen), squawk_code = VALUES(squawk_code)")
#         data = (update_state['hex_address'], update_state['time_last_seen'], update_state.get('squawk_code', ''))
#         cursor.execute(query, data)

#         connection.commit()
#         cursor.close()
#         connection.close()

# class DisplayManager:
#     async def display_update(self, trajectory_update_display):
#         while True:
#             position_update = await trajectory_update_display.get()
#             # Update the display or perform other relevant actions
#             print(f"Updating display for {position_update['hex_address']}")

# Example usage
async def main():
    # dhaka_processor = AircraftListProcessor(sensor_name="Dhaka", sensor_url="http://192.168.30.27/aircraftlist.json")
    # chatto_processor = AircraftListProcessor(sensor_name="Chatto", sensor_url="http://45.125.223.124/aircraftlist.json")

    # state_updater = StateUpdater()
    # display_manager = DisplayManager()

    # dhaka_stream = dhaka_processor.process_messages()
    # chatto_stream = chatto_processor.process_messages()

    # asyncio.create_task(state_updater.update_state(dhaka_stream))
    # asyncio.create_task(state_updater.update_state(chatto_stream))
    # asyncio.create_task(display_manager.display_update(trajectory_update_display))

    # # Run the event loop
    # await asyncio.sleep(10)  # Simulate a runtime
    # asyncio.gather(state_updater.update_state(dhaka_stream), state_updater.update_state(chatto_stream), return_exceptions=True)

    print("System is working fine")

if __name__ == "__main__":
    asyncio.run(main())