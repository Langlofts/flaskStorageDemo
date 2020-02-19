from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
from azure.storage.queue import QueueClient

def create_blob_client(connectionString,containerName):
    blob_service_client = BlobServiceClient.from_connection_string(connectionString)
    container_client = blob_service_client.get_container_client(containerName)
    return container_client

def upload_blob_data(container_client,fileName,sourcefile):
     try:
            # Create new Container in the service
            #container_client.create_container()

            # Instantiate a new BlobClient
            blob_client = container_client.get_blob_client(fileName)

            # [START upload_a_blob]
            # Upload content to block blob
            with open(sourcefile, "rb") as data:
                 blob_client.upload_blob(data, blob_type="BlockBlob")
            # [END upload_a_blob]
     finally:
        print('container error')

def connect_to_table(connectionString):
     table_service = TableService(connection_string=connectionString)
     return table_service

def insert_to_table(table_service,table_name,formData,fileName):
     profile = {'PartitionKey': formData['emailId'], 'RowKey': formData['fullName'],'Password':formData['password'],'FileName':fileName}
     table_service.insert_entity(table_name, profile)

def connect_to_queue(connectionString,queue_name):
     queue = QueueClient.from_connection_string(conn_str=connectionString, queue_name=queue_name)
     return queue

def push_message_to_queue(queue_client,message):
     queue_client.send_message(message)
