import threading
import time

from mqtt import mqtt_sub_worker, publish
from pytify.linux import Linux as Pytify

interface = Pytify()


def handle_music_changes(client, userdata, message):
    action = message.topic.split('/')[-1]
    print(f'Action received: {action}')

    # Define what to do depending on which state is received
    actions = {
        'prev': interface.prev,
        'next': interface.next,
        'play': interface.play_pause,
        'pause': interface.play_pause,
    }
    try:
        actions[action]()
    except KeyError:
        print(
            f'MQTT action not supported:\n'
            f' -- Action: {action}\n'
            f' -- Topic: {message.topic}\n'
            f' -- Payload: {message.payload}'
        )


def send_info(topic, seconds_to_sleep=1.0):
    old_state = None
    while True:
        # Sleep for a while
        time.sleep(seconds_to_sleep)

        current_state = interface.get_current_playing()
        if old_state != current_state:
            # Store current state
            old_state = current_state
            # Logging current state
            print(f'Current song: {current_state}')
            # Publish info
            publish(
                topic=topic,
                message=current_state
            )


# launch subscriber thread that listens to events and actuate
threading.Thread(target=mqtt_sub_worker, args=(handle_music_changes, 'music/state/change/#'), daemon=True).start()
# launch publisher thread
threading.Thread(target=send_info, args=('music/state/info',), daemon=True).start()

# Keep main thread alive   - TODO: is this needed?
while True:
    time.sleep(10)
