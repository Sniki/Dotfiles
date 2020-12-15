#!/bin/bash
# baraction.sh for spectrwm status bar by Sniki

## DISK
hdd() {
	hdd="$(df -h | awk 'NR==4{print $3, $5}')"
	echo -e "HDD: $hdd"
}

## RAM
mem() {
	mem=`free | awk '/Mem/ {printf "%dM/%dM\n", $3 / 1024.0, $2 / 1024.0 }'`
	echo -e "MEM: $mem"
}

## CPU
cpu() {
	read cpu a b c previdle rest < /proc/stat
	prevtotal=$((a+b+c+previdle))
	sleep 0.5
	read cpu a b c idle rest < /proc/stat
	total=$((a+b+c+idle))
	cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
	echo -e "CPU: $cpu%"
}

## VOLUME
vol() {
	vol=`amixer get Master | awk -F'[][]' 'END{ print $4":"$2 }' | sed 's/on://g'`
	echo -e "VOL: $vol"
}

## BATTERY 0
bat0() {
	batt="/sys/class/power_supply/BAT0"
	capac="$(cat "$batt"/capacity)"
    	bstatus="$(cat "$batt"/status)"
    	bstat="$(echo "$bstatus" | sed 's/Charging/↑/;s/Discharging/↓/;s/Full//;s/Unknown//')"
	echo "BAT0 $bstat$capac%"
}

## BATTERY 1
bat1() {
	batt="/sys/class/power_supply/BAT1"
	capac="$(cat "$batt"/capacity)"
    	bstatus="$(cat "$batt"/status)"
    	bstat="$(echo "$bstatus" | sed 's/Charging/↑/;s/Discharging/↓/;s/Full//;s/Unknown//')"
	echo "BAT1 $bstat$capac%"
}

## Backlight
bkl() {
	bkl="$(xbacklight -get | awk '{print int($1+0.6)}' | sed 's/\..*//')%"
	echo "BKL: $bkl"
}
    
SLEEP_SEC=1
#loops forever outputting a line every SLEEP_SEC secs

# It seems that we are limited to how many characters can be displayed via
# the baraction script output. And the the markup tags count in that limit.
# So I would love to add more functions to this script but it makes the 
# echo output too long to display correctly.
while :; do
	echo "+@fg=1; $(cpu) | +@fg=2; $(mem) | +@fg=3; $(hdd) | +@fg=4; $(vol) | +@fg=1; $(bat0) | +@fg=2; $(bat1) | +@fg=3; $(bkl) |"
	sleep $SLEEP_SEC
done
