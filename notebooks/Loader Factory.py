# Databricks notebook source
class DataSink:

    def __init__(self,df,path,method, params = None):
        self.df = df
        self.path=path
        self.method = method
        self.params = params

    def load_data_frame(self):
        raise ValueError("Not implemented")

class LoadtoDBFS(DataSink):

    def load_data_frame(self):

        self.df.write.mode(self.method).parquet(self.path)


class LoadtoDBFSWithPartition(DataSink):

    def load_data_frame(self):
        partitionByColumns = self.params.get("partitionByColumns")
        self.df.write.mode(self.method).partitionBy(*partitionByColumns).save(self.path)

class LoadtoDelta(DataSink):

    def load_data_frame(self):
        self.df.write.format("delta").mode(self.method).saveAsTable(self.path)


def get_sink_source(sink_type,df,path,method,params=None):

    if sink_type == 'dbfs':
        return LoadtoDBFS(df,path,method,params)
    
    elif sink_type == 'dbfs_with_partition':
        return LoadtoDBFSWithPartition(df,path,method,params)
    
    elif sink_type == 'delta':
        return LoadtoDelta(df,path,method,params)
    
    else:
        return ValueError(f"Not implemented for sink type: ")

