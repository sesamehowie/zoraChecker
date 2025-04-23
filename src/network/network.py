class Network:
    def __init__(
        self, name: str, rpc_list: list[str], native_token: str, chain_id: int
    ):
        self.name = name
        self.rpc_list = rpc_list
        self.native_token = native_token
        self.chain_id = chain_id


Base = Network(
    "Base", ["https://mainnet.base.org", "https://1rpc.io/base"], "ETH", 8453
)
