""" (C) Mahino Consulting Ltd 2024
    Author: T Hughes
    Purpose: Demonstrate asyncio techniques
"""

# Library modules
import asyncio

# Third party modules

# Local Modules


async def periodic_task(period: float):
    """Do something periodically. Period in seconds"""

    while True:
        # do something
        await asyncio.sleep(period)


async def print_hello_world_periodically(period: float):
    """Periodically print hello world"""

    while True:
        print("Hello World!")
        await asyncio.sleep(period)


def print_hello_world_every_second():
    """Use asyncio.run() to create and run a task"""
    asyncio.run(print_hello_world_periodically(1.0))


async def print_something_periodically(something: str, period: float):
    """Generalise the 'print something' task"""
    while True:
        print(something)
        await asyncio.sleep(period)


async def print_a_couple_of_things_at_different_rates():
    """Run two asyncio tasks"""

    await asyncio.gather(
        print_something_periodically("1 second", 1.0),
        print_something_periodically("0.6 second", 0.6),
    )


def two_task_demo():
    """Run two task demo"""
    asyncio.run(print_a_couple_of_things_at_different_rates())


if __name__ == "__main__":
    #    print_hello_world_every_second()
    two_task_demo()