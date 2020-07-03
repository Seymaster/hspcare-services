import uuid

def generate_random_numbers():
    id = uuid.uuid4()
    return id.node
print(generate_random_numbers())