""" generates random numner to be used as booking ID """

import uuid

def generate_random_number():
    id = uuid.uuid4()
    return id.node
# print(generate_random_number())