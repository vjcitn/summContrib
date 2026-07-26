# BiocContributions Package Submissions Analysis

The `bioconductor/BiocContributions` repository serves as the submission portal and automated build-test framework for new R packages proposed for inclusion in the Bioconductor project. This report classifies the recent package submissions into themed categories of genomic data science. Categories were generated dynamically by **anthropic** using model `claude-sonnet-4-6`.

Packages that include compiled C or C++ source code in their `src/` directory are marked with **[C/C++]**.

---

## 1. Mass Spectrometry & Metabolomics
This category includes tools dedicated to the specified topic.

### Representative Submissions:
* **[quantMSImageR](https://github.com/MJS-708/quantMSImageR)** (Issue #115): Provides quantitative analysis of mass spectrometry imaging data.
* **[MRManalyzeR](https://github.com/MJS-708/MRManalyzeR)** (Issue #112): Performs reproducible post-acquisition processing and QC of targeted LC-MS/MS metabolomics data from Waters TargetLynx, Skyline, or generic matrices.
* **[SpectraStash](https://github.com/RforMassSpectrometry/SpectraStash)** (Issue #111): Implements language-agnostic storage and serialization formats for Spectra Bioconductor package MS data objects including alabaster support.
* **[MsBackendMetabolomicsWorkbench](https://github.com/rformassspectrometry/MsBackendMetabolomicsWorkbench)** (Issue #77): Provides a Spectra MsBackend interface to access and retrieve metabolomics data from the Metabolomics Workbench repository.
* **[LIPIDIFy](https://github.com/fayrouzhammal/LIPIDIFy)** (Issue #56): Supports lipid identification and differential analysis in lipidomics mass spectrometry experiments.
* **[pepVet](https://github.com/LangeLab/pepVet)** (Issue #98): Provides quality control and validation tools for peptide-level proteomics data.
* **[PTMsToPathwaysData](https://github.com/UM-Applied-Algorithms-Lab/PTMsToPathwaysData)** (Issue #79): Supplies post-translational modification to pathway mapping reference data for enrichment analyses.
* **[pepitope](https://github.com/mschubert/pepitope)** `[C/C++]` (Issue #62): Enables analysis and characterisation of peptide epitopes from proteomics or immunopeptidomics data.

---

## 2. Single-Cell, Spatial & Multi-Omics Analysis
This category includes tools dedicated to the specified topic.

### Representative Submissions:
* **[MultiAssaySpatialExperiment](https://github.com/Genentech/MultiAssaySpatialExperiment)** (Issue #110): Extends MultiAssayExperiment to support multi-assay spatial transcriptomics experiment containers.
* **[SPAROscore](https://github.com/MangiolaLaboratory/SPAROscore)** (Issue #104): Computes spatial omics activity or regulation scores for spatially resolved transcriptomics data.
* **[scMAGeCK](https://github.com/weili-lab/scMAGeCK)** `[C/C++]` (Issue #89): Integrates single-cell RNA-seq with CRISPR screen (MAGeCK) data to identify gene regulatory relationships.
* **[scCertify](https://github.com/Jaya-Surya-dev/scCertify)** (Issue #78): Provides certification and quality benchmarking of single-cell RNA-seq datasets or analysis pipelines.
* **[SwitchClass](https://github.com/PYangLab/SwitchClass)** (Issue #76): Detects and characterises isoform or cell-state switching events in single-cell transcriptomics data.
* **[WOVEN](https://github.com/NathanBresette/woven)** (Issue #73): Integrates multiple single-cell or multi-omics data modalities into a unified embedding or network.
* **[scOverlay](https://github.com/bernatgel/scOverlay)** (Issue #68): Overlays and visualises single-cell data annotations or signals on reference maps or embeddings.
* **[CySA](https://github.com/baj12/CySA)** (Issue #66): Performs cytometry-based single-cell analysis including clustering and marker visualisation.
* **[cellpaintr](https://github.com/ChristofSeiler/cellpaintr)** (Issue #93): Analyses morphological cell painting image-based profiling data from high-content microscopy screens.
* **[TiDEomics](https://github.com/hte123/TiDEomics)** (Issue #40): Enables time-series or temporal decomposition analysis across multi-omics single-cell datasets.
* **[sciNOME](https://github.com/Medinfo-Lab/sciNOME)** (Issue #59): Integrates single-cell multi-omics layers to infer regulatory or functional relationships across modalities.
* **[polyICSFlow](https://github.com/SoegaardLab/polyICSFlow)** (Issue #53): Analyses flow cytometry data from poly(I:C) stimulation immune profiling experiments.
* **[IntegratedLearner](https://github.com/himelmallick/IntegratedLearner)** (Issue #48): Builds ensemble or stacked machine-learning models for integrated multi-omics outcome prediction.
* **[SimiCviz](https://github.com/ML4BM-Lab/SimiCviz)** (Issue #38): Visualises cell similarity, trajectories, or clustering results from single-cell omics experiments.
* **[MOTL](https://github.com/MOohTus/MOTL)** (Issue #61): Provides multi-omics transfer learning or integration utilities for single-cell datasets.
* **[bHIVE](https://github.com/BorchLab/bHIVE)** `[C/C++]` (Issue #41): Performs Bayesian or hierarchical integration and inference across multi-omics data modalities.
* **[CMEnt](https://github.com/CMG-UA/CMEnt)** (Issue #55): Computes cross-modal entropy or information-theoretic measures for multi-omics data integration.
* **[mdclust](https://github.com/Herbermann/mdclust)** `[C/C++]` (Issue #103): Implements multi-dimensional or multi-omics clustering algorithms for high-dimensional biological data.
* **[fastPLS](https://github.com/tkcaccia/fastPLS)** `[C/C++]` (Issue #84): Provides fast partial least squares regression and discrimination for high-dimensional omics data.
* **[faissR](https://github.com/tkcaccia/faissR)** `[C/C++]` (Issue #86): Wraps the FAISS library to enable efficient approximate nearest-neighbour search on large omics feature matrices.

---

## 3. Genomics, Epigenomics & Genome Organisation
This category includes tools dedicated to the specified topic.

### Representative Submissions:
* **[ggwas](https://github.com/bczech/ggwas)** (Issue #114): Creates ggplot2-based visualisations for genome-wide association study (GWAS) results.
* **[MESA](https://github.com/cruk-mi/mesa)** (Issue #113): Performs methylation or epigenomic set analysis to identify differentially active regulatory regions.
* **[consensusTADs](https://github.com/CSOgroup/consensusTADs)** (Issue #72): Derives consensus topologically associating domain (TAD) boundaries across multiple Hi-C datasets.
* **[epiwraps](https://github.com/ETHZ-INS/epiwraps)** (Issue #46): Provides wrapper utilities for common epigenomics workflows including signal processing over genomic regions.
* **[tTEscanR](https://github.com/avarassanchez/tTEscanR)** (Issue #75): Scans for and characterises transposable element activity or expression in genomic or transcriptomic data.
* **[inferRecom](https://github.com/catherinefayemahoney/inferRecom)** (Issue #80): Infers meiotic recombination events or hotspots from genomic sequencing data.
* **[karioCaS](https://github.com/thiagoparentefiocruz/karioCaS)** (Issue #67): Analyses karyotype changes or chromosomal instability signals from sequencing or cytogenetic data.
* **[loopcityData](https://github.com/jpflores-13/loopcityData)** (Issue #60): Supplies reference or processed chromatin loop datasets for use in 3D genome analysis workflows.
* **[GPlinksR](https://github.com/Corawang123/GPlinksR)** (Issue #69): Identifies and analyses genomic links between genetic variants and phenotypes or regulatory elements.
* **[ClinicalVariantR](https://github.com/safarafique/ClinicalVariantR)** (Issue #100): Annotates and interprets clinical significance of genomic variants using curated databases.
* **[rvarsim](https://github.com/liu-sun/rvarsim)** (Issue #52): Simulates realistic genomic variant datasets for benchmarking variant calling and annotation pipelines.
* **[QuickBLAST](https://github.com/vizkidd/QuickBLAST)** `[C/C++]` (Issue #96): Provides a fast R interface for running BLAST sequence similarity searches on nucleotide or protein sequences.
* **[geneslator](https://github.com/knowmics-lab/geneslator)** (Issue #42): Translates or maps gene identifiers and annotations across species or database reference systems.
* **[gdscloud](https://github.com/zhengxwen/gdscloud)** `[C/C++]` (Issue #58): Enables cloud-based access and analysis of Genomic Data Structure (GDS) format genomic datasets.
* **[TxParq.Hs.gencode.v49](https://github.com/vjcitn/TxParq.Hs.gencode.v49)** (Issue #28): Provides human GENCODE v49 transcript annotation data in Parquet format for efficient genomic queries.
* **[GO.ddb,](https://github.com/vjcitn/GO.ddb)** (Issue #27): Supplies a DuckDB-backed Gene Ontology annotation database for fast term and gene queries.
* **[PlantTxDbHub](https://github.com/kabilanbio/PlantTxDbHub)** (Issue #44): Provides a AnnotationHub-based repository of plant transcript annotation databases across species.

---

## 4. Data Infrastructure, Storage & Database Backends
This category includes tools dedicated to the specified topic.

### Representative Submissions:
* **[BiocDuckDB](https://github.com/Genentech/BiocDuckDB)** (Issue #109): Provides a general DuckDB backend integration layer for Bioconductor data structures and workflows.
* **[DuckDBSpatial](https://github.com/Genentech/DuckDBSpatial)** (Issue #108): Implements a DuckDB-backed storage backend for spatially resolved omics data objects.
* **[DuckDBGRanges](https://github.com/Genentech/DuckDBGRanges)** (Issue #107): Provides a DuckDB-backed representation of GRanges genomic interval objects for scalable range queries.
* **[DuckDBArray](https://github.com/Genentech/DuckDBArray)** (Issue #106): Implements a DuckDB-backed DelayedArray backend for out-of-memory storage of large omics matrices.
* **[DuckDBDataFrame](https://github.com/Genentech/DuckDBDataFrame)** (Issue #105): Provides a DuckDB-backed DataFrame class enabling scalable, lazy tabular data operations in Bioconductor.
* **[OmicsLake](https://github.com/matsui-lab/OmicsLake)** (Issue #97): Implements a data lake architecture for storing, organising, and retrieving large-scale multi-omics datasets.
* **[spatialdataR](https://github.com/HelenaLC/spatialdataR)** (Issue #34): Provides infrastructure and data containers for managing and distributing spatial omics reference datasets.
* **[PACMOSData](https://github.com/lipikakalson/PACMOSData)** (Issue #64): Supplies curated reference or processed omics datasets for use in PACMOS analysis workflows.
* **[GSE142512](https://github.com/paulYRP/GSE142512)** (Issue #82): Provides processed and annotated data from GEO series GSE142512 as a Bioconductor ExperimentData package.
* **[GSE280465](https://github.com/paulYRP/GSE280465)** (Issue #81): Provides processed and annotated data from GEO series GSE280465 as a Bioconductor ExperimentData package.

---

## 5. Differential Expression, Pathway & Network Analysis
This category includes tools dedicated to the specified topic.

### Representative Submissions:
* **[DgeaHeatmap](https://github.com/leolanci/DgeaHeatmap)** (Issue #102): Generates specialised heatmap visualisations for differential gene expression analysis results.
* **[MetaPathNet](https://github.com/zhaojie-wang/MetaPathNet.git)** (Issue #43): Constructs and analyses metabolite-pathway networks for metabolomics enrichment and topology studies.
* **[selexprepR](https://github.com/marcorotanegroni/selexprepR)** (Issue #90): Prepares and preprocesses selection or comparative expression data for downstream statistical analysis.
* **[Sbivar](https://github.com/sthawinke/sbivar)** `[C/C++]` (Issue #45): Performs bivariate statistical association or co-expression analysis across omics features.
* **[grayleafspotr](https://github.com/rotsl/grayleafspotr)** (Issue #39): Identifies and visualises grey-leaf-spot or analogous pattern signals in biological expression datasets.
* **[reglScatterplotR](https://github.com/george123ya/reglScatterplotR)** (Issue #65): Produces regulatory scatterplots to visualise gene expression relationships and regulatory associations.
* **[multipointR](https://github.com/mjemons/multipointR)** (Issue #63): Performs multi-point or multi-locus statistical testing for genetic or expression association studies.
* **[multipletR](https://github.com/Alex05a/multipletR)** (Issue #101): Handles multiplet detection, correction, or modelling in omics association or co-occurrence analyses.
* **[MOTL](https://github.com/MOohTus/MOTL)** (Issue #61): Provides tools for multi-omics transfer learning approaches to improve pathway and network inference.

---

## 6. Visualisation, Utilities & Specialised Applications
This category includes tools dedicated to the specified topic.

### Representative Submissions:
* **[grayleafspotr](https://github.com/rotsl/grayleafspotr)** (Issue #39): Detects and visualises grey leaf spot disease signals from plant phenotyping or image data.
* **[reglScatterplotR](https://github.com/george123ya/reglScatterplotR)** (Issue #65): Creates regulatory-context scatterplots for visualising relationships between regulatory and expression variables.
* **[SimiCviz](https://github.com/ML4BM-Lab/SimiCviz)** (Issue #38): Visualises similarity metrics and clustering results for comparative cell or omics profiling.
* **[DgeaHeatmap](https://github.com/leolanci/DgeaHeatmap)** (Issue #102): Generates publication-ready heatmaps tailored for differential gene expression result visualisation.