from unittest import TestCase

from diamond import Diamond


class TestDiamond(TestCase):

    def setUp(self):
        self.diamond = Diamond()

    def test_create_diamond_should_return_diamond_size_1_when_up_to_A(self):
        # Given
        stop_letter = 'A'

        # When
        result = self.diamond.up_to(stop_letter)

        # Then
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], 'A')
