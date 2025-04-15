### Preparing the data  

#### 1. Raw sequence data processing  

##### 1a Ultralong ONT data processing → Herro + assembly (LAURA, DARIO, FLAVIA)
- Sequence quality before correction (see the pdf) 
- Assembly before correction 
    - with Shasta -DONE 
    - with Fly 
- Herro correction DONE 
- Assembly after correction 
    - with Shasta   DONE 
    - with Fly 

- [Shasta - beforeAfter](img/read_length_histogram.png)


##### 1b PacBio data processing → assembly   

    -Test twice (Franco and Flavia) using Hifiasm GS0138, GSO435 --> too many contings
    - See the [figure assmblyhifiasm](img/assembly_metrics_pacbio.png)
    - -- (1)  check for contaminats;   
    - -- (2)  try verkko;   
    - -- (3) align over reference 
    - -- (4) use reads > 15-20k  

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
Genomic Variant calling in 21 bats using 1a, 1b. 
PanGenomic Variant calling in 21 bats using 2 
mtDNA variant calling and copy number from 1a, 1b

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