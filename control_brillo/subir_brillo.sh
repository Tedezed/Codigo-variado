#!/bin/sh

modificador=30

brillo=$(cat /sys/class/backlight/intel_backlight/brightness)
max_brillo=$(cat /sys/class/backlight/intel_backlight/max_brightness)
brillo=$(expr $brillo + $modificador)

if [ "$brillo" -lt "$max_brillo" ]; then
	echo $brillo > /sys/class/backlight/intel_backlight/brightness
else
	echo $max_brillo > /sys/class/backlight/intel_backlight/brightness
fi