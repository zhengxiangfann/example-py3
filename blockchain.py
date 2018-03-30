import hashlib
import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        block = {'index':len(self.chain) + 1,
                'timestamp':time(),
                'transactions':self.current_transactions,
                'proof':proof,
                'previous_hash':provious_hash or self.hash(self.chain[-1]),}
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender':sender,
            'recipient':recipient,
            'amount':amount
            })
        return self.lask_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_key=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
