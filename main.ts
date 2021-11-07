let intervalSecret = 1000
let intervalPlayers = 0
let INTERVAL_STEP = 250
music.setVolume(16)
on_button_pressed_b()
function on_button_pressed_a() {
    
    basic.showIcon(IconNames.No)
    music.playTone(Note.A, intervalSecret)
    music.playTone(Note.C, 100)
    basic.showIcon(IconNames.Yes)
    
}

function on_button_pressed_b() {
    
    basic.showIcon(IconNames.Heart)
    intervalSecret = randint(1, 10) * INTERVAL_STEP
    on_button_pressed_a()
    basic.showIcon(IconNames.Yes)
    
}

input.onLogoEvent(TouchButtonEvent.Released, function on_logo_release() {
    
    
    intervalPlayers = control.millis() - intervalPlayers
    music.stopAllSounds()
    console.logValue("secret", intervalSecret)
    console.logValue("player", intervalPlayers)
    let percentil = Math.map(Math.min(intervalPlayers, intervalSecret), 0, Math.max(intervalPlayers, intervalSecret), 0, 100)
    if (percentil >= 95) {
        soundExpression.happy.playUntilDone()
    } else {
        music.playTone(Note.C, 100)
    }
    
    led.plotBarGraph(percentil - (100 - percentil) * 2, 100)
    
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touch() {
    
    intervalPlayers = control.millis()
    control.inBackground(function onIn_background() {
        music.stopAllSounds()
        basic.showIcon(IconNames.Asleep)
    })
    
})
input.onButtonPressed(Button.A, on_button_pressed_a)
input.onButtonPressed(Button.B, on_button_pressed_b)
