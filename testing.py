import subprocess
import re
import time
import os

def get_connected_displays():
    cmd = ["xrandr"]
    output = subprocess.check_output(cmd).decode().strip().split("\n")
    connected_displays = []
    for line in output:
        if " connected" in line:
            display_name = line.split()[0]
            connected_displays.append(display_name)
    return connected_displays

def get_active_display():
    output = subprocess.check_output(["xrandr"])
    lines = output.decode().strip().split("\n")
    for line in lines:
        if " connected primary" in line:
            return line.split()[0]
    if lines:
        return lines[0].split()[0]
    raise ValueError("No connected displays found.")

def get_current_resolution(display):
    cmd = ["xrandr"]
    output = subprocess.check_output(cmd, env={"DISPLAY": os.environ["DISPLAY"]}).decode().strip().split("\n")
    pattern = rf"{display}\s+connected\s+(\d+x\d+)\s+"
    for line in output:
        match = re.search(pattern, line)
        if match:
            resolution = match.group(1)
            return tuple(map(int, resolution.split("x")))
    raise ValueError(f"No connected display '{display}' found.")


def set_screen_resolution(display, width, height):
    resolution = f"{width}x{height}"
    subprocess.run(["xrandr", "--output", display, "--mode", resolution])


def main():
    try:
        # Get connected displays
        connected_displays = get_connected_displays()
        print("Connected Displays:", connected_displays)

        # Get the highest supported resolution
        highest_width, highest_height = 1920, 1080  # Replace with your desired resolution

        # Get the active display or the first connected display
        active_display = get_active_display()
        print("Active Display:", active_display)

        # Get current screen resolution for the active display
        current_width, current_height = get_current_resolution(active_display)

        # Check if the current resolution is the highest supported resolution
        if (current_width, current_height) == (highest_width, highest_height):
            print(f"The display '{active_display}' is already set to the highest supported resolution.")
        else:
            print(f"Current resolution for display '{active_display}': {current_width}x{current_height}")
            print(f"Adjusting resolution to fit the screen: {highest_width}x{highest_height}...")
            set_screen_resolution(active_display, highest_width, highest_height)

        # Give some time for the resolution to take effect
        time.sleep(2)

        print("Resolution adjusted successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
