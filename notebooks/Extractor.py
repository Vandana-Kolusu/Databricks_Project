# Databricks notebook source
# MAGIC %run "./Reader's Factory "

# COMMAND ----------

class Extractor:
    " Abstract class"
    def __init__(self):
        pass

    def extract(self):
        pass

class AirpodsAfterIphone(Extractor):

    def extract(self):

        "Implementing the code for extracting"

        TransactionInputDf = get_data_source(
            data_type="csv", 
            file_path="dbfs:/FileStore/tables/Transaction_Updated.csv"
        ).get_data_frame()

        customerInputDF = get_data_source(
            data_type="delta", 
            file_path="default.customer_delta_table"
        ).get_data_frame()

        inputDFs = {

                "TransactionInputDf" : TransactionInputDf,
                "customerInputDF" : customerInputDF

        }

        return inputDFs
