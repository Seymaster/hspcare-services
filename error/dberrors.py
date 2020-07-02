def generate_fake(count=100):
    from sqlalchemy.exc import IntegrityError
    from random import seed
    import