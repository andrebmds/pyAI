# To read a file 
# Where is the file ?
# Set my path
# Name of the project
# ex: 'digit-recognizer', 'landmark-retrieval-challenge', 'iMaterialist Challenge (Fashion) at FGVC5'
# /kaggle/competitions/landmark-retrieval-challenge
# /kaggle/competitions/landmark-retrieval-challenge
# Name of each principal file
# Test, Train, sample_submission
# What kind of file is it ?
# JSON
# CSV
# Images
# What kind of return should be?
# Return a pandas format.
import pandas as pd


class ReadFile:
    """Read a file and return as pandas"""

    def __init__(self, name_of_competition, name_of_file, format_of_file):
        # set variables
        self.name_of_competition = name_of_competition
        self.name_of_file = name_of_file
        self.format_of_file = format_of_file

        # Init Methods
        self.Set_Path_Name()
        self.Get_File_From()

    def Set_Path_Name(self):
        self.path_name = '../../competitions/{}/{}.{}'.format(self.name_of_competition, self.name_of_file,
                                                              self.format_of_file)

    def Get_File_From(self):
        """Returns a pandas file from the input """
        self.file = pd.read_csv(self.path_name)


if __name__ == '__main__':

    print('Read Files')
    bank = ReadFile(name_of_competition='Bank', name_of_file='creditcard', format_of_file='csv')

    if isinstance(bank.file, pd.DataFrame):
        # Pandas format
        bank_df = bank.file
        print(bank_df.info())

