Set_Hand = 0

def on_gesture_shake():
    global Set_Hand
    Set_Hand = randint(1, 3)
    if Set_Hand == 1:
        basic.show_leds("""
            # # # # #
                        # . . . #
                        # . . . #
                        # . . . #
                        # # # # #
        """)
        basic.show_string("paper")
    elif Set_Hand == 2:
        basic.show_leds("""
            # # . . #
                        # # . # .
                        # . # . .
                        # # . # .
                        # # . . #
        """)
        basic.show_string("scissors")
    elif Set_Hand == 3:
        basic.show_leds("""
            . . . . .
                        . # # # .
                        . # # # .
                        . # # # .
                        . . . . .
        """)
        basic.show_string("rock")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    pass
basic.forever(on_forever)
