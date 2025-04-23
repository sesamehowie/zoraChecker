import json
from itertools import cycle
from config import ZORA_ALLOCATION_CA
from src.utils.sleep.sleep import random_sleep
from src.utils.csv.csv_tools import write_csv
from src.utils.txt.txt_tools import read_txt
from src.network.network import Base
from src.contract.contract_interface import ContractInterface


WALLETS = read_txt("data/wallets.txt")
PROXIES = read_txt("data/proxies.txt")
CA = ZORA_ALLOCATION_CA
RETRIES = 3
ABI = json.load(open("src/contract/abi/ZoraToken.json"))


def get_results() -> list:
    results = []

    proxy_cycle = cycle(PROXIES)

    for wallet in WALLETS:
        proxy = next(proxy_cycle)

        contract_interface = ContractInterface(
            wallet_address=wallet,
            network=Base,
            proxy=proxy,
            contract_address=CA,
            abi=ABI,
        )

        data_item = [wallet]
        for attempt in range(RETRIES):
            try:
                allocation = contract_interface.check_allocation()
                if isinstance(allocation, float):
                    data_item.append(allocation)
                    break
            except Exception as e:
                print(f"Attempt {attempt+1}/{RETRIES}, error: {str(e)}")
                if "HTTPSConnectionPool" in str(e):
                    random_sleep(2)
                else:
                    random_sleep(1)

        if len(data_item) != 2:
            data_item.append(0)

        results.append(data_item)

        random_sleep(1)

    return results


def main():
    results = get_results()
    write_csv("data/results.csv", results, ["address", "$ZORA allocation"])


if __name__ == "__main__":
    main()
