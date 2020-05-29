import time

import paho.mqtt.publish as mqtt_pub
import paho.mqtt.subscribe as mqtt_sub

import settings


def mqtt_sub_worker(callback, topic='#'):
    while True:
        time.sleep(1)
        mqtt_sub.callback(callback, topics=topic, hostname=settings.MQTT_SERVER)


def publish(topic, message):
    mqtt_pub.single(topic, payload=message, hostname=settings.MQTT_SERVER)
