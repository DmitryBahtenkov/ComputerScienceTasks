from SimpleTasks.unbreakable_encryption import *

if __name__ == '__main__':
    k1, k2 = encrypt("Hello there!")
    result: str = decrypt(k1, k2)
    print(result)
