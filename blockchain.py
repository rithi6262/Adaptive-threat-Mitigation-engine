import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, time(), {"msg": "Genesis Block"}, "0")
        self.chain.append(genesis_block)

    def add_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), time(), data, prev_block.hash)
        self.chain.append(new_block)
        return new_block

    def get_chain(self):
        return [block.__dict__ for block in self.chain]
