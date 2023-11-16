#!/bin/bash

# Get the name of the active display
active_display=$(xrandr | grep " connected primary" | awk '{print $1}')
if [ -z "$active_display" ]; then
    active_display=$(xrandr | grep " connected" | head -n 1 | awk '{print $1}')
fi

if [ -z "$active_display" ]; then
    echo "No connected displays found."
    exit 1
fi

echo "Active Display: $active_display" 

# Find and set the highest resolution
desired_resolution=$(xrandr | grep -oP '\d{3,4}x\d{3,4}' | sort -t 'x' -k1,1nr -k2,2nr | head -n 1)

# Get the current resolution for the active display
current_resolution=$(xrandr | grep "$active_display" | awk '{print $4}')
echo "Current Resolution: $current_resolution"

# Adjust resolution
if [ "$current_resolution" = "$desired_resolution" ]; then
    echo "The display '$active_display' is already set to the desired resolution."
else
    echo "Adjusting resolution to fit the screen: $desired_resolution..."
    xrandr --output "$active_display" --mode "$desired_resolution"
    sleep 2
    echo "Resolution adjusted successfully."
fi
