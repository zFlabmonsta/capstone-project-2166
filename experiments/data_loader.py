'''
Load the provided dataset into a big pandas data frame
Inefficient as shit but easy
'''

import pandas as pd
import json
import sys
import os
import io

class DataLoader:
    def read(self, directory: str) -> pd.DataFrame:
        print(os.path.realpath(os.path.join(directory, "assessments.json")))
        assessments = self.load_file(os.path.join(directory, "assessments.json"))
        learning_outcomes = self.load_file(os.path.join(directory, "learning_outcomes.json"))
        as_map_lo = self.load_file(os.path.join(directory, "as_map_lo.json"))

        assessments.columns = ["assessment" if x == "id" else x for x in assessments.columns]
        learning_outcomes.columns = ["learning_outcome" if x == "id" else x for x in learning_outcomes.columns]

        # Merge them

        print(assessments.head())
        print(learning_outcomes.head())
        print(as_map_lo.head())

        assessments = assessments.merge(as_map_lo, on="assessment")
        print(assessments.head())
        return assessments.merge(learning_outcomes, on="learning_outcome")


    def load_file(self, file: str) -> pd.DataFrame:
        f = io.open(file, "r", encoding='utf-8-sig')
        ret = pd.DataFrame(json.load(f))

        f.close()
        return ret


if __name__ == "__main__":
    loader = DataLoader()

    print(loader.read("../data").head())


        
