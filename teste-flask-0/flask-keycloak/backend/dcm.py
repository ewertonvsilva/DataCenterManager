import serial

def sendPs2Key (data):
    # For special characters, we sum 2k to the real value to differenciate on the arduino
    strPs2ScanCodeDictionary = {
        "ArrowUp":"2117",
        "ArrowDown":"2114",
        "ArrowLeft":"2107",
        "ArrowRight":"2116",
        "Delete":"2113",
        "Enter":"90",
        "Escape":"118",
        "Backspace":"102",
        "F1":"5",
        "F2":"6",
        "F3":"4",
        "F4":"12",
        "F5":"3",
        "F6":"11",
        "F7":"131",
        "F8":"10",
        "F9":"1",
        "F10":"9",
        "F11":"120",
        "F12":"7",
#         "SCROLL_LOCK":"126",
#         "ACCENT":"14",
#         "SEVEN":"61",
#         "EIGHT":"62",
#         "NINE":"70",
#         "ZERO":"69",
#         "MINUS":"78",
#         "EQUAL":"85",
        "Tab":"13",
        "Q":"21",
        "W":"29",
        "E":"36",
        "R":"45",
        "T":"44",
        "Y":"53",
        "U":"60",
        "I":"67",
        "O":"68",
        "P":"77",
        "q":"21",
        "w":"29",
        "e":"36",
        "r":"45",
        "t":"44",
        "y":"53",
        "u":"60",
        "i":"67",
        "o":"68",
        "p":"77",
        "[":"84",
        "]":"91",
        "\\":"93",
        "CapsLock":"88",
        "A":"28",
        "S":"27",
        "D":"35",
        "F":"43",
        "G":"52",
        "H":"51",
        "J":"59",
        "K":"66",
        "L":"75",
        "a":"28",
        "s":"27",
        "d":"35",
        "f":"43",
        "g":"52",
        "h":"51",
        "j":"59",
        "k":"66",
        "l":"75",
        ";":"76",
        "'":"82",
        "Shift":"18",
        "Z":"26",
        "X":"34",
        "C":"33",
        "V":"42",
        "B":"50",
        "N":"49",
        "M":"58",
        "z":"26",
        "x":"34",
        "c":"33",
        "v":"42",
        "b":"50",
        "n":"49",
        "m":"58",
        ",":"65",
        ".":"73",
        "/":"74",
        "Shift":"89",
        "Control":"20",
        "Alt":"17",
        " ":"41",
        "NumLock":"119",
        "*":"124",
        "-":"123",
        "+":"121",
         ",":"113",
#---
        "1":"22",
        "2":"30",
        "3":"38",
        "4":"37",
        "5":"46",
        "6":"54",
        "7":"61",
        "8":"62",
        "9":"70",
        "0":"69",
        "OS":"2031",
        # "RIGHT_ALT":""17",
        # "RIGHT_WIN":""39",
        # "MENUS":""47",
        # "RIGHT_CONTROL":""20",
         "insert":"2112",
         "home":"2108",
        # "PAGE_UP":""125",
        # "DELETE":""113",
        # "END":""105",
        # "PAGE_DOWN":""122",
        # "UP_ARROW":""117",
        # "LEFT_ARROW":""107",
        # "DOWN_ARROW":""114",
        # "RIGHT_ARROW":""116",
        # "DIVIDE":""74",
        # "NUMPAD_ENTER":""90",
        # "NEXT_TRACK":""77",
        # "PREVIOUS_TRACK":""21",
        # "STOP":""59",
        # "PLAY_PAUSE":""52",
        # "MUTE":""35",
        # "VOLUME_UP":""50",
        # "VOLUME_DOWN":""33",
        # "MEDIA_SELECT":""80",
        # "EMAIL":""72",
        # "CALCULATOR":""43",
        # "MY_COMPUTER":""64",
        # "WWW_SEARCH":""16",
        # "WWW_HOME":""58",
        # "WWW_BACK":""56",
        # "WWW_FORWARD":""48",
        # "WWW_STOP":""40",
        # "WWW_REFRESH":""32",
        # "WWW_FAVORITES":""24",
        # "POWER":""94",
        # "SLEEP":""95",
        # "WAKE":""99",
        "=":"85"
        }

    print(strPs2ScanCodeDictionary[data])
    ser = serial.Serial('/dev/ttyUSB0', 9600)
    ser.write(strPs2ScanCodeDictionary[data].encode())

