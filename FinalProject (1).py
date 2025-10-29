#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyspark
import pandas as pd
import csv


# In[ ]:


from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, LongType, IntegerType, FloatType
import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import OneHotEncoder, StringIndexer, VectorAssembler, IndexToString
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator


# In[ ]:


ss=SparkSession.builder.master("local").appName("PhillyDelayPredictor").getOrCreate()


# In[ ]:


flight_schema = StructType([ StructField("id", IntegerType(), False ),                         StructField("clump_thickness", IntegerType(), False),                         StructField("unif_cell_size", IntegerType(), False ),                         StructField("unif_cell_shape", IntegerType(), False ),                         StructField("marg_adhesion", IntegerType(), False),                         StructField("single_epith_cell_size", IntegerType(), False),                         StructField("bare_nuclei", IntegerType(), False),                        StructField("bland_chrom", IntegerType(), False),                         StructField("norm_nucleoli", IntegerType(), False),                         StructField("mitoses", IntegerType(), False),                         StructField("class", StringType(), False)                            ])


# In[ ]:


import pandas as pd

excel_path = "/storage/work/cml6923/ds410_f25/Final_Project/United_Statistics.xls"  
df = pd.read_excel(excel_path)

csv_path = "/storage/work/cml6923/ds410_f25/Final_Project/United_Statistics.csv"
df.to_csv(csv_path, index=False)


# In[ ]:


spark_df = ss.read.csv("/storage/work/cml6923/ds410_f25/Final_Project/United_Statistics.csv", header=True, inferSchema=True)
spark_df.show(5)


# In[ ]:




