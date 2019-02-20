from matplotlib import pyplot as plt
from setCalculations import setList
from matplotlib_venn import venn3

venn3(subsets = setList, set_labels = ('ClinVar', 'LOVD', 'Allele Frequency Databases'))
plt.title("Number of Variants per Contributor")
plt.savefig('contributors.png', dpi=500)
plt.show()