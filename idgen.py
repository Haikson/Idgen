import string
import random

class Idgen:
    def gen(size=6, upp=True, low=True, dig=True, ex_chars = ''):
        chars = ''
        if upp:
            chars += string.ascii_uppercase
        if low:
            chars += string.ascii_lowercase
        if dig:
            chars += string.digits
        chars += ex_chars
    
        if chars == '':
            return ''

        return ''.join(random.choice(chars) for x in range(size))
