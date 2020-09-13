
import os

from decouple import AutoConfig

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config = AutoConfig(f'{BASE_DIR}/')

MQTT_SERVER = config("MQTT_SERVER", default="localhost")
