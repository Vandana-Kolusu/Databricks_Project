# Databricks notebook source
# MAGIC %run "./Loader Factory"

# COMMAND ----------

class AbstractLoader:
    def __init__(self,TransformedDF):
        if TransformedDF is None:
            raise ValueError("Error: TransformedDF cannot be None in AbstractLoader")
        self.TransformedDF = TransformedDF
        pass

    def sink(self):
        pass

class AirpodsAfterIphoneLoader(AbstractLoader):

    def sink(self):
        get_sink_source(
            sink_type="dbfs",
            df = self.TransformedDF,
            path = "dbfs:/FileStore/tables/apple_analysis/output/AirpodsAfterIphone",
            method = "overwrite"
        ).load_data_frame()

class OnlyAirpodsandIphoneLoader(AbstractLoader):

    def sink(self):
        params = {
            "partitionByColumns" : ["location"]
        }
        get_sink_source(
            sink_type="dbfs_with_partition",
            df = self.TransformedDF,
            path = "dbfs:/FileStore/tables/apple_analysis/output/OnlyAirpodsandIphone",
            method = "overwrite",
            params = params
        ).load_data_frame()

        get_sink_source(
            sink_type="delta",
            df = self.TransformedDF,
            path = "default.OnlyAirpodsandIphone",
            method = "overwrite"
        ).load_data_frame()