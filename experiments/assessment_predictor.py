import data_loader
import tqdm
import sklearn.ensemble
import sklearn.feature_extraction
import sklearn.pipeline
import sklearn.feature_selection
import sklearn.metrics

import pandas as pd

class AssessmentPredictor:
    def __init__(self):
        #vectoriser = sklearn.feature_extraction.TfidfVectorizer()
        #self.__pipeline = 
        pass

    def extract_x_y(self, data: pd.DataFrame) -> pd.DataFrame:
        # We want to create a feature vector of learning outcome description and y is set of assessment types and their weight

        x = data["learning_outcome_description"]

        print(data.head())

        assessment_labels = ["assessment_type_weight_" + str(x) for x in data.assessment_type.unique()]
        y = pd.DataFrame(columns=["learning_outcome", *assessment_labels])
        for outcome_id in tqdm.tqdm(data["learning_outcome"].unique()):
            mask = (data["learning_outcome"] == outcome_id)
            
            row = {"learning_outcome": outcome_id}
            row.update({"assessment_type_weight_" + str(x): 0 for x in data.assessment_type.unique()})
            # sum up all assessments of the same type
            for assessment_type in data.assessment_type.unique():
                relevant_assessments = data[mask][data[mask]["assessment_type"] == assessment_type]
                total = sum(relevant_assessments["assessment_weight"])
                row.update({"assessment_type_weight_" + str(assessment_type): total})

            y = y.append(row, ignore_index=True)

        return x, y

    def train(self, data: pd.DataFrame):
        pass


if __name__ == "__main__":
    loader = data_loader.DataLoader()

    data = loader.read("../data")

    predictor = AssessmentPredictor()

    x, y = predictor.extract_x_y(data)

    print(x.head())
    print(y.head())



                    
                    
                



