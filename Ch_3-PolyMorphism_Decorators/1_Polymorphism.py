class api_fetch():
  def fetch(self):
        print("Fetching Data from API..")

class Database_fetch():
  def fetch(self):
        print("Fetching Data from Database..")

class s3_fetch():
  def fetch(self):
        print("Fetching Data from s3..")

obj=Database_fetch()
obj.fetch()