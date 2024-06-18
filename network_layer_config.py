from network_layer import NetworkLayer

class NetworkLayerConfig:
    __instance = None

    def __init__(self):
        if NetworkLayerConfig.__instance is not None:
            raise Exception("NetworkLayerConfig is a singleton class. Use NetworkLayerConfig.get_instance() to get the instance.")
        else:
            self.network_layer = NetworkLayer()
            NetworkLayerConfig.__instance = self

    @staticmethod
    def get_instance():
        if NetworkLayerConfig.__instance is None:
            NetworkLayerConfig()
        return NetworkLayerConfig.__instance