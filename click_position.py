
from pynput import mouse
from pynput.mouse import Button

def on_click(x, y, button, pressed):
    if pressed and button == Button.left:
        print(f"Click sinistro a posizione: ({x}, {y})")


with mouse.Listener(on_click=on_click) as listener:
    print("Ascolto solo i click sinistri... (CTRL+C per uscire)")
    listener.join()
