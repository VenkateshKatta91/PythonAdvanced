import pandas as pd

class DataExt:

   def __init__(self,file_path:str):
      self.file_path=file_path

   def fetch_csv(self,separator:str):
      #Write your custom logic
      df=pd.read_csv(self.file_path, sep=separator)
      print(df.head())

   def fetch_json(self):
      #Write your custom logic
      df=pd.read_json(self.file_path)
      print(df.head())

   def fetch_parquet(self):
      #Write your custom logic
      df=pd.read_parquet(self.file_path)
      print(df.head())

   def fetch_tsv(self):
      #Write your custom logic
      df=pd.read_tsv(self.file_path)
      print(df.head())

obj=DataExt("Ch_1-OOP/Files/orders.csv")
obj.fetch_csv(",")