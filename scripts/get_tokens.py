from ape import accounts, networks, project
from rich.console import Console

from scripts.helper import Helper

console = Console()


def drip():
    helper: Helper = Helper()
    # ex. ethereum sepolia
    network_name: str = networks.provider.network.ecosystem.name + " " + networks.provider.network.name
    router_address: str = helper.get_ccip_bnm_address(network_name)
    # console.print(router_address)
    bnm_contract = project.ICCIPBNM.at(router_address)
    user = accounts.load("ctf")
    user.set_autosign(True)

    bnm_contract.drip(user.address, sender=user)


# need for ape
def main():
    networks_list = [
        ":sepolia",  # working
        "optimism:sepolia:alchemy",  # working
        "polygon:amoy:alchemy",
        "base:sepolia:alchemy",  # working
        "avalanche:fuji:node",  # working
        "arbitrum:sepolia:infura",  # working
    ]
    for ntwrk in networks_list:
        with networks.parse_network_choice(ntwrk, disconnect_after=True) as provider:
            # console.print(provider)
            try:
                # you can add a for loop to drip any number of tokens you want
                drip()
            except:
                pass
    # drip()


if __name__ == "__main__":
    main()
