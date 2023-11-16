# Screen_Display_Resolution

The given python script aims to manage the display resolution on a linux system using the 'xrandr' command-line utility. It allows users to identify connected displays, check their current resolutions,
and set the resolution to the highest supported one(1920x1080 by default) if necessary. 

The script comprises the following key components:

1. Importing Modules: The script starts by importing the necessary modules:
- subprocess: For running external commands and capturing their input
- re: For performing regular expression pattern matching
- time: For introducing delays in the script.
- os: For accessing environment variables

2. Function 'get_connected_displays()': This function retrieves a list of connected displays by running the 'xrandr' command.It processes the command's output, looking for lines containing "connected"
   and extracts the display names

3. Function 'get_active_display()': This function determines the active display (marked as "primary" in the 'xrandr' output). It returns the name of the active display.

4. Function 'get_current_resolution(display)': This function retreives the current resolution (width and height) of a specific display. It runs 'xrandr' with the appropriate environment variable
  and processes the output using regular expressions to find the resolution

5. Function 'set_screen_resolution(display,width,height)': This function sets the screen resolution for a specific display using the 'xrandr' command with the appropriate arguments.

6. Function 'main': The main function orchestrates the entire process of identifying connected displays, checking their current resolutions and adjusting the resolution if needed. It follows these
   steps:
   - Get connected displays and print them
   - Determine the active display and print it.
   - Get the current resolution of the active display and print it
   - Check if the current resolution matches the highest supported resolution(1920x1080 by default)
   - If not, set the resolution to the highest supported one and print a success message
   - Introduce a 2-second display to allow the resolution to take effect.
  
   The script utilizes exception handling to catch any errors that may occur during the executions of the functions and displays an error message.

   The code also contains a conditional block at the end to execute the 'main()' function only if the script is running directly (not imported as a module).

   After checking the resolutions using xrandr command then run these command to automatically resize the screen to the best resolution display -> xrandr --output eDP-1 --mode 1920x1080
