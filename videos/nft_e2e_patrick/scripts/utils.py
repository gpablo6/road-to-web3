import scripts.constants as const 
from brownie import interface, config, network

def get_network() -> str:
    """
    Get current active network
    """
    return network.show_active()

def link_funding(contract_cls, origin_wallet: str = const.DEV):
    """
    Funds a contract with LINK tokens from specified wallet

    Parameters
    ---------
    origin_wallet: str, default = const.DEV
        Wallet for funding the contract
    """
    link_token = interface.LinkTokenInterface(config['networks'][get_network()]['link_token'])
    link_token.transfer(contract_cls, 100000000000000000, {"from": origin_wallet})
