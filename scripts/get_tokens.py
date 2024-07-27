from ape import project, networks, accounts
from scripts.helper import Helper


def drip():
    helper: Helper = Helper()
    # ethereum sepolia
    network_name: str = networks.provider.network.ecosystem.name + ' ' + networks.provider.network.name
    router_address: str = helper.get_ccip_bnm_address(network_name)
    print(router_address)
    bnm_contract = project.ICCIPBNM.at(router_address)
    user = accounts.load("ctf")
    user.set_autosign(True)

    bnm_contract.drip(user.address, sender=user)


# need for ape
def main():
    # you can add a for loop to drip any number of tokens you want
    drip()

if __name__ == "__main__":
    main()