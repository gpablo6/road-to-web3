from brownie import Collectible
from scripts.utils import link_funding

def fund_collectible():
    """
    Fund latest deploy Collectible contract
    """
    collectible = Collectible[-1]
    link_funding(collectible)

def get_breed(breed_number: int) -> str:
    """
    Get Breed type as define in Enum Breed

    Parameters
    ---------
    breed_number: int
        Index of breed to return

    Returns
    -------
    breed_type: str
        The name of indexed breed type
    """
    switch = {0: 'PUG', 1: 'SHIBA_INU', 2: 'ST_BERNARD'}
    return switch[breed_number]
