from brownie import Collectible, config
import scripts.constants as const
from scripts.utils import get_network, link_funding

publish_source = False
active_network = get_network()

def main():
    """
    Runner function for deploying

    Returns
    -------
    collectible: ContractContainer
        Collectible contract current deployed instance
    """
    print(f"Account Address: {const.DEV}\tAt network: {active_network}")
    collectible = Collectible.deploy(config['networks'][active_network]['vrf_coordinator'], \
                                    config['networks'][active_network]['link_token'], \
                                    config['networks'][active_network]['keyhash'], \
                                    {"from": const.DEV}, publish_source = publish_source)
    link_funding(collectible)
    return collectible
                            
if __name__ == "__main__":
    main()