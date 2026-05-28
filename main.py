def countdown(seconds: number):
    global start
    start = input.running_time()
    while True:
        elapsed = Math.idiv(input.running_time() - start, 1000)
        remaining = seconds - elapsed
        display.show_number(remaining)
        if remaining <= 0:
            display.show_number(0)
            break
        play_basketball()

def on_button_pressed_a():
    countdown(24)
input.on_button_pressed(Button.A, on_button_pressed_a)

def play_basketball():
    global distance, total_score
    distance = PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J2,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM)
    if distance > 0 and distance < THRESHOLD_CM:
        total_score += 2
        basic.show_number(total_score)
        basic.pause(COOLDOWN_MS)
total_score = 0
distance = 0
start = 0
display: PlanetX_Display.TM1637LEDs = None
COOLDOWN_MS = 0
THRESHOLD_CM = 0
# SETTINGS
SHOT_CLOCK_SECONDS = 24
THRESHOLD_CM = 8
COOLDOWN_MS = 200
display = PlanetX_Display.tm1637_create(PlanetX_Display.DigitalRJPin.J1)