"""
To run python script:
	YOU MUST HAVE INSTALLED PYTHON3 OR GREATER
	Linux: python3 stats.py
	Windows:

Steps To Run:
	1. Install Python3
	2. Download and save this python script(stats.py) to computer
	3. Create a text-file named "sqstats"
	4. Coppy List of cadets from EServices and save file in the same
	   Directory that contsins the "stats.py" program
	5. Run using commands above
	6. View output and enjoy!
"""


file1 = open('sqstats', 'r')
Lines = file1.readlines()
z = 0


ranksHead = ["CADETS", "Airman", "Airman First Class", "Senior Airman", "Staff Sgt.", "Tech Sgt.", "Master Sgt.", "Senior Master Sgt.", "Chief Master Sgt.", "2dLt", "First Lt.", "Captain", "Major", "Lt Colonel", "Colonel"]
ranksUsed = ["CADET", "Amn", "A1C", "SrA", "SSgt", "TSgt", "MSgt", "SMSgt", "CMSgt", "2ndLt", "1stLt", "C/Capt", "C/Maj", "LtCol", "C/Col"]


def percentage(part, whole):
	Percentage = 100 * float(part)/float(whole)
	return str(round(Percentage, 1)) + "%"
	
class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

#Main Counter for detailed list
for x in ranksUsed:
	y = 0		#Counts how many cadets are at each rank (Amn, Sgt....)
	print()
	print(color.BLUE + ranksHead[z] + color.END)	#Prints the title of the list below it
	print()
	for line in Lines:
		if x in line:
			y += 1
			print(str(y) + "  " + line)	#Prints cadets CAPID, Rank, and full name listed in EServices
	z = z + 1


#Essentilly the same thing but prints a quick overview of squadron in percentages
for x in ranksUsed:
	count = 0
	y = 0
	for line in Lines:
		count += 1
		if x in line:
			y += 1
	print(x + ": " + str(y) + "/" + str(count) + " : " + percentage(y, count))
