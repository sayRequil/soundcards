import os

packages = []

class soundcard:
  def __init__(name="",description="",filetype="mp4",sound="sound",package=["soundcard","sound"]):
    # name: Name of the soundcard.
    # description: A short description describing the soundcard.
    # filetype: The type of sound file.
    # package: The package name. Example for others than soundcard: ["mysound","sound"] Which would mean the folder it is in, and the name of the sound.
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
    
  def build():
    for 
