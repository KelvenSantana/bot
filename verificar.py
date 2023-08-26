import pygetwindow as gw
import pyautogui
import cv2
import numpy as np

def find_bluestacks_window():
    bluestacks_title = "MSI App Player"
    try:
        bluestacks_window = gw.getWindowsWithTitle(bluestacks_title)[0]
        return bluestacks_window
    except IndexError:
        return None

def take_screenshot_bluestacks(region):
    bluestacks_window = find_bluestacks_window()
    if bluestacks_window:
        bluestacks_window.activate()
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save("bluestacks_screenshot.png")
        print("Captura de tela do Bluestacks realizada com sucesso.")
    else:
        print("Janela do Bluestacks não encontrada.")

def find_image_on_screen(template_path, screenshot_path, threshold=0.35):
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    screenshot = cv2.imread(screenshot_path, cv2.IMREAD_GRAYSCALE)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    return locations

if __name__ == "__main__":
    # Capture a tela inteira do Bluestacks
    bluestacks_window = find_bluestacks_window()
    if bluestacks_window:
        take_screenshot_bluestacks((bluestacks_window.left, bluestacks_window.top, bluestacks_window.width, bluestacks_window.height))
    else:
        print("Janela do Bluestacks não encontrada.")

    template_image_path = "berm.png"  # Substitua pelo caminho da imagem que você deseja encontrar
    screenshot_path = "bluestacks_screenshot.png"

    match_locations = find_image_on_screen(template_image_path, screenshot_path)

    if match_locations:
        print("Imagem encontrada nas posições:", match_locations)
        # Realize a ação desejada quando a imagem for encontrada.
    else:
        print("Imagem não encontrada.")
