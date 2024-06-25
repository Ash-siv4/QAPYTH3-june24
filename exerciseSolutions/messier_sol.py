# 2.	Examine the file messier.txt in the labs directory, which contains details of celestial "Messier" objects.
# It consists of several columns for each object, identified by the 'M' number. The columns are as follows:
#
# MessierNumber    CommonName	ObjectType	  Constellation
#
# Note that many have no common name. Read the file using a for loop:
#
# 	for line in open('messier.txt', encoding='latin_1'):
#        if not line: break
# 	    # The text is in the variable named 'line'
#
# Ignore lines that do not start with 'M'.
# Print the fields from each line delimited with '|' characters. Where there is no common name, use 'no name'.
# Ignore any lines not beginning with a Messier number. For example:
# |M1|The Crab Nebula|Supernova remnant|Taurus|
# |M2|no name|Globular cluster|Aquarius|
# |M3|no name|Globular cluster|Canes Venatici|
#
# Hint: the header on the file should assist in getting the field positions.

for line in open('../scripts&Files/messier.txt'):
    if not line: break
    # ignore lines that don't start with M - find the lines that start with m, if so, ignore, otherwise dont ignore
    if line.startswith("M"):
        print(line)
        #slice each field
        MessierNumber = line[:6].rstrip()
        print(MessierNumber)
        CommonName = line[6:40].rstrip()
        ObjectType = line[40:64].rstrip()
        Constellation = line[64:].rstrip()
        # # get each field from the string - split()
        # fields = line.split()
        # print(fields)
        # # extract the fields based on their postion
        # MessierNumber = fields[0]
        # CommonName = " ".join(fields[1:2]) if len(fields) > 3 else "no name"
        # ObjectType = fields[-2]
        # Constellation = fields[-1]

        # handle cases with no common name
        if CommonName == "":
            CommonName = "no name"
        # print fields delimited with "|"
        print(f"|{MessierNumber}|{CommonName}|{ObjectType}|{Constellation}|")
        print("|{}|{}|{}|{}|".format(MessierNumber, CommonName, ObjectType, Constellation))

