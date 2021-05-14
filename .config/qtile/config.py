# Laptop Qtile Configuration for Laptops by Sniki (Nord Theme)

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"                             # My terminal of choice

keys = [

	 # Volume Control
	 Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 5%+")),
	 Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 5%-")),
	 Key([], "XF86AudioMute", lazy.spawn("amixer sset Master toggle")),
    
	 # Microphone Mute
	 Key([], "XF86AudioMicMute", lazy.spawn("amixer sset Capture toggle")),
         
	 # Brightness Control
	 Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight -inc 5")),
	 Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -dec 5")),
	 
	 # F7 Video Mirror
	 Key([], "XF86Display", lazy.spawn("")),
	 
	 # F8 Wireless / Bluetooth
	 Key([], "XF86WLAN", lazy.spawn("")),
	 
	 # F8 Settings
	 Key([], "XF86Tools", lazy.spawn("alacritty")),
	 
	 # F10 Search
	 Key([], "XF86Search", lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\"")),
	 
	 # F11 Launch Applications
	 Key([], "XF86LaunchA", lazy.spawn("firefox")),
	 
	 # F12 Explorer
	 Key([], "XF86Explorer", lazy.spawn("nautilus")),
	 
	 # Print Screen
	 Key([], "Print", lazy.spawn("scrot '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'")),
	 Key([mod], "Print", lazy.spawn("scrot -s '%Y-%m-%d_$wx$h.png' -e 'mv $f ~/Pictures/Screenshots/'")),
	
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm+" -e fish"),
             desc='Launches My Terminal'
             ),
         Key([mod, "shift"], "Return",
             # lazy.spawn("dmenu_run -p 'Run: '"),
             lazy.spawn("rofi -show drun -config ~/.config/rofi/themes/dt-dmenu.rasi -display-drun \"Run: \" -drun-display-format \"{name}\""),
             desc='Run Launcher'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key(["control", "shift"], "e",
             lazy.spawn("emacsclient -c -a emacs"),
             desc='Doom Emacs'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         # Emacs programs launched using the key chord CTRL+e followed by 'key'
         KeyChord(["control"],"e", [
             Key([], "e",
                 lazy.spawn("emacsclient -c -a 'emacs'"),
                 desc='Launch Emacs'
                 ),
             Key([], "b",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
                 desc='Launch ibuffer inside Emacs'
                 ),
             Key([], "d",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
                 desc='Launch dired inside Emacs'
                 ),
             Key([], "i",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
                 desc='Launch erc inside Emacs'
                 ),
             Key([], "m",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(mu4e)'"),
                 desc='Launch mu4e inside Emacs'
                 ),
             Key([], "n",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
                 desc='Launch elfeed inside Emacs'
                 ),
             Key([], "s",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
                 desc='Launch the eshell inside Emacs'
                 ),
             Key([], "v",
                 lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
                 desc='Launch vterm inside Emacs'
                 )
         ]),
         # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
         KeyChord([mod], "p", [
             Key([], "e",
                 lazy.spawn("./dmscripts/dmconf"),
                 desc='Choose a config file to edit'
                 ),
             Key([], "i",
                 lazy.spawn("./dmscripts/dmscrot"),
                 desc='Take screenshots via dmenu'
                 ),
             Key([], "k",
                 lazy.spawn("./dmscripts/dmkill"),
                 desc='Kill processes via dmenu'
                 ),
             Key([], "l",
                 lazy.spawn("./dmscripts/dmlogout"),
                 desc='A logout menu'
                 ),
             Key([], "m",
                 lazy.spawn("./dmscripts/dman"),
                 desc='Search manpages in dmenu'
                 ),
             Key([], "o",
                 lazy.spawn("./dmscripts/dmqute"),
                 desc='Search your qutebrowser bookmarks and quickmarks'
                 ),
             Key([], "r",
                 lazy.spawn("./dmscripts/dmred"),
                 desc='Search reddit via dmenu'
                 ),
             Key([], "s",
                 lazy.spawn("./dmscripts/dmsearch"),
                 desc='Search various search engines via dmenu'
                 ),
             Key([], "p",
                 lazy.spawn("passmenu"),
                 desc='Retrieve passwords with dmenu'
                 )
         ])
]

group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

layout_theme = {"border_width": 1,
                "margin": 15,
                "border_focus": "81a1c1",
                "border_normal": "5e81ac"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 11,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 12,
         border_width = 2,
         bg_color = "3b4252",
         active_bg = "5e81ac",
         active_fg = "ffffff",
         inactive_bg = "81a1c1",
         inactive_fg = "ffffff",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 200
         ),
    layout.Floating(**layout_theme)
]

colors = [["#3b4252", "#3b4252"], # panel background
          ["#3d3f4b", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#5e81ac", "#5e81ac"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#81a1c1", "#81a1c1"], # color for the 'even widgets'
          ["#eceff4", "#eceff4"], # window name
          ["#eceff4", "#eceff4"], # backbround for inactive screens
          ["#3b4252", "#3b4252"]] # GroupBox Color

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Image(
                       filename = "~/.config/qtile/icons/python-white.png",
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn('rofi -show drun -config ~/.config/rofi/themes/dt-center.rasi -display-drun \"Run: \" -drun-display-format \"{name}\"')},
                       background = colors[5],
                       scale = True,
                       margin = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 15,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 5,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[4],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[4]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[1],
                       padding = 0,
                       fontsize = 59
                       ),         
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[3],
                       background = colors[1]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[0],
                       background = colors[0]
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[0],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.Wlan(
             	       format = ' {essid} - {percent:2.0%} ',
		       interface = 'wlp4s0',
		       disconnected_message = 'Disconnected',
		       background = colors[4],
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.OpenWeather(
              	       cityid = 788652,
              	       #format = '{location_city}: {main_temp} °{units_temperature} {weather_details} ',
              	       format = '{main_temp} °{units_temperature} {weather_details} ',
              	       metric = True,
              	       background = colors[5],
              	       fontsize = 14,
              	       #mouse_callbacks = 'https://openweathermap.org/city/788652'
              	       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.TextBox(
		       text='☀',
		       background = colors[4],
		       foreground = colors[2],
		       padding = 0,
		       fontsize = 22
		       ),
              widget.Backlight(
		       background = colors[4],
		       backlight_name="intel_backlight",
		       format = '{percent: 5.0%}  ',
		       padding = -5,
		       ),
              widget.TextBox(
                       text='',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 59
                       ),         
              widget.Battery(
		       battery = 0,
		       charge_char = '',
		       discharge_char = '',
		       empty_char = '',
		       full_char = '',
		       unknown_char = '',
		       #unknown_char = '',
		       low_percentage = 0.1,
		       format = ' {char} {percent:2.0%} ',
		       #format = ' {char} {percent:2.0%} {hour:d}:{min:02d} ',
		       show_short_text = False,
		       background = colors[5],
		       padding = 0,
		       ),         
	      widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 59
                       ),
	      widget.Battery(
		       battery = 1,
		       charge_char = '',
		       discharge_char = '',
		       empty_char = '',
		       full_char = '',
		       unknown_char = '',
		       #unknown_char = '',
		       low_percentage = 0.1,
		       format = ' {char} {percent:2.0%} ',
		       #format = ' {char} {percent:2.0%} {hour:d}:{min:02d} ',
		       show_short_text = False,
		       background = colors[4],
		       padding = 0,
		       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.TextBox(
                       text = "🖴",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[5],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                       fontsize = 14,
                       padding = 5
                       ),
              widget.TextBox(
                       text='',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.TextBox(
                       text = "",
                       padding = 0,
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14
                       ),
              widget.BitcoinTicker(
                       foreground = colors[2],
                       background = colors[4],
                       fontsize = 14,
                       padding = 5
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.TextBox(
                      text = "",
                       foreground = colors[2],
                       background = colors[5],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Volume(
                       foreground = colors[2],
                       background = colors[5],
                       padding = 5,
                       fontsize = 14
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[5],
                       foreground = colors[4],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[0],
                       background = colors[4],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[4],
                       padding = 5,
                       fontsize = 14
                       ),
              widget.TextBox(
                       text = '',
                       background = colors[4],
                       foreground = colors[5],
                       padding = 0,
                       fontsize = 59
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[5],
                       format = "%A, %B %d - %H:%M ",
                       fontsize = 14
                       ),
             #widget.TextBox(
             #          text = '',
             #          background = colors[5],
             #          foreground = colors[4],
             #          padding = 0,
             #          fontsize = 59
             #          ),
             #widget.TextBox(
             # 	       text = "⏻",
             # 	       background = colors[4],
             #          foreground = colors[2],
             #          #font="Font Awesome 5 Free Solid",
             #          fontsize = 17,
             #          padding = 17,
             #          mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("./.config/rofi/powermenu/powermenu.sh")},
             #          ),
             #widget.Systray(
             #          background = colors[4],
             #          #icon_size = 25,
             #          padding = 50
             #          ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=30)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=30)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=30))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='Org.gnome.Nautilus'), # Nautilus File Manager
    Match(wm_class='Gnome-calculator'),  # Gnome Calculator   
])

auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
