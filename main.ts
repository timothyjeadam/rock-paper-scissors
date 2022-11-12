let set_hand = 0
input.onGesture(Gesture.Shake, function () {
    set_hand = randint(1, 3)
    if (set_hand == 1) {
        basic.showLeds(`
            # # # # #
            # . . . #
            # . . . #
            # . . . #
            # # # # #
            `)
        basic.showString("paper")
    } else if (set_hand == 2) {
        basic.showLeds(`
            # # . . #
            # # . # .
            # . # . .
            # # . # .
            # # . . #
            `)
        basic.showString("scissors")
    } else if (set_hand == 3) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # # # .
            . # # # .
            . . . . .
            `)
        basic.showString("rock")
    }
})
basic.forever(function () {
	
})
