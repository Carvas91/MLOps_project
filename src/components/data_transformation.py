import sys
from dataclasses import dataclass

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

import os




@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifact', 'preprocessor.pkl')
    

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_obj(self):
        try:
            numerical_columns = ['reading_score', 'writing_score']
            categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

        except:
            pass

    