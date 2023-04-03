class sequence_repeat:

    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.number - 1:
            raise StopIteration

        self.index += 1

        return self.sequence[self.index % len(self.sequence)]


# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        result = list(sequence_repeat('I Love Python', 3))
        self.assertEqual(result, ['I', ' ', 'L'])

if __name__ == '__main__':
    unittest.main()