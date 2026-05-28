function countdown (seconds: number) {
    let elapsed: number;
let remaining: number;
start = input.runningTime()
    while (true) {
        elapsed = Math.idiv(input.runningTime() - start, 1000)
        remaining = seconds - elapsed
        display.showNumber(remaining)
        if (remaining <= 0) {
            display.showNumber(0)
            break;
        }
        play_basketball()
        basic.pause(20)
    }
}
input.onButtonPressed(Button.A, function () {
    countdown(24)
})
function play_basketball () {
    now = input.runningTime()
    if (now < next_ready) {
        return
    }
    distance = PlanetX_Basic.ultrasoundSensor(PlanetX_Basic.DigitalRJPin.J2, PlanetX_Basic.Distance_Unit_List.Distance_Unit_cm)
    if (distance > 0 && distance < THRESHOLD_CM) {
        total_score += 2
        basic.showNumber(total_score)
        next_ready = now + COOLDOWN_MS
    }
}
let total_score = 0
let distance = 0
let next_ready = 0
let now = 0
let start = 0
let display: PlanetX_Display.TM1637LEDs = null
let COOLDOWN_MS = 0
let THRESHOLD_CM = 0
// SETTINGS
let SHOT_CLOCK_SECONDS = 24
THRESHOLD_CM = 8
COOLDOWN_MS = 800
display = PlanetX_Display.tm1637Create(PlanetX_Display.DigitalRJPin.J1)
