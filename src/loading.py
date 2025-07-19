import flet as ft
import time
import random
import threading
import genImage
import generated

generationComplete = False

def generate_thread(page, navDrawer, prompt: str, res: str):
    global generationComplete
    genImage.generate(prompt)
    generationComplete = True

def monitor_generation(page, navDrawer, prompt, res):
    global generationComplete
    while not generationComplete:
        time.sleep(0.01)

    generated.screen(page, navDrawer, prompt)

RandomActivities = [
    "Adjust your posture — sit up straight and relax your shoulders.",
    "Blink slowly to moisturize your eyes.",
    "Look away from the screen for 20 seconds — try the 20-20-20 rule!",
    "Roll your neck gently from side to side.",
    "Stretch your wrists and fingers for a few seconds.",
    "Take a sip of water — staying hydrated helps focus.",
    "Do 5 shoulder rolls — forward and backward.",
    "Stretch your arms overhead and take a deep breath.",
    "Gently massage your temples or the back of your neck.",
    "Check that your feet are flat on the floor and not crossed.",
    "Close your eyes and take 3 slow, deep breaths.",
    "Relax your jaw — unclench your teeth.",
    "Check your screen brightness and adjust if needed.",
    "Quickly clean your keyboard or mouse with a cloth.",
    "Place your hands over your eyes for 10 seconds to reduce strain.",
    "Wiggle your toes and shift your leg position.",
    "Sit back in your chair and relax for a moment.",
    "Do a seated twist — gently rotate your torso left and right.",
    "Reach out and stretch your back by pushing your hands forward.",
    "Roll your eyes in circles to ease eye fatigue."
]

def set_random_activity(page: ft.Page, acSug: ft.Text):
    suggestion = random.choice(RandomActivities)
    while suggestion == acSug.value:
        suggestion = random.choice(RandomActivities)
    acSug.value = "While we generate the pictue feel free to: " +  suggestion
    page.update()

def animate_text(lt: ft.Text, page: ft.Page):
    while True:
        for dots in [".", "..", "..."]:
            lt.value = f"Generating{dots}"
            time.sleep(0.8)
            page.update()

def screen(page: ft.Page, navDrawer, prompt, res):
    global generationComplete
    generationComplete = False  # Reset flag

    page.clean()
    page.title = "Wallpaper AI - generating!"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = "#1B2729"

    loadingText = ft.Text("Generating...", size=30, color=ft.Colors.WHITE, weight="bold")
    spinner = ft.ProgressRing(color=ft.Colors.CYAN, width=60, height=60)
    activitySuggestion = ft.Text("While we generate the pictue feel free to: " + random.choice(RandomActivities), color=ft.Colors.WHITE)

    loadingRow = ft.Column(
        [
            spinner,
            ft.Container(height=20),
            loadingText,
            activitySuggestion,
            ft.IconButton(ft.Icons.REFRESH, on_click= lambda a: set_random_activity(page, activitySuggestion))
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(loadingRow)

    # Start generation thread
    gen_thread = threading.Thread(target=generate_thread, args=(page, navDrawer, prompt, res), daemon=True)
    gen_thread.start()

    # Start animation thread
    animation_thread = threading.Thread(target=animate_text, args=(loadingText, page), daemon=True)
    animation_thread.start()

    # Start monitor thread
    monitor_thread = threading.Thread(target=monitor_generation, args=(page, navDrawer, prompt, res), daemon=True)
    monitor_thread.start()
