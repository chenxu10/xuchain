import hashlib as hasher
import datetime as date
import time

class xublock():
    def __init__(self, timestamp, index, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        crypotsha = hasher.sha256()
        block_info = str(self.index) + str(self.timestamp) + str(self.data) + \
        str(self.previous_hash)
        crypotsha.update(block_info.encode('utf-8'))
        return crypotsha.hexdigest()

def create_first_block():
    return xublock(date.datetime.now(), 0, "my_first_block", "0")

def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = last_block.hash
    return xublock(this_timestamp, this_index, this_data, this_hash)

if __name__ == '__main__':
    blockchain = [create_first_block()]
    previousblock = blockchain[0]

    num_of_blocks = 20
    for i in range(0, num_of_blocks):
        to_add_block = next_block(previousblock)
        blockchain.append(to_add_block)
        previousblock = to_add_block

        print ("Block {} has been added to the blockchain".format(to_add_block.index))
        time.sleep(2)
        print ("Hash:{}\n".format(to_add_block.hash))
