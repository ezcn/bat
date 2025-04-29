### Preparing the data  

#### 1. Raw sequence data processing  

##### 1a Ultralong ONT data processing → Herro + assembly (LAURA, DARIO)
- Sequence quality before correction (see the pdf) 
- Assembly before correction 
    - with Shasta 
    - with Fly 
- Herro correction  
- Assembly after correction 
    - with Shasta   
    - with Fly 

##### 1b PacBio data processing (FLAVIA, FRANCO)
- Assemblies:  done 

[figure assmblyhifiasm primary](img/assembly_metrics_primary_only.pdf)

[figure assmblyhifiasm haploid](img/assembly_metrics_all_h1_h2.png) 

[figure contiguity ](img/contiguity_plot.pdf)

[figure coverage](img/coverage_distribution_summary.png)

[figure contigs length distribution](img/contig_length_distribution_faceted.png) 

[figure contigs length distribution without low quality samples](img/contig_length_histogram_filtered.png)

Next steps: 
 - assign contigs to chromosomes (permissive alignment whole genome one sample vs (a) mutica, (b) sorcina, (c) commissarii) 


*- [not necessary] Replicate Tilman 
    - -- (1) use same data as Tillman (no HiC, downsampling to 10X (30Gb))
    Reassembled Commissari with only HiFi:
            - H1: 118 contigs (194 contigs in Tilman's data)
            - H2: 112 contigs (181 contigs in Tilman's data))
            - primary: 93 contigs
    - -  (4) polish assemblies https://github.com/ChongLab/Inspector?tab=readme-ov-file
    - -- (5) check for contaminats;   
    - -- (6) try verkko;   
    - -- (7) align over reference* 


#### 2.  Pangenome graph induction (FRANCO) 
- Using 1a, 1b + publicly available data and what we have so far: 

    - -- Glossophaga commissarisi: 146 GB of HIFi, HiC 
    - -- Glossophaga soricina (pure): HiFi + HiC 
    - -- Glossophaga mutica (pure): GCA_039655065.1 on NCBI

- Rough estimate of divergence/ similarity 

    - -- Self-silmilarity [see figure chr15 hap1vs hap2]()
Performed an alignment using minimap2 and and mummer (local). 
Filtering removed redundant (overlapped) or low-confidence alignments:
    - -- Total high-confidence non-overlapped aligned segments: 6
    - -- Query coverage (Soricina): 99.64% 
    - -- Reference coverage (Mutica): 92.61%
    - -- Average sequence identity: 57.47% (potential errors?)

- Preliminary graph - chromosome 15:  
    - [Pangenome graph](img/bat_pangenome.png)

#### 3. Detection of genetic variants (ERNESTINE, ANGELA)
- Genomic Variant calling in 21 bats using 1a, 1b. 
- PanGenomic Variant calling in 21 bats using 2 
- mtDNA variant calling and copy number from 1a, 1b

#### 4. Methylation profiles 
Using pacBio data (1b) . 

#### 5. Phenotypes summary stats (SILVIA, ERNESTINE, ANGELA)
**Descriptive stats for phenotypic data**

##### All bats 
- [Phenotype Distribution Check](img/checkPhenoDistribution.png)

##### Sequenced bats 
- [Sequenced Phenotype Distribution Check](img/sequencedCheckPhenoDistribution.png)

##### All bats - colonies, males, females 
- [Phenotype Analysis](img/phenotype.png)

##### Sequenced bats - colonies, males, females 
- [Sequenced Phenotype Data](img/sequenced_phenotype.png)

**Descriptive stats for metabolomic data**
