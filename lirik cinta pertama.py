import sys
from time import sleep
import time 

def print_lyrics():
    lines = [
        ("satu hari tidak bertemu", 0.04),
        ("dan rindupun menggebu-gebu", 0.04),
        ("rasa ingin bersua dan selalu bersama", 0.04),
        ("walau hanya untuk sekejap", 0.05),
        ("bertemupun hanya sekejap namun terobat rindu", 0.04),
        ("inilah yang ku rasakan saat ini ku rasakan", 0.05),
        ("Mataku tak mau pejam", 0.05),
        ("makanpun tak pernah kenyang", 0.04)
    ]
    delays = [0.4, 1.5, 2.8, 2.4, 5, 3, 1, 1, 1, 1]    

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')    

print_lyrics()
        
           
