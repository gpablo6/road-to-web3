import time
from brownie import Collectible
import scripts.constants as const
from scripts.collectible.helpers import get_breed, fund_collectible

def main():
    """
    Mint an NFT
    """
    try:
        collectible = Collectible[-1]
        transaction = collectible.createCollectible("None", {"from": const.DEV})
        transaction.wait(1)
        request_id = transaction.events['requestedCollectible']['requestId']
        token_id = collectible.requestIdToTokenId(request_id)
        time.sleep(55)
        breed = get_breed(collectible.tokenIdToBreed(token_id))
        print(f"Dog breed of token id: {breed}")
    except ValueError:
        fund_collectible()
        main()

if __name__ == "__main__":
    main()