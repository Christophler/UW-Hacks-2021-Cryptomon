
# How you use blockchain.py

from blockchain import addNewBlock, printBlockchain

if __name__ == '__main__':
    # parameters:
    # transactionType, success, mineInt, catchInt, encounter, numGraphicCards, numDogecoin, numEthereum, numBitcoin
    
    # add blocks to the block chain
    addNewBlock("genesis", True, 0, 0, False, 10, 0, 0, 0)
    addNewBlock("sell", False, 0, 0, False, 1, 2, 3, 4)

    printBlockchain() # print out the block chain
    
    # what is printed out by printBlockchain:
    '''
    ===== Block 1 =====
    Hash: c6dd0cae19eafbc487e4bad7d267dfb1
    BlockData: ('genesis', True, 0, 0, False, 10, 0, 0, 0)
    Previous Hash: None

    ===== Block 2 =====
    Hash: c9afc528ed0e05113bc2f6bdbc402b9f
    BlockData: ('sell', False, 0, 0, False, 1, 2, 3, 4)
    Previous Hash: c6dd0cae19eafbc487e4bad7d267dfb1
    '''
