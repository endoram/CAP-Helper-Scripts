file1 = open('stats', 'r')
Lines = file1.readlines()


CADET = 0
Amn = 0
A1C = 0
SrA = 0
SSgt = 0
TSgt = 0
MSgt = 0
SMSgt = 0
CMSgt = 0
twodLt = 0
firststLt = 0
Capt = 0
Maj = 0
LtCol = 0
Col = 0


count = 0
# Strips the newline character
print("CADETS")
print()
for line in Lines:
	count += 1
	if "CADET" in line:
		CADET += 1
		print(line + "  " + str(CADET))



count = 0
print()
print("Airman")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "Amn" in line:
		Amn += 1
		print(line + "  " + str(Amn))

count = 0
print()
print("Airman First Class")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "A1C" in line:
		A1C += 1
		print(line + "  " + str(A1C))

count = 0
print()
print("Senior Airman")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "SrA" in line:
		SrA += 1
		print(line + "  " + str(SrA))

count = 0
print()
print("Staff Sgt.")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "SSgt" in line:
		SSgt += 1
		print(line + "  " + str(SSgt))

count = 0
print()
print("Tech Sgt.")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "TSgt" in line:
		TSgt += 1
		print(line + "  " + str(TSgt))

count = 0
print()
print("Master Sgt.")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "C/MSgt" in line:
		MSgt += 1
		print(line + "  " + str(MSgt))

count = 0
print()
print("Senior Master Sgt.")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "SMSgt" in line:
		SMSgt += 1
		print(line + "  " + str(SMSgt))

count = 0
print()
print("Chief Master Sgt.")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "CMSgt" in line:
		CMSgt += 1
		print(line + "  " + str(CMSgt))

count = 0
print()
print("2dLt")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "2dLt" in line:
		twodLt += 1
		print(line + "  " + str(twodLt))

count = 0
print()
print("First Lt.")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "1stLt" in line:
		firststLt += 1
		print(line + "  " + str(firststLt))

count = 0
print()
print("Captain")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "C/Capt" in line:
		Capt += 1
		print(line + "  " + str(Capt))

count = 0
print()
print("Major")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "C/Maj" in line:
		Maj += 1
		print(line + "  " + str(Maj))

count = 0
print()
print("Lt Colonel")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "LtCol" in line:
		LtCol += 1
		print(line + "  " + str(LtCol))

count = 0
print()
print("Colonel")
print()
# Strips the newline character
for line in Lines:
	count += 1
	if "C/Col" in line:
		Col += 1
		print(line + "  " + str(Col))


def percentage(part, whole):
	Percentage = 100 * float(part)/float(whole)
	return str(round(Percentage, 1)) + "%"


print("CADETS: " + str(CADET) + "/" + str(count) + " : " + percentage(CADET, count))
print("Amn: " + str(Amn) + "/" + str(count) + " : " + percentage(Amn, count))
print("A1C: " + str(A1C) + "/" + str(count) + " : " + percentage(A1C, count))
print("SrA: " + str(SrA) + "/" + str(count) + " : " + percentage(SrA, count))
print("SSgt: " + str(SSgt) + "/" + str(count) + " : " + percentage(SSgt, count))
print("TSgt: " + str(TSgt) + "/" + str(count) + " : " + percentage(TSgt, count))
print("MSgt: " + str(MSgt) + "/" + str(count) + " : " + percentage(MSgt, count))
print("SMSgt: " + str(SMSgt) + "/" + str(count) + " : " + percentage(SMSgt, count))
print("CMSgt: " + str(CMSgt) + "/" + str(count) + " : " + percentage(CMSgt, count))
print("2dLt: " + str(twodLt) + "/" + str(count) + " : " + percentage(twodLt, count))
print("1stLt: " + str(firststLt) + "/" + str(count) + " : " + percentage(firststLt, count))
print("Capt: " + str(Capt) + "/" + str(count) + " : " + percentage(Capt, count))
print("Maj: " + str(Maj) + "/" + str(count) + " : " + percentage(Maj, count))
print("LtCol: " + str(LtCol) + "/" + str(count) + " : " + percentage(LtCol, count))
print("Col: " + str(Col) + "/" + str(count) + " : " + percentage(Col, count))
