import unittest
import pandas as pd
import readFiles

class ReadFilesTest(unittest.TestCase):
    def testReturnOfPathName(self):
        mnist = readFiles.ReadFile(name_of_competition='digit-recognizer', 
                                   name_of_file='train',
                                   format_of_file='csv')
        self.assertEqual(mnist.path_name,
                        '../../competitions/digit-recognizer/train.csv')
    def testTypeOfFile(self):
        mnist = readFiles.ReadFile(name_of_competition='digit-recognizer', 
                                   name_of_file='train',
                                   format_of_file='csv')
        self.assertTrue(isinstance(mnist.file, pd.DataFrame))
        # self.assertEqual(type(mnist.file),
        #                 '../../competitions/digit-recognizer/train.csv')


if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
