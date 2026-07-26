import json
import re
import urllib.request
import urllib.error
import os

filepath = "livecontent.md"

with open(filepath, "r") as f:
    text = f.read()

json_start = text.find("[")
if json_start == -1:
    print("Could not find JSON array")
    exit(1)

json_text = text[json_start:]
issues = json.loads(json_text)

# Build a mapping of package_name -> repo_url
package_repos = {}
for issue in issues:
    title = issue.get("title", "").strip()
    # Clean title in case of "SpectraStash - serialize/restore MS..."
    clean_title = title.split(" ")[0].split(":")[0].strip()
    
    body = issue.get("body", "") or ""
    # Extract url from body
    # We look for lines containing github.com
    urls = re.findall(r'https://github.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', body)
    if urls:
        # Use the first github URL found
        package_repos[title.lower()] = urls[0]
        package_repos[clean_title.lower()] = urls[0]

# Add manual fallbacks if any are missing or need correction
# Let's make sure casing is handled properly

def has_compiled_code(repo_url, token=None):
    """Return True if the GitHub repo has a src/ folder containing C or C++ files.

    Checks the GitHub Contents API for the src/ directory and looks for files
    with extensions .c, .cc, .cpp, .cxx, or .h.  Returns False if src/ is
    absent or the API call fails.  Pass a GitHub personal-access token via the
    token argument (or the GITHUB_TOKEN env var) to avoid rate-limiting.
    """
    # Normalise URL: strip trailing slash and .git suffix
    repo_url = repo_url.rstrip("/")
    if repo_url.endswith(".git"):
        repo_url = repo_url[:-4]

    # Extract owner/repo from https://github.com/owner/repo
    m = re.search(r'github\.com/([^/]+/[^/]+)$', repo_url)
    if not m:
        return False

    api_url = f"https://api.github.com/repos/{m.group(1)}/contents/src"
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "bioc-submission-scanner"}

    resolved_token = token or os.environ.get("GITHUB_TOKEN")
    if resolved_token:
        headers["Authorization"] = f"Bearer {resolved_token}"

    req = urllib.request.Request(api_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            contents = json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False   # no src/ directory
        return False
    except Exception:
        return False

    compiled_extensions = {".c", ".cc", ".cpp", ".cxx", ".h", ".hpp"}
    for entry in contents:
        _, ext = os.path.splitext(entry.get("name", ""))
        if ext.lower() in compiled_extensions:
            return True
    return False


def scan_compiled_code(package_repos, token=None):
    """Return a dict mapping package name -> bool indicating compiled code presence.

    Iterates over every unique repo URL in package_repos and calls
    has_compiled_code for each one.
    """
    # Deduplicate: multiple keys (title variants) may share the same URL
    seen_urls = {}
    for name, url in package_repos.items():
        if url not in seen_urls:
            seen_urls[url] = has_compiled_code(url, token=token)

    return {name: seen_urls[url] for name, url in package_repos.items()}


def get_link(name, issue_num):
    # Try exact match or clean title match
    url = package_repos.get(name.lower())
    if url:
        return f"[{name}]({url})"
    return f"{name}"

categories = {
    "1. Single-Cell & Spatial Omics": [
        ("MultiAssaySpatialExperiment", 110, "Integrates multiple spatial assays and imaging data into a unified, coordinate-aware experimental container."),
        ("DuckDBSpatial", 108, "High-performance querying and extraction of spatial transcriptomics features stored in database backends."),
        ("multipletR", 101, "Doublet/multiplet detection in patient-derived xenograft (PDX) single-cell RNA-seq."),
        ("scCertify", 78, "An explainable confidence scoring framework for annotating cell types in single-cell RNA-seq data."),
        ("scOverlay", 68, "Overlay and registration utilities for single-cell imaging and transcriptomics data."),
        ("scCompoundDE", 49, "Differential expression analysis specifically designed for drug/compound screening at single-cell resolution."),
        ("SimiCviz", 38, "Visualization and regulatory analysis of gene co-expression and transcription factors in single cells."),
        ("spatialdataR", 34, "Representation and manipulation of large spatial biology datasets."),
        ("scMAGeCK", 89, "High-throughput single-cell CRISPR screen analysis.")
    ],
    "2. Proteomics, Metabolomics, & Mass Spectrometry": [
        ("quantMSImageR", 115, "Preprocessing, segmentation, and quantification of Mass Spectrometry Imaging (MSI) data."),
        ("MRManalyzeR", 112, "Post-acquisition quality control and statistical analysis of targeted LC-MS/MS metabolomics."),
        ("SpectraStash", 111, "High-efficiency serialization and restoration of MS spectra objects using a language-agnostic storage format."),
        ("MsStash", 70, "Underlying language-agnostic database serialization layer for raw and processed mass spectrometry spectra."),
        ("MsBackendMetabolomicsWorkbench", 77, "Connects R/Bioconductor sessions directly to the Metabolomics Workbench repository."),
        ("LIPIDIFy", 56, "Structural lipid identification and annotation from tandem mass spectrometry."),
        ("PTMsToPathwaysData", 79, "Curated database mapping post-translational modifications (PTMs) directly to biological pathways."),
        ("MsBackendMassIVE", 37, "Client backend for the MassIVE public mass spectrometry database repository.")
    ],
    "3. Epigenomics, 3D Genomics, & Chromatin Structure": [
        ("MESA", 113, "Methylation Enrichment Sequencing Analysis (window-based differential methylation detection)."),
        ("consensusTADs", 72, "Consensus Topologically Associating Domain (TAD) calling across multiple Hi-C replicates."),
        ("loopcityData", 60, "Data structures and reference materials for 3D chromatin looping assays."),
        ("epiwraps", 46, "Wrappers and visualization functions for ChIP-seq, ATAC-seq, and related epigenomics tracks."),
        ("selexprepR", 90, "Data preprocessing and quality control for Systematic Evolution of Ligands by Exponential Enrichment (SELEX) experiments.")
    ],
    "4. Multi-Omics Integration & Machine Learning": [
        ("fastPLS", 87, "Fast and memory-efficient Partial Least Squares algorithms for dimension reduction and multi-omics regression."),
        ("MultiOmicsBridge", 50, "Bridge infrastructure enabling unified analysis across disparate omics datasets."),
        ("IntegratedLearner", 48, "Machine learning pipeline optimizing predictors from high-dimensional multi-platform omics datasets."),
        ("TiDEomics", 40, "Analytical framework for time-course multi-omics biological data."),
        ("SPAROscore", 104, "Unified gene set scoring that adaptively manages sparsity across spatial and bulk transcriptomics."),
        ("WOVEN", 73, "Multi-omics data consolidation and network-based integration.")
    ],
    "5. Big Data Infrastructure, Databases, & Computational Utilities": [
        ("BiocDuckDB", 109, "Primary Bioconductor bindings for DuckDB, enabling high-performance SQL query engines on genomic files."),
        ("DuckDBDataFrame", 105, "SQL/Parquet-backed tabular representations for DataFrame metadata."),
        ("DuckDBGRanges", 107, "Out-of-memory genomic interval queries using the `GenomicRanges` API backed by DuckDB."),
        ("DuckDBArray", 106, "Large array representations (DelayedArray) utilizing DuckDB backends."),
        ("gdscloud", 58, "Cloud storage integrations for the Genomic Data Structure (GDS) file format."),
        ("pgen2gds", 35, "Converts large PLINK 2 binary genotype files (`.pgen`) into Genomic Data Structure (`.gds`) files."),
        ("FaissR", 85, "R bindings to the FAISS library for fast K-nearest neighbors search in high-dimensional genomic spaces."),
        ("QuickBLAST", 96, "Utilities to accelerate BLAST alignment queries.")
    ],
    "6. Functional Annotation, Genetics, & Disease/Organism Repositories": [
        ("ggwas", 114, "Customizable `ggplot2`-based visualization of Genome-Wide Association Studies (GWAS) and locus plots."),
        ("ClinicalVariantR", 100, "Clinical genomics annotation and variant reporting pipelines."),
        ("inferRecom", 80, "Pedigree-based algorithms to detect homologous recombination and map recombination intervals."),
        ("PlantTxDbHub", 44, "Standardized TxDb annotations specifically curated for plant species."),
        ("geneslator", 42, "Clean translation utilities for gene IDs across different databases and nomenclature standards."),
        ("KEGGemUP", 33, "Enrichment and mapping utilities for the Kyoto Encyclopedia of Genes and Genomes (KEGG) database."),
        ("GO.ddb", 27, "Semantic SQL database representing the Gene Ontology (GO) hierarchical structure."),
        ("ontoProc2", 25, "Continuation package for ontology processing and vocabulary mapping in R."),
        ("karioCaS", 67, "Kraken Confidence Scores for reliable domain-specific microbiota inference in metagenomics.")
    ]
}

print("Scanning repos for compiled C/C++ code in src/ — this may take a moment...")
compiled_flags = scan_compiled_code(package_repos)
print("Scan complete.")

markdown_content = """# BiocContributions Package Submissions Analysis

The `bioconductor/BiocContributions` repository serves as the submission portal and automated build-test framework for new R packages proposed for inclusion in the Bioconductor project. This report classifies the recent package submissions into six core categories of genomic data science.

Packages that include compiled C or C++ source code in their `src/` directory are marked with **[C/C++]**.

---
"""

for cat_name, items in categories.items():
    markdown_content += f"\n## {cat_name}\n"
    markdown_content += "This category includes tools dedicated to the specified topic.\n\n### Representative Submissions:\n"
    for name, issue_num, desc in items:
        link_str = get_link(name, issue_num)
        compiled_tag = " `[C/C++]`" if compiled_flags.get(name.lower()) else ""
        markdown_content += f"* **{link_str}**{compiled_tag} (Issue #{issue_num}): {desc}\n"
    markdown_content += "\n---\n"

# Remove the trailing line/dashes
markdown_content = markdown_content.rstrip("-\n ")

# Write out the new summary file
out_path = "bioc_contributions_summary.md"
with open(out_path, "w") as f:
    f.write(markdown_content)

print("Generated bioc_contributions_summary.md successfully!")
