# Databricks notebook source
from pyspark.sql.window import Window
from pyspark.sql.functions import lead, col, broadcast, collect_set, size, array_contains

class Transformer:
    def __init__(self):
        pass

    def transform(self, inputDFs):
        pass

class AirpodsAfterIphoneTransformer(Transformer):

    def transform(self, inputDFs):
        
        TransactionInputDf = inputDFs.get("TransactionInputDf")

        print("TransactionInputDf in transform")

        TransactionInputDf.show()

        WindowSpec = Window.partitionBy("customer_id").orderBy("transaction_date")

        transformedDF = TransactionInputDf.withColumn(
            "next_product_name", lead("product_name").over(WindowSpec)
        )

        print("Airpods after buying Iphone")

        transformedDF.orderBy("customer_id","transaction_date","product_name").show()

        filteredDF = transformedDF.filter(

            (col("product_name") == "iPhone") & (col("next_product_name") == "AirPods")
        )

        filteredDF.orderBy("customer_id","transaction_date","product_name").show()

        customerInputDF = inputDFs.get("customerInputDF")

        joinDF = customerInputDF.join(
            broadcast(filteredDF),
            "customer_id"
        )
        print("Joined DF")
        joinDF.show()

        return joinDF.select(
            "customer_id",
            "customer_name",
            "location"
        )


class OnlyAirpodsandIphone(Transformer):

    def transform(self,inputDFs):

        TransactionInputDf = inputDFs.get("TransactionInputDf")

        print("TransactionInputDf in transform")

        groupedDF = TransactionInputDf.groupBy("customer_id").agg(

            collect_set("product_name").alias("products")
        )

        groupedDF.show()

        filteredDF = groupedDF.filter(

            (array_contains(col("products"),"iPhone")) & 
            (array_contains(col("products"),"AirPods")) &
            (size(col("products")) == 2)
        )

        filteredDF.show()

        customerInputDF = inputDFs.get("customerInputDF")

        joinDF = customerInputDF.join(
            broadcast(filteredDF),
            "customer_id"
        )
        print("Joined DF")
        joinDF.show()

        return joinDF.select(
            "customer_id",
            "customer_name",
            "location"
        )

