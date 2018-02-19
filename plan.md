# Thesis Plan - Felix Simkovic

### 1. Introduction

#### 1.1 General introduction

#### 1.2 Molecular Replacement
This section will provide an overview of MR.

#### 1.3 Ab initio structure prediction
This section will provide an overview of fragment-based ab initio structure prediction of protein sequences.

#### 1.4 Contact predictions
This section will discuss primarily covariance-based contact prediction. It will also ellaborate on latest developments
of hybrid methods and in this context briefly describe ML-based algorithms.

### 2. General methods
This section will outline general methodologies used throughout multiple chapters in the thesis. It will outline any
software developments done as part of the PhD to create, enhance or fix software.

#### 2.1 Dataset creation
This section will describe proceedures of selecting target datasets.

#### 2.2 Evaluation of data
This section will outline and explain all mathematical and statistical definitions used throughout all chapters to
assess various information.

##### 2.2.1 Co-evolution data

##### 2.2.2 Structure prediction data

##### 2.2.3 Crystallographic data

### 3. Residue contacts predicted by evolutionary covariance extend the application of ab initio Molecular Replacement to larger and more challenging protein folds
This chapter will contain all work described in Simkovic et al (2016)

### 4. Approaches to ab initio molecular replacement of alpha-helical transmembrane proteins
This chapter will contain all contact-related work described in Thomas et al (2017)

### 5. Evaluation of ROSETTA distance-restraint energy functions on contact-guided ab initio structure prediction
This chapter will contain all work related to the evaluation of two ROSETTA energy functions given three separate
metapredictor contact predictions.

### 6. Decoy subselection using contact information to enhance MR search model creation
This chapter will discuss the use of contact information to score ab initio decoys, how this information could be used to enhance ensemble search model quality and ultimately MR success.

### 7. Alternative ab initio structure prediction algorithms for AMPLE
This chapter will briefly discuss the use of two alternate ab initio structure prediction algorithms and the (dis-)advantages of using the output decoys in AMPLE

### 8. Protein fragments as search models in Molecular Replacement
This chapter will discuss the use of ab initio structure prediction fragments directly as search models.

### 9. Software developments

#### 9.1 ConKit
This section will describe the ConKit package, and any algorithms implemented to assess contact and sequence information. 
It will expand on Simkovic et al (2017) and describe the package in more detail.

#### 9.2 Integration of ConKit in AMPLE
This section will briefly outline the integration of ConKit in AMPLE

#### 9.3 Truncation of single models in AMPLE
This section will outline the algorithm implemented into AMPLE to truncate single decoys

### 9. Discussion
