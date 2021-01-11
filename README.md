# Pedestrian generator
Generates training data for pedestrian detection models using the ESI Pro-SiVIC simulator.

# Requirements

* ESI Pro-SiVIC.
* Pro-SiVIC DDS install/Release folder in PATH and PYTHONPATH according to DDS instructions.
* Python 3.7 (Pro-SiVIC DDS requirement).
* Only tested on Windows 10.

# Quick start

```
git clone https://github.com/updbqn/pedestrian-generator
```

If python DDS is not already set up, add DDS install folder to path e.g. by running the provided powershell script with admin privileges: 

```
./util/set-prosivic-env-vars.ps1 C:/path/to/DDS/install/Release
```

Copy the scenario in prosivic_scenes to your Pro-SiVIC scripts folder.

Start Pro-SiVIC, then run the scenario:

```
python src/cli.py
```

Captured camera images and pedestrian pixel masks will be saved to:

```
C:/Users/Yourname/Pro-SiVIC/My project/sensors/[date-and-time]/[simulation-id]
```
