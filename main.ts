input.onGesture(Gesture.Shake, function () {
    music.play(music.stringPlayable("E B C5 A B G A F ", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function () {
	
})
