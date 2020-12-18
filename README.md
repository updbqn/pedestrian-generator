# Pedestrian generator
Generates training data for pedestrian detection models using the ESI Pro-SiVIC simulator.

# Requirements

* Python 3.7 (Pro-SiVIC DDS requirement).
* Pro-SiVIC DDS install/Release folder must be added to PATH and PYTHONPATH according to DDS instructions.

# Quick start

```
git clone https://github.com/updbqn/pedestrian-generator
```

If python DDS is not already set up, add DDS install folder to path e.g. by running the provided powershell script with admin privileges: 

```
./util/set-prosivic-env-vars.ps1 C:/path/to/install/Release
```

Copy the scenario in prosivic_scenes to your Pro-SiVIC scripts folder.

Run the scenario:

```
python src/cli.py
```
