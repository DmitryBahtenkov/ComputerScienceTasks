import unittest
from SimpleTasks.trivial_compression import *
from sys import getsizeof


class CompressionTestCase(unittest.TestCase):
    def test_compressed(self):
        data: str = "AGCTCTGCTGCCTCCCGATAAAA" * 100
        compressed = CompressedGene(data)

        original_size = getsizeof(data)
        compressed_size = getsizeof(compressed.bit_string)
        decompressed = compressed.decompress()

        self.assertTrue(original_size > compressed_size)
        self.assertEqual(decompressed, data)


if __name__ == '__main__':
    unittest.main()
