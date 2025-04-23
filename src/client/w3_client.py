import random
import pyuseragents
from web3 import Web3
from ..network.network import Network


class EthClient:
    def __init__(self, wallet_address: str, network: Network, proxy: str | None):
        self.address = wallet_address
        self.network = network
        self.rpc = random.choice(self.network.rpc_list)
        self.proxy = proxy
        self.w3 = self.get_w3_client()

        print(
            f"Initialized client:\nWallet address: {self.address}\nNetwork: {network.name}\nProxy: {self.proxy}\n"
        )

    def get_w3_client(self) -> Web3:
        if self.proxy is not None:
            user_agent = pyuseragents.random()
            w3 = Web3(
                Web3.HTTPProvider(
                    endpoint_uri=self.rpc,
                    request_kwargs={
                        "proxies": {
                            "http": f"http://{self.proxy}",
                            "https": f"http://{self.proxy}",
                        },
                        "headers": {
                            "Content-Type": "application/json",
                            "User-Agent": user_agent,
                        },
                        "timeout": 30,
                    },
                )
            )
        else:
            w3 = Web3(
                Web3.HTTPProvider(endpoint_uri=self.rpc, request_kwargs={"timeout": 30})
            )

        return w3

    def get_contract(self, contract_address: str, abi: str | None):
        return self.w3.eth.contract(contract_address, abi=abi)
