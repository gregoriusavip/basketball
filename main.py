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
        basic.pause(20)

def on_button_pressed_a():
    global total_score
    total_score = 0
    countdown(24)
input.on_button_pressed(Button.A, on_button_pressed_a)

def play_basketball():
    global now, distance, total_score, next_ready
    now = input.running_time()
    if now < next_ready:
        return
    distance = PlanetX_Basic.ultrasound_sensor(PlanetX_Basic.DigitalRJPin.J2,
        PlanetX_Basic.Distance_Unit_List.DISTANCE_UNIT_CM)
    if distance > 0 and distance < THRESHOLD_CM:
        total_score += 2
        next_ready = now + COOLDOWN_MS
distance = 0
next_ready = 0
now = 0
start = 0
total_score = 0
display: PlanetX_Display.TM1637LEDs = None
COOLDOWN_MS = 0
THRESHOLD_CM = 0
# SETTINGS
SHOT_CLOCK_SECONDS = 24
THRESHOLD_CM = 8
COOLDOWN_MS = 800
display = PlanetX_Display.tm1637_create(PlanetX_Display.DigitalRJPin.J1)
basic.show_number(total_score)