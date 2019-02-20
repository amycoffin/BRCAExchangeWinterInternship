clinVar = 15553 #quantity contributed by ClinVar
lovd = 7704 #quantity contributed by LOVD
alleleFreq = 7246 #quantity contributed by Allele Frequency contributors (ExAC, 1000 Genomes, etc.)
clinVarLOVD = 6486 #quantity in clinVar and LOVD
clinVarAlleleFreq = 3323 #quantity in ClinVar and all Allele Frequency contributors (ExAC, 1000 Genomes, etc.)
lovdAlleleFreq = 2087 #quantity in LOVD and all Allele Frequency contributors (ExAC, 1000 Genomes, etc.)
allThree = 1986 #quantity in all 3 data contributor sets

total0 = clinVar + lovd + alleleFreq +clinVarLOVD + clinVarAlleleFreq + lovdAlleleFreq + allThree
#WRITE SOMETHING TO CHECK TOTAL and PRINT IT below!
"""Here are numbers for you.  
There are 15553 variants from ClinVar, 
7730 of which are distinct to ClinVar.  
There are 7704 variants in LOVD, 
1117 of which are distinct to LOVD.   
There are 7246 variants from the allele frequency repositories (1000 Genomes, ExAC, ESP), 
3822 of which are distinct to allele frequency sets.

For the two-way intersections, there are 
3323 variants in ClinVar and allele frequency sets, 
2087 in LOVD and allele frequency sets, 
and 6486 in ClinVar and LOVD.
For the three-way intersection, there are 1986 variants in all three sets."""

g = allThree
f = lovdAlleleFreq - allThree
e = clinVarAlleleFreq - allThree
c = clinVarLOVD - allThree
a = clinVar - c - e - g
b = lovd - c - f - g
d = alleleFreq - e - f - g
setList = a, b, c, d, e, f, g
#print sum(setList, 0)

total = 0
for item in setList:
    total = total + item
#print total


#print(setList)
