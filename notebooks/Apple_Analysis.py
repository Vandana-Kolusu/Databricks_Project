# Databricks notebook source


# COMMAND ----------

# MAGIC %run "./Transform"

# COMMAND ----------

# MAGIC %run "./Extractor"

# COMMAND ----------

# MAGIC %run "./Loader"

# COMMAND ----------

class FirstWorkFlow:
    """
        ETL pipeline to find out customers who have bought Airpods after Iphone
    """
    def __init__(self):
        pass

    def runner(self):

        # Step 1: Extract the data from different sources
        inputDFs = AirpodsAfterIphone().extract()

        # Step 2: Implement the logic for transformation
        # Customers who have bought Airpods after Iphone
        FirstTransformedDF = AirpodsAfterIphoneTransformer().transform(inputDFs) 

        # Step 3: Loading the data into sink
        AirpodsAfterIphoneLoader(FirstTransformedDF).sink()
    


# COMMAND ----------

class SecondWorkFlow:
    """
        ETL pipeline to find out customers who have bought Airpods and Iphone
    """
    def __init__(self):
        pass

    def runner(self):

        # Step 1: Extract the data from different sources
        inputDFs = AirpodsAfterIphone().extract()

        # Step 2: Implement the logic for transformation
        # Customers who have bought Airpods after Iphone
        SecondTransformedDF = OnlyAirpodsandIphone().transform(inputDFs)

        # Step 3: Loading the data into sink
        OnlyAirpodsandIphoneLoader(SecondTransformedDF).sink()
    


# COMMAND ----------

class WorkFlowRunner():

    def __init__(self,name):
        self.name = name

    def runner(self):
        if self.name == "FirstWorkFlow":
            return FirstWorkFlow().runner()
        elif self.name == "SecondWorkFlow":
            return SecondWorkFlow().runner()

name = "SecondWorkFlow"
workflowRunner = WorkFlowRunner(name).runner()

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("thebigdatashow.me").getOrCreate()

input_df = spark.read.format("csv").option("header", "True").load("dbfs:/FileStore/tables/Transaction_Updated.csv")

input_df.show()

# COMMAND ----------

dbutils.fs.mkdirs("dbfs:/FileStore/tables/apple_analysis/output/AirpodsAfterIphone")
