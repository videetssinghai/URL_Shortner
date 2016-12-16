import string
import random

def generate_code(size=7,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
    new_code = generate_code(size=size)
    print instance.__class__
    print instance
    temp = instance.__class__
    qs_exists = temp.objects.filter(shortcode= new_code).exists()
    if qs_exists:
        return create_shortcode(size=6)
    return new_code


