# ConfigObj
'''
import os.path
from configobj import ConfigObj
# from icecream import ic

BASE = os.path.dirname(os.path.abspath(__file__))
# ic(BASE)

config = ConfigObj(os.path.join(BASE, "Chapter030_config.ini"))
print(config["product"])

'''
import os.path
import configobj

BASE = os.path.dirname(os.path.abspath(__file__))

def createConfig(path):
    config = configobj.ConfigObj()
    config.filename = path
    config["Sony"] = {}
    config["Sony"]["Product"] = "Sony PS3"
    config["Sony"]["accessories"] = ['controller', 'eye', 'memmory stick']
    config["Sony"]["retail price"] = "$400"
    config.write()

if __name__ == "__main__":
    createConfig(os.path.join(BASE, ".\data\Chapter030_config_02.ini"))
