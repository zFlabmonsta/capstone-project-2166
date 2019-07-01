'''
Load the provided dataset into a big pandas data frame
Inefficient as shit but easy
'''

import pandas as pd
import json
import sys
import os
import io

def rename_column(df: pd.DataFrame, orig: str, to: str):
    df.columns = [to if x == orig else x for x in df.columns]

class DataLoader:
    def read(self, directory: str) -> pd.DataFrame:
        print(os.path.realpath(os.path.join(directory, "assessments.json")))
        assessments = self.load_file(os.path.join(directory, "assessments.json"))
        learning_outcomes = self.load_file(os.path.join(directory, "learning_outcomes.json"))
        as_map_lo = self.load_file(os.path.join(directory, "as_map_lo.json"))

        rename_column(assessments, "id", "assessment")
        rename_column(assessments, "title", "assessment_title")
        rename_column(assessments, "description", "assessment_description")
        rename_column(assessments, "weight", "assessment_weight")

        rename_column(learning_outcomes, "id", "learning_outcome")
        rename_column(learning_outcomes, "description", "learning_outcome_description")
        rename_column(learning_outcomes, "clone_of", "learning_outcome_clone_of")

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


        
