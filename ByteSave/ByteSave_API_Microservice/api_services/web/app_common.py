import datetime
import arrow
from pymongo import MongoClient
from azure.storage.blob import BlobServiceClient
link_api_agent = ''
link_api_mac = ''

client = MongoClient("mongodb://0.0.0.0:27017")
class Timer(object):
    @classmethod
    def get_timestamp_now(cls):
        now = arrow.utcnow()
        return now.timestamp
    @classmethod
    def get_timestamp(cls,timedate):
        date = datetime.datetime.strptime(timedate, "%Y/%m/%d")
        at = datetime.datetime.timestamp(date)
        return int(at)

def Convert_timestamp(timestamp):
    try:
        ts = datetime.datetime.fromtimestamp(int(timestamp)).strftime("%d/%m/%Y")
    except Exception as e:
        return ''
    return ts
def Convert_timestamp2(timestamp):
    try:
        ts = datetime.datetime.fromtimestamp(int(timestamp))
    except Exception as e:
        return ''
    return ts
def GetCapacity(conn_str):
    size = 0
    try:
        # conn_str = 'DefaultEndpointsProtocol=https;AccountName=tsgblobtestbykhanh;AccountKey=46BUwKMiWg+hJx9NSdB46dbL46RmkSLRWnEOkY8aXjASLBFIojsBchdLBdvJCW+2iH91riWgN76gr3ljCXZjdQ==;EndpointSuffix=core.windows.net'
        blob_service_client = BlobServiceClient.from_connection_string(conn_str=conn_str.strip())
        all_containers = blob_service_client.list_containers(include_metadata=True)
        for con in all_containers:
            container = blob_service_client.get_container_client(container=con.name)
            for blob in container.list_blobs():
                size += blob.size
    except Exception as e:
        print(e)
        size = 0
    return size

