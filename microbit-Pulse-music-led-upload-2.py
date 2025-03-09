def on_wifi_connect(IP_Address, Device_ID):
    basic.show_icon(IconNames.CHESSBOARD)
WiFiIoT.on_wifi_connect(on_wifi_connect)

def on_thingspeak_conn(Status, Error_code):
    basic.show_icon(IconNames.HOUSE)
    basic.show_string(Error_code)
WiFiIoT.on_thingspeak_conn(on_thingspeak_conn)

WiFiIoT.initialize_wifi(SerialPin.P16, SerialPin.P8)
WiFiIoT.set_wifi("pixel", "97293183")
strip = neopixel.create(DigitalPin.P2, 60, NeoPixelMode.RGB)
item = 0
sum2 = 0
basic.show_icon(IconNames.YES)

def on_every_interval():
    global item, sum2
    item = 0
    sum2 = 0
    basic.pause(10000)
    basic.show_number(sum2 * 6)
    if sum2 * 6 >= 96:
        basic.show_icon(IconNames.ANGRY)
        basic.clear_screen()
        music.play(music.string_playable("G E E F D D C C ", 75),
            music.PlaybackMode.UNTIL_DONE)
        strip.show_rainbow(50, 200)
        strip.clear()
    elif sum2 * 6 >= 80:
        basic.show_icon(IconNames.SURPRISED)
        basic.clear_screen()
        music.play(music.string_playable("F E D G E D E C ", 80),
            music.PlaybackMode.UNTIL_DONE)
        strip.show_rainbow(50, 150)
        strip.clear()
    elif sum2 * 6 >= 65:
        basic.show_icon(IconNames.HAPPY)
        basic.clear_screen()
        music.play(music.string_playable("C D E C D G G - ", 100),
            music.PlaybackMode.UNTIL_DONE)
        strip.show_rainbow(1, 360)
        strip.clear()
    elif sum2 * 6 >= 50:
        basic.show_icon(IconNames.ASLEEP)
        basic.clear_screen()
        music.play(music.string_playable("C D E G A A B C5 ", 75),
            music.PlaybackMode.UNTIL_DONE)
        strip.show_rainbow(1, 120)
        strip.clear()
    else:
        basic.show_icon(IconNames.NO)
        basic.clear_screen()
        music.play(music.string_playable("C5 - C5 - C5 - - - ", 120),
            music.PlaybackMode.UNTIL_DONE)
        strip.show_rainbow(1, 2)
        strip.clear()
    if WiFiIoT.is_wifi_connect():
        WiFiIoT.send_thingspeak("19Q6HHNLRQ2SN4A5", sum2 * 6)
        basic.pause(15000)
loops.every_interval(60000, on_every_interval)

def on_forever():
    global item, sum2
    item = pins.digital_read_pin(DigitalPin.P1)
    if 1 == item:
        sum2 += 1
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
basic.forever(on_forever)
