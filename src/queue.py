import asyncio
import random 
import time

"""
    Reference link for this codebase:
    https://docs.python.org/3/library/asyncio-queue.html
    
"""


async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'{name} has slept for {sleep_for:.2f} seconds')


async def main():
    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(20):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())



"""
The queue.task_done() call is crucial for asyncio.Queue to correctly track when items are taken out of the queue and processed. 
When you comment out queue.task_done(), you prevent the queue from being notified that a task has been processed, which can lead to incorrect behavior and potentially a deadlock.

In your case, when you comment out queue.task_done(), the workers keep processing tasks from the queue, but since the queue is 
never marked as done for any of the items, await queue.join() in the main() function never completes. This causes the program to be stuck at that point, and the subsequent code (the print statements) is never executed.

If you need to modify your code to handle situations where queue.task_done() is not called, you must ensure that the queue is
 marked as done in some other way. However, this may require changing the overall logic of your program to ensure proper handling 
 of tasks and their completion. In general, it's recommended to keep queue.task_done() in place to maintain the correct behavior of asyncio.Queue.
"""