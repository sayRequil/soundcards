import os
import pygame

packages = []

class soundcard:
  def __init__(name="",description="",author="",filetype=".mp4",sound="sound",package=["soundcard","sound"],build=False):
    # name: Name of the soundcard.
    # description: A short description describing the soundcard.
    # filetype: The type of sound file.
    # package: The package name. Example for others than soundcard: ["mysound","sound"] Which would mean the folder it is in, and the name of the sound.
    if build == False:
      diri = package[0]
      file = package[1] + filetype
      path = os.path.join(package,file)
      packages.append(path)
      n = open(os.path.join(package[0],"name.scd"),"a")
      n.write(name)
      d = open(os.path.join(package[0],"desc.scd"),"a")
      d.write(desc)
      n.close()
      d.close()
      
    if build == True:
      i = 0
      for pack in packages:
        i = i+1
        p = os.path.join("cards_","card" + i)
        card = open(p,"a")
        card.write(name + " " + description + " " + author + "" + filetype + " " + sound + " " + package[0]) # Example: soundname sounddesc soundauthor mp4 sound soundcard
    
  def play(name="")
    for r, d, f in os.walk("cards_")
      c = open(f,"r")
      data = c.split()
      if data[0] == name:
        print("Playing " + data[0] + " by " + data[2]) # Credits
        sound = data[4] + data[3]
        package = data[4]
        path = os.path.join(package,sound)
        pygame.mixer.music.load(path)
        
