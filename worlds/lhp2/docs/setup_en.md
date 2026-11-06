# SETUP GUIDE FOR LEGO HARRY POTTER 5-7
- --
## Required software
- An unmodified copy of Lego Harry Potter 5-7, either:
  - the original Steam or GOG release
  - or LEGO Harry Potter Collection on Steam (see "Playing on the Collection" below)
- A copy of the APWorld (requires Archipelago version 0.6.7 or higher)
- Reloaded II Mod Loader [Link](https://reloaded-project.github.io/Reloaded-II/QuickStart)
  - Requires .NET 9.0 or higher
- The Lego Harry Potter 5-7 Archipelago Mod [Link](https://github.com/jradcode23/LHP2-Mod/releases)
- --
## Optional Software
- DXWnd [Link](https://sourceforge.net/projects/dxwnd/)
- --
## First Time Setup 
- Install Reloaded II Mod Loader
- Add Lego Harry Potter 5-7 to Reloaded II either through setup or by clicking the + on the left.
  - Must use the exe found in the Steam or GOG Lego Harry Potter folder
  - For the Collection, use the exe in `LHPCR\Years 5-7\harry2.exe`
- If you are using the Steam version or the Collection, we will need to use the ASI loader (optional for GOG version) 
  - Under Lego Harry Potter 5-7, click Edit Application
  - Under "Advanced Tools & Options", make sure that "Don't Inject Loader" is enabled
    - Indicated by the red +
  - Click "Deploy ASI Loader" and then "Okay"
- Navigate to the "Mods" folder in wherever you installed Reloaded II
- Move the LHP2.Archi.Mod folder into the Reloaded II Mods folder
- --
## Connecting to a Multiworld
- In Reloaded II, select the LHP2 Archipelago Mod and click "Configure Mod"
- Fill out the Host IP, Port Number, Slot Name, and Password as applicable
- Ensure that the Archipelago Mod is enabled
  - Indicated by the red +
- Launch the game either in Reloaded II
  - If you are using ASI Loader, launching in DXWnd, Steam, or GOG will also work
- The game will attempt to connect to the server once the menu is loaded
- IT IS IMPORTANT THAT YOU WAIT ON THE MENU UNTIL IT IS CONNECTED
- Start a new game and enjoy
- --
## Playing on the Collection
- Set `GameVersion: collection` in your YAML
  - This adds the 10 extra characters sold at Madam Malkin's as items, and buying them as checks
  - A Collection seed still works on the original game: those purchases are sent automatically
  - A Legacy seed works on the Collection too: those characters then stay locked
- The same mod works on both games, no separate download is needed
- With the ASI loader, you can launch from Steam (pick Years 5-7 in the Collection launcher) or run harry2.exe directly
- --

## Important Notes (Please Read)
- Please read the Lego Harry Potter F.A.Q.S as it has important information that you will need to complete an archipelago.
