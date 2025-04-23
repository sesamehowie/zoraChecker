from ..client.w3_client import EthClient


class ContractInterface(EthClient):
    def __init__(self, wallet_address, network, proxy, contract_address, abi):
        super().__init__(wallet_address, network, proxy)

        self.contract = self.get_contract(contract_address=contract_address, abi=abi)

    def check_allocation(self):
        print(f"Checking allocation on Zora contract for address {self.address}")

        allocation = self.contract.functions.allocations(self.address).call()
        readable_amount = allocation / 10**18

        print(f"{self.address} | Total allocation: {readable_amount:.6f}")

        return readable_amount
