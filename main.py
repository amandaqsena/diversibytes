def on_gesture_shake():
    music.play(music.string_playable("E B C5 A B G A F ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
