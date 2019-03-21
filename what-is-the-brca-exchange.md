CA Exchange is a curated data platform that provides information on variants of two specific genes: *BRCA1* and *BRCA2*. Rather than contributing new information about a variant, BRCA Exchange collects and organizes existing information from a variety of databases, such as ClinVar and LOVD. Importantly, BRCA Exchange aggregates variant data according to the Hg38 reference genome and the HGVS nomenclature system even when other sites use different variant aliases. For more information regarding the aggregation and organization of variant information, see *Merging BRCA Variants*.

BRCA Exchange organizes the information from these sources to answer three basic questions about a variant:      
  
* What is the most definitive clinical interpretation available for this variant?    

* When was this interpretation made?    

* What publicly available data informed this interpretation?    

There are two ways to view variant data on this site. The default, or *summary*, view of BRCA Exchange displays variant aliases, ENIGMA variant interpretations, and a brief interpretation history. The ENIGMA Consortium assesses variant pathogenicity using an expert-developed set of *BRCA1* and *BRCA2* classification criteria. The *All Public* view contains all publicly available data on a variant. Thus, this view of the data provides a more complete, but also more complicated, variant characterization. By offering two different portals to view the aggregation of multiple large-scale data sources, BRCA Exchange is a resource that curates contextualized BRCA variant data.      

##### Merging BRCA Variants     

The purpose of the BRCA Exchange is to aggregate and organize all publicly available information related to *BRCA1* and *BRCA2* genetic variants for variant researchers, clinicians, and genetic counselors. This is a challenging bioinformatics problem because there is not a single standard variant naming convention, so the same genetic mutation is frequently referred to by many different aliases. There are two factors that determine the name of a variant: 1) the chosen reference genome, and 2) the chosen nomenclature system. BRCA Exchange helps resolve ambiguities and redundancies in BRCA variant data by merging variant aliases and determining variant names according to a single convention, the Hg38-HGVS convention. There are three key bioinformatic operations involved in *variant merging*.      

1. **Data Aggregation:** Variant data is aggregated from multiple sites and mapped according to the Hg38 Reference Genome.     

2. **Variant merging:** Variants that are identical in content and map to the same Hg38 coordinates are determined to be functionally the same. The data pertaining to variants that are functionally the same is merged.     

3. **Variant naming:** Merged variants are assigned names according to the Hg38 Reference Genome and the HGVS nomenclature system.      

Variant merging reconciles multiple aliases with reference to the Hg38 Genome. For example, ClinVar lists the 185delAG variant as two separate variants with separate database entries. While both entries refer to variants that are functionally the same, the entries appear to reference different variants because the entries adhere to different naming conventions. The BRCA Exchange data aggregation and organization pipeline recognizes this redundancy and merges the data from both ClinVar entries according to the Hg38-HGVS naming convention. This variant merging also occurs with variant data collected from different sites. Therefore, BRCA Exchange consolidates variant information and removes redundancy without losing variant data in order to streamline variant research. 

For more information on variant nomenclatures, see *Variant Nomenclatures*.   

[Variant Merging Documentation Meeting Notes](https://docs.google.com/document/d/141sEJLjxXc6wi0DAPlggDZhoMEYWXdTnhYq39elGoyY/edit).

