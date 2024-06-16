from data_link_layer import DataLinkLayer

class DataLinkLayerConfig:
    __instance = None

    def __init__(self):
        if DataLinkLayerConfig.__instance is not None:
            raise Exception("DataLinkLayerConfig is a singleton class. Use DataLinkLayerConfig.get_instance() to get the instance.")
        else:
            self.data_link_layer = DataLinkLayer()
            DataLinkLayerConfig.__instance = self

    @staticmethod
    def get_instance():
        if DataLinkLayerConfig.__instance is None:
            DataLinkLayerConfig()
        return DataLinkLayerConfig.__instance
