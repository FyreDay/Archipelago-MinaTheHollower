
## Required Software

- [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases).
- A Legal steam copy of Mina the Hollower

## Installation Procedures

### Install Archipelago
Download and install [Archipelago](<https://github.com/ArchipelagoMW/Archipelago/releases/latest>). **The installer 
   file is located in the assets section at the bottom of the version information.**
### Install the AP world
1. Download the [Latest AP World release here](https://github.com/FyreDay/Archipelago-MinaTheHollower/releases/latest)
2. Double click the ap world to install it to your archipelago. 
3. Restart the archipelago program for Mina the Hollower to show up.
4. Use the options creator to create a yaml, or modify the supplied one on github releases

## If Playing
Send your yaml to whoever is hosting your AP world. You will also have to send them the .apworld or a link to download the .apworld

## If Hosting
6. Put the yaml in the **Players** folder in your AP files and all other yamls for players you with to play with
7. Run generate
8. Go to archipelago.gg and host the game. select the generated zip in **/output/**

If this is confusing go the official archipelago discord for help

### Windows Install
1. Download the [Latest Mod Release](https://github.com/Axertin/mth-apclient/releases/latest). The mod will be a zip file with your OS name

2. Unzip the mod.zip (containing a `apclient` folder with a `mod.dll` and `mod.yc`) inside into:

```
%APPDATA%\Yacht Club Games\Mina the Hollower\mods
```
so that the .dll and .yc files are in
```
%APPDATA%\Yacht Club Games\Mina the Hollower\mods\apclient\
```
3. Switch to the **experimental-modding Beta** beta on steam
   If you have not switched steam betas before
   1. navigate to Steam->Mina The Hollower->Properties->Game Versions & Betas
   2. Select `experimental-modding` in the version list
   
4. Set Steam launch options for Mina the Hollower to:

```
-mod -mod-allow-code
```
(this enables loading a mod's code library)

The game's mod loader writes `%APPDATA%\Yacht Club Games\Mina the Hollower\mod.log` each run;
the mod's own runtime log is `%LOCALAPPDATA%\mth-apclient\mthap_*.log`.

### Linux Install

1. Download the [Latest Mod Release](https://github.com/Axertin/mth-apclient/releases/latest). The mod will be a zip file with your OS name

2. Unzip the mod.zip (containing a `apclient` folder with a `mod.so` and `mod.yc`) inside into:, 

```
~/.local/share/Yacht Club Games/Mina the Hollower/mods
```
so that the .dll and .yc files are in
```
~/.local/share/Yacht Club Games/Mina the Hollower/mods/apclient/
```
3. Switch to the **experimental-modding Beta** beta on steam
   If you have not switched steam betas before
   1. navigate to Steam->Mina The Hollower->Properties->Game Versions & Betas
   2. Select `experimental-modding` in the version list
   
4. Set Steam launch options for Mina the Hollower to:

```
-mod -mod-allow-code
```
(this enables loading a mod's code library)

The game's mod loader writes `~/.local/share/Yacht Club Games/Mina the Hollower/mod.log` each
run (whether a mod loaded, version-check or load failures) - check it first if the mod doesn't
appear. The mod's own runtime log is `~/.local/share/mth-apclient/mthap_*.log` (one file per run).

## Running
An ImGui overlay window should appear allowing connection and disconnection to an AP server. If it
doesn't appear or you want to hide it once connected, it can be toggled by pressing `F2`.

You will see "disconnected" instead of "Start Game" until you are connected to a multiworld.

You will automatically load into a save once you click "Start game"

## Debugging

There is also a console you can access by presssing **F1**. type ```help``` to see commands
