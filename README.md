# TDSRandomizer
A randomization script for Tower Defense Simulator.

**Note:** You need Python 3 installed on your computer to use this script. I'd also recommend using Command Prompt (Windows) or the Terminal (Mac) to run it (simply use `python3 TDSRandomizer.py`).

If you don't have Git installed to clone this repository you can download the script in Releases.

**Understanding the output**

The script prints two arrays. The first array contains the towers you should equip for your loadout. The second array is used for golden skin conditions and simply contains any towers that meet the golden criteria. The script has a 50/50 chance to make any eligible tower golden; this is indicated by prefixing the tower's name with Golden. Here's an example:

`["Farm", "Commander", "Golden Soldier", "Demoman", "Pyromancer"], ["Soldier", "Pyromancer"]`

The script selected two eligible towers and only made one of them golden. Your loadout in this case would be the first table, making only Soldier golden.
