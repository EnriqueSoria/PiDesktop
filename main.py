import threading
import time

from mqtt import mqtt_sub_worker, publish
from pytify.linux import Linux

interface = Linux()


def handle_music_changes(client, userdata, message):
    topic = message.topic
    print(f'Topic: "{topic}" -- Message: "{message.payload}"')
    action = topic.split('/')[-1]

    actions = {
        'prev': interface.prev,
        'next': interface.next,
        'play': interface.play_pause,
        'pause': interface.play_pause,
    }
    actions[action]()


def send_info(topic, run_freq=5000):
    old_state = None
    while True:
        time.sleep(run_freq / 1000)  # sleep for a while

        current_state = interface.get_current_playing()
        if old_state == current_state:
            continue

        old_state = current_state
        print(f'Current song: {current_state}')
        publish(
            topic='mytopic',
            message=current_state
        )


threading.Thread(target=mqtt_sub_worker, args=(handle_music_changes, 'music/state/change/#'), daemon=True).start()
threading.Thread(target=send_info, args=('music/state/info', ), daemon=True).start()

# TODO: is this needed?
while True:
    time.sleep(10)


