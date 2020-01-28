import unittest
from cardclasses import *

class TestPokerHands(unittest.TestCase):
    royal_flush_hand = Hand(['0H','JH','QH','KH','AH'])
    straight_flush_hand = Hand(['4S','5S','6S','7S','8S'])
    four_kind_hand = Hand(['2C','2S','2H','2D','AS'])
    full_house_hand = Hand(['5H','5D','5C','0S','0D'])
    flush_hand = Hand(['2S','3S','0S','6S','JS'])
    straight_hand = Hand(['5H','6D','7H','8S','9C'])
    three_kind_hand = Hand(['JS','JC','JD','5H','3C'])
    two_pair_hand = Hand(['5S','5D','KC','KS','AD'])
    pair_hand = Hand(['AS','AH','8C','3S','7D'])
    high_card_hand = Hand(['JC','3D','4D','5D','6D'])
    empty_hand = Hand([])
    short_hand = Hand(['5C','6C','7C','8C'])

    def test_royalflush(self):
        self.assertEqual(self.royal_flush_hand.classify(), HandTypes.Royal_Flush)
    def test_straightflush(self):
        self.assertEqual(self.straight_flush_hand.classify(), HandTypes.Straight_Flush)
    def test_fourkind(self):
        self.assertEqual(self.four_kind_hand.classify(), HandTypes.Four_Of_A_Kind)
    def test_fullhouse(self):
        self.assertEqual(self.full_house_hand.classify(), HandTypes.Full_House)
    def test_flush(self):
        self.assertEqual(self.flush_hand.classify(), HandTypes.Flush)
    def test_straight(self):
        self.assertEqual(self.straight_hand.classify(), HandTypes.Straight)
    def test_threekind(self):
        self.assertEqual(self.three_kind_hand.classify(), HandTypes.Three_Of_A_Kind)
    def test_twopair(self):
        self.assertEqual(self.two_pair_hand.classify(), HandTypes.Two_Pair)
    def test_pair(self):
        self.assertEqual(self.pair_hand.classify(), HandTypes.Pair)
    def test_highcard(self):
        self.assertEqual(self.high_card_hand.classify(), HandTypes.High_Card)
    def test_emptyhand(self):
        self.assertEqual(self.empty_hand.classify(), HandTypes.Undefined)
    def test_shortcard(self):
        self.assertEqual(self.short_hand.classify(), HandTypes.Undefined)

if __name__ == '__main__':
    unittest.main()
