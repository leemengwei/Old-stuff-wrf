#!/bin/bash
echo "Making Hourly GIF...."
#convert -delay 0 Hourly_png/Hourly_Rainfall_from_start\ *.png -loop 0 Hourly_Out.gif
echo "Making Daily GIF...."
convert -delay 0 Daily_png/Daily_Rainfall_from_start\ *.png -loop 0 Daily_Out.gif
