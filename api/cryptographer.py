import random

class Cryptographer:
    @classmethod
    def encode(cls, buffer: str):
        new_buffer = ''
        for i in range(0, len(buffer)):
            new_buffer += str(random.randrange(10)) \
                       + chr(ord(buffer[i]) + 10) \
                       + str(random.randrange(10))

        return new_buffer

    @classmethod
    def decode(cls, buffer: str):
        new_buffer = ''
        for i in range(1, len(buffer), 3):
                new_buffer += chr(ord(buffer[i]) - 10)

        return new_buffer
