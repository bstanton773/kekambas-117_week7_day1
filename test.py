from whiteboard import solution
from unittest import TestCase, main


class ChocolateChecker(TestCase):

    def test_01(self):
        self.assertEqual(solution(4,1,9),4)

    def test_02(self):
        self.assertEqual(solution(4,1,10),-1)

    def test_03(self):
        self.assertEqual(solution(4,1,7),2)

    def test_04(self):
        self.assertEqual(solution(6,2,7),2)

    def test_05(self):
        self.assertEqual(solution(4,1,5),0)
    
    def test_06(self):
        self.assertEqual(solution(4,1,4),4)

    def test_07(self):
        self.assertEqual(solution(5,4,9),4)

    def test_08(self):
        self.assertEqual(solution(9,3,18),3)

    def test_09(self):
        self.assertEqual(solution(3,1,9),-1)
        
    def test_10(self):
        self.assertEqual(solution(1,2,7),-1)

    def test_11(self):
        self.assertEqual(solution(1,2,6),1)

    def test_12(self):
        self.assertEqual(solution(1,2,5),0)

    def test_13(self):
        self.assertEqual(solution(6,1,10),5)

    def test_14(self):
        self.assertEqual(solution(6,1,11,),6)

    def test_15(self):
        self.assertEqual(solution(6,1,12),-1)

    def test_16(self):
        self.assertEqual(solution(6,1,13),-1)

    def test_17(self):
        self.assertEqual(solution(6,2,10),0)

    def test_18(self):
        self.assertEqual(solution(6, 2, 11),1)

    def test_19(self):
        self.assertEqual(solution(6,2,12),2)

    def test_20(self):
        self.assertEqual(solution(60,100,550),50)

    def test_21(self):
        self.assertEqual(solution(1000,1000000, 5000006),6)

    def test_22(self):
        self.assertEqual(solution(7,1,12),7)

    def test_23(self):
        self.assertEqual(solution(7,1,13),-1)
        
    def test_24(self):
        self.assertEqual(solution(7,2,13),3)

if __name__ == '__main__':
    main()