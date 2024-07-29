from enum import Enum


class SupportedNetworks(Enum):
    ETHEREUM_SEPOLIA = 0
    AVALANCHE_FUJI = 1
    ARBITRUM_SEPOLIA = 2
    POLYGON_AMOY = 3
    BNB_CHAIN_TESTNET = 4
    OPTIMISM_SEPOLIA = 5
    BASE_SEPOLIA = 6
    WEMIX_TESTNET = 7
    KROMA_SEPOLIA = 8
    GNOSIS_CHIADO = 9
    CELO_ALFAJORES = 10


class PayFeesIn(Enum):
    Native = 1
    LINK = 2


class Helper:
    def __init__(self):
        self.networks = {
            SupportedNetworks.ETHEREUM_SEPOLIA: "Ethereum Sepolia",
            SupportedNetworks.AVALANCHE_FUJI: "Avalanche Fuji",
            SupportedNetworks.ARBITRUM_SEPOLIA: "Arbitrum Sepolia",
            SupportedNetworks.POLYGON_AMOY: "Polygon Amoy",
            SupportedNetworks.BNB_CHAIN_TESTNET: "BNB Chain Testnet",
            SupportedNetworks.OPTIMISM_SEPOLIA: "Optimism Sepolia",
            SupportedNetworks.BASE_SEPOLIA: "Base Sepolia",
            SupportedNetworks.WEMIX_TESTNET: "Wemix Testnet",
            SupportedNetworks.KROMA_SEPOLIA: "Kroma Sepolia",
            SupportedNetworks.GNOSIS_CHIADO: "Gnosis Chiado",
            SupportedNetworks.CELO_ALFAJORES: "Celo Alfajores",
        }

        # * reverse a dict
        self.supportedNetworksMapping = {v: k for k, v in self.networks.items()}
        # self.supportedNetworksMapping = set(k.lower() for k in self.inv_map)

        # Chain IDs
        self.chain_ids = {
            SupportedNetworks.ETHEREUM_SEPOLIA: 16015286601757825753,
            SupportedNetworks.AVALANCHE_FUJI: 14767482510784806043,
            SupportedNetworks.ARBITRUM_SEPOLIA: 3478487238524512106,
            SupportedNetworks.POLYGON_AMOY: 16281711391670634445,
            SupportedNetworks.BNB_CHAIN_TESTNET: 13264668187771770619,
            SupportedNetworks.OPTIMISM_SEPOLIA: 5224473277236331295,
            SupportedNetworks.BASE_SEPOLIA: 10344971235874465080,
            SupportedNetworks.WEMIX_TESTNET: 9284632837123596123,
            SupportedNetworks.KROMA_SEPOLIA: 5990477251245693094,
            SupportedNetworks.GNOSIS_CHIADO: 8871595565390010547,
            SupportedNetworks.CELO_ALFAJORES: 3552045678561919002,
        }

        # Router addresses
        self.routers = {
            SupportedNetworks.ETHEREUM_SEPOLIA: "0x0BF3dE8c5D3e8A2B34D2BEeB17ABfCeBaf363A59",
            SupportedNetworks.AVALANCHE_FUJI: "0xF694E193200268f9a4868e4Aa017A0118C9a8177",
            SupportedNetworks.ARBITRUM_SEPOLIA: "0x2a9C5afB0d0e4BAb2BCdaE109EC4b0c4Be15a165",
            SupportedNetworks.POLYGON_AMOY: "0x9C32fCB86BF0f4a1A8921a9Fe46de3198bb884B2",
            SupportedNetworks.BNB_CHAIN_TESTNET: "0xE1053aE1857476f36A3C62580FF9b016E8EE8F6f",
            SupportedNetworks.OPTIMISM_SEPOLIA: "0x114A20A10b43D4115e5aeef7345a1A71d2a60C57",
            SupportedNetworks.BASE_SEPOLIA: "0xD3b06cEbF099CE7DA4AcCf578aaebFDBd6e88a93",
            SupportedNetworks.WEMIX_TESTNET: "0xA8C0c11bf64AF62CDCA6f93D3769B88BdD7cb93D",
            SupportedNetworks.KROMA_SEPOLIA: "0xA8C0c11bf64AF62CDCA6f93D3769B88BdD7cb93D",
            SupportedNetworks.GNOSIS_CHIADO: "0x19b1bac554111517831ACadc0FD119D23Bb14391",
            SupportedNetworks.CELO_ALFAJORES: "0xb00E95b773528E2Ea724DB06B75113F239D15Dca",
        }

        # Link addresses
        self.links = {
            SupportedNetworks.ETHEREUM_SEPOLIA: "0x779877A7B0D9E8603169DdbD7836e478b4624789",
            SupportedNetworks.AVALANCHE_FUJI: "0x0b9d5D9136855f6FEc3c0993feE6E9CE8a297846",
            SupportedNetworks.ARBITRUM_SEPOLIA: "0xb1D4538B4571d411F07960EF2838Ce337FE1E80E",
            SupportedNetworks.POLYGON_AMOY: "0x0Fd9e8d3aF1aaee056EB9e802c3A762a667b1904",
            SupportedNetworks.BNB_CHAIN_TESTNET: "0x84b9B910527Ad5C03A9Ca831909E21e236EA7b06",
            SupportedNetworks.OPTIMISM_SEPOLIA: "0xE4aB69C077896252FAFBD49EFD26B5D171A32410",
            SupportedNetworks.BASE_SEPOLIA: "0xE4aB69C077896252FAFBD49EFD26B5D171A32410",
            SupportedNetworks.WEMIX_TESTNET: "0x3580c7A817cCD41f7e02143BFa411D4EeAE78093",
            SupportedNetworks.KROMA_SEPOLIA: "0xa75cCA5b404ec6F4BB6EC4853D177FE7057085c8",
            SupportedNetworks.GNOSIS_CHIADO: "0xDCA67FD8324990792C0bfaE95903B8A64097754F",
            SupportedNetworks.CELO_ALFAJORES: "0x32E08557B14FaD8908025619797221281D439071",
        }

        # Wrapped native addresses
        self.wrapped_natives = {
            SupportedNetworks.ETHEREUM_SEPOLIA: "0x097D90c9d3E0B50Ca60e1ae45F6A81010f9FB534",
            SupportedNetworks.AVALANCHE_FUJI: "0xd00ae08403B9bbb9124bB305C09058E32C39A48c",
            SupportedNetworks.ARBITRUM_SEPOLIA: "0xE591bf0A0CF924A0674d7792db046B23CEbF5f34",
            SupportedNetworks.POLYGON_AMOY: "0x360ad4f9a9A8EFe9A8DCB5f461c4Cc1047E1Dcf9",
            SupportedNetworks.BNB_CHAIN_TESTNET: "0xae13d989daC2f0dEbFf460aC112a837C89BAa7cd",
            SupportedNetworks.OPTIMISM_SEPOLIA: "0x4200000000000000000000000000000000000006",
            SupportedNetworks.BASE_SEPOLIA: "0x4200000000000000000000000000000000000006",
            SupportedNetworks.WEMIX_TESTNET: "0xbE3686643c05f00eC46e73da594c78098F7a9Ae7",
            SupportedNetworks.KROMA_SEPOLIA: "0x4200000000000000000000000000000000000001",
            SupportedNetworks.GNOSIS_CHIADO: "0x18c8a7ec7897177E4529065a7E7B0878358B3BfF",
            SupportedNetworks.CELO_ALFAJORES: "0x99604d0e2EfE7ABFb58BdE565b5330Bb46Ab3Dca",
        }

        # CCIP-BnM addresses
        self.ccip_bnm = {
            SupportedNetworks.ETHEREUM_SEPOLIA: "0xFd57b4ddBf88a4e07fF4e34C487b99af2Fe82a05",
            SupportedNetworks.AVALANCHE_FUJI: "0xD21341536c5cF5EB1bcb58f6723cE26e8D8E90e4",
            SupportedNetworks.ARBITRUM_SEPOLIA: "0xA8C0c11bf64AF62CDCA6f93D3769B88BdD7cb93D",
            SupportedNetworks.POLYGON_AMOY: "0xcab0EF91Bee323d1A617c0a027eE753aFd6997E4",
            SupportedNetworks.BNB_CHAIN_TESTNET: "0xbFA2ACd33ED6EEc0ed3Cc06bF1ac38d22b36B9e9",
            SupportedNetworks.OPTIMISM_SEPOLIA: "0x8aF4204e30565DF93352fE8E1De78925F6664dA7",
            SupportedNetworks.BASE_SEPOLIA: "0x88A2d74F47a237a62e7A51cdDa67270CE381555e",
            SupportedNetworks.WEMIX_TESTNET: "0xF4E4057FbBc86915F4b2d63EEFFe641C03294ffc",
            SupportedNetworks.KROMA_SEPOLIA: "0x6AC3e353D1DDda24d5A5416024d6E436b8817A4e",
            SupportedNetworks.GNOSIS_CHIADO: "0xA189971a2c5AcA0DFC5Ee7a2C44a2Ae27b3CF389",
            SupportedNetworks.CELO_ALFAJORES: "0x7e503dd1dAF90117A1b79953321043d9E6815C72",
        }

    @classmethod
    def capitalise_words(cls, s: str) -> str:
        return " ".join(word.capitalize() for word in s.strip().split())

    def get_supported_networks(self) -> list:
        return list(self.networks.keys())

    def get_network_info(self, network) -> dict:
        return {
            "chain_id": self.chain_ids.get(network),
            "router_address": self.routers.get(network),
            "link_address": self.links.get(network),
            "wrapped_native_address": self.wrapped_natives.get(network),
            "ccip_bnm_address": self.ccip_bnm.get(network),
        }

    def get_ccip_bnm_address(self, network: str):
        network: str = self.capitalise_words(network)
        # print(f"{self.supportedNetworksMapping.get(network)=}")
        return self.ccip_bnm.get(self.supportedNetworksMapping.get(network))


def main(): ...
