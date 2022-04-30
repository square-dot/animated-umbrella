import p272
import unittest

class Test_StringInput(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(p272.process("\"This is a test\""), """``This is a test''""")

    def test_multiline(self):
        self.assertEqual(p272.process("""\"This is 
a multiline 
input\""""), """``This is 
a multiline 
input''""")

    def test_exampleFromPdf(self):
        self.assertEqual(p272.process("""\"To be or not to be," quoth the Bard, "that
is the question".
The programming contestant replied: "I must disagree.
To `C' or not to `C', that is The Question!\""""), """``To be or not to be,'' quoth the Bard, ``that
is the question''.
The programming contestant replied: ``I must disagree.
To `C' or not to `C', that is The Question!''""")

if __name__ == '__main__':
    unittest.main()
