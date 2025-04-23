import time
import random


def random_sleep(mode: int) -> None:
    match mode:
        case 1:
            t = random.randint(2, 5)
        case 2:
            t = random.randint(10, 15)
        case _:
            t = 1

    print(f"Sleeping for {t} seconds")
    time.sleep(t)
