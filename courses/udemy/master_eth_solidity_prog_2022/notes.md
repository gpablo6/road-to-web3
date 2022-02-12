# Lesson 3. Ethereum Nodes
Etehreum is a peer-to-peer network of computers named /**"Ethereum Nodes"**. Anyone can run an Ethereum Node on its laptop or desktop machine (it require lots of resources).
Every Ethereum Node runs an Ethereum Client such as [geth](https://geth.ethereum.org/)

### Types of Node:
a. Full Node - Stores locally a copy of the entire blockchain, participates in the block validation and verifies all blocks and states
b. Light Node - Stores only the header chain and request everything else, and can verify the validity of the data against the states in the block headers
c. Archive Node - Stores eveything ketp in the full node and builts an archive of historical states

An Ethereum node runs a VM named *EVM* and runs applications (EVM bytecode) based on a global consensus mechanism. **This EVM has its microkernel, stack, memory, and storage**.

There are new clients for Ethereum 2.0 that run [*Beacon*](https://ethereum.org/en/upgrades/beacon-chain/) and the [*Shard Chains*](https://ethereum.org/en/upgrades/shard-chains/) 

There are **many different Ethereum Networs**: Main Net, Test Nets (Rinkeby, Kovan), Private Ethereum Blockchains

--

# Lesson 4. Ethereum Accounts and Ethereum Addresses
1. Externally Owned Account (EOA)
* **Controlled by a private key** and identified by an unique address;
* It holds an ETH balance and has no associated code;
* Used for holding, sending and recieving ETH and for interacting with smart contracts (deployment, calling functions etc); 

2. Contract Account (CA)
* **Controlled by the contract code**;
* Has a unique address but doesn't have a public or private key;
* It's an autonomous agent and it's code execution is triggered by recieving a transaction or a message (call) from another contract of an EOA;
* It holds and ETH balance like an EOA;

### Ethereum Account Components
1. Nonce -> counter that indicates the number of transactions sent from the account (it ensure that the same transaction isn't submitted twice)
2. Balance (in wei | *denomination of ETH (10^18 wei in an ETH)*)
3. Account Address
4. Account Private & Public Key (only for EOA)
5. Code (only for the contract account). This is the inmutable EVM bytecode
6. Storage (only for the contract account, empty by default)

NOTE: You never hold cryptocurrency. You hold the private key that can unlock the funds that are always on the blockchain!

### Ethereum Address
* An EOA Address is derived from the last 20 bytes (160 bits) of the publick key that are Keccak-256 hashed. It's represented in a hexadecimal format, which is often indicated explicitly by appending 0x to the address.
**Example**: 0xCC713690827C96b8b0b5456F34B23dCC7D03aEd2
* The address for an Ethereum Contract is deterministically computed from the address of its creator (sender) and how many transactions the creator has sent (nonce). 
* There is a **lower-case** address version and **partial upper-case** version that also contains a **checksum**.
    * 0x0d8775f648430679a709e98d2b0cb6250d2887ef
    * 0x0D8775F648430679A709E98d2b0Cb6250d2887EF

--

# Lesson 5. Creating an Ethereum Account Using MetaMask

### MetaMask Overview
* **OpenSource** - the code can be reviewed and audited by the community;
* **Hierarchical Deterministic (HD) wallet** - you can backup your account using a set of words called *seed phrase*. The Seed phrases can be used to restore the account;
* It has built-in cryptocurrency purchasing;
* **Simple interface and local key storage**. It stores the private key not the cryptocurrency; 

NOTE: You only are the owner if you have the private key that unlocks the funds!

--

# Lesson 7. Ether (ETH)
* *Ether* having the *ETH* code and the Greek uppercase Xi character (*Ξ*) is the cryptocurrency used on the Ethereum Platform
* It is used to *pay for transactions* fees and computational services on the Ethereum network. It's the crypto-fuel for the Ethereum platform.
* Ether is the incentive ensuring that **developers write quality applications** (wasteful code costs more), and that the **network remains healthy** (people are compensated for their contributed resources).

--

# Lesson 8. Rinkeby Authenticated Faucet

" Faucets are web apps where you can input an address to which you requested tesnet ETH to be sent to 