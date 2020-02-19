class Config(object):
    DEBUG = False
    TESTING = False
class ProductionConfig(Config):
    AZURE_STORE_CONNECTION ="DefaultEndpointsProtocol=https;AccountName=pydemostore;AccountKey=EDI1bZePwltDk6slUoVAd/TUAhBSmCEv60WQK24+PsDsRXnZq6mRuB5HFROGOQFDYq8TXRsUpI/o38lR2HEbeA==;EndpointSuffix=core.windows.net"
    BLOB_CONTAINER ="profilepic"
    TABLE_NAME = "profile"
    QUEUE_NAME = "profilequeue"
class DevelopmentConfig(Config):
    DEBUG = True
    AZURE_STORE_CONNECTION ="DefaultEndpointsProtocol=https;AccountName=pydemostore;AccountKey=EDI1bZePwltDk6slUoVAd/TUAhBSmCEv60WQK24+PsDsRXnZq6mRuB5HFROGOQFDYq8TXRsUpI/o38lR2HEbeA==;EndpointSuffix=core.windows.net"
    BLOB_CONTAINER ="profilepic"
    TABLE_NAME = "profile"
    QUEUE_NAME = "profilequeue"
