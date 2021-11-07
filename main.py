intervalSecret = 1000
intervalPlayers = 0
INTERVAL_STEP = 250

music.set_volume(16)

on_button_pressed_b()

def on_logo_touch():
    global intervalPlayers
    intervalPlayers = control.millis()
    def onIn_background():
        music.stop_all_sounds()
        basic.show_icon(IconNames.ASLEEP)
    control.in_background(onIn_background)
    pass

def on_logo_release():
    global intervalPlayers
    global intervalSecret
    intervalPlayers = control.millis() - intervalPlayers
    music.stop_all_sounds()

    console.log_value("secret", intervalSecret)
    console.log_value("player", intervalPlayers)

    
    percentil = Math.map(Math.min(intervalPlayers, intervalSecret), 0, Math.max(intervalPlayers, intervalSecret), 0, 100)
    
    if percentil >= 95: soundExpression.happy.play_until_done()
    else: music.play_tone(Note.C, 100)

    led.plot_bar_graph(percentil - (100 - percentil) * 2, 100)
    pass
    
def on_button_pressed_a():
    global intervalSecret
    basic.show_icon(IconNames.NO)
    music.play_tone(Note.A, intervalSecret)
    music.play_tone(Note.C, 100)
    basic.show_icon(IconNames.YES)
    pass

def on_button_pressed_b():
    global intervalSecret
    basic.show_icon(IconNames.HEART)
    intervalSecret = randint(1, 10) * INTERVAL_STEP
    on_button_pressed_a()
    basic.show_icon(IconNames.YES)
    pass

input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_release)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touch)
input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)


