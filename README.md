## summContrib -- analyze and report on packages in review at Bioconductor

### Basic workflow

1. Generate JSON document with basic information about submissions.  These
are all open issues at `bioconductor/BiocContributions`.
```
  curl -H "Authorization: Bearer $GITHUB_PAT" \
       -H "Accept: application/vnd.github+json" \
       "https://api.github.com/repos/bioconductor/BiocContributions/issues?state=all&per_page=100"
```

2. Save the result of the API call above to a file, say `conts.json`.

3. Run the `generate_bioc_summary.py` program, preferably with `GITHUB_TOKEN` set to
a valid value.  A markdown document will be produced with categorization and
additional information about each submission.

## Compiled code detection

`code/generate_bioc_summary.py` automatically checks each submitted package's GitHub repository for a `src/` directory containing C or C++ source files (`.c`, `.cc`, `.cpp`, `.cxx`, `.h`, `.hpp`). Packages where such files are found are tagged with `` `[C/C++]` `` inline in the report.

The check uses the GitHub Contents API and runs once per unique repository URL before the report is written. Results appear directly in the package listing, for example:

```
* **[FaissR](https://github.com/tkcaccia/FaissR)** `[C/C++]` (Issue #85): R bindings to the FAISS library...
```

### GITHUB_TOKEN

The GitHub API allows **60 unauthenticated requests per hour** per IP address. A single report run across ~40 packages will stay within that limit, so no token is needed for occasional use.

For repeated runs during development (e.g., iterating on the script, testing with different issue snapshots), the limit can be exhausted quickly. To raise it to **5,000 requests per hour**, set a GitHub personal access token in your environment before running:

```bash
export GITHUB_TOKEN=ghp_...
python3 code/generate_bioc_summary.py
```

The script reads the token from the `GITHUB_TOKEN` environment variable automatically. A fine-grained token with read-only access to public repositories is sufficient.


## Origins

Gemini 3.5 was prompted with: Please summarize the issues at https://github.com/bioconductor/BiocContributions into five or six categories of genomic data science

Then it was asked to produce a markdown document and then to use hyperlinks for the names of contributed packages in the report.

Output in markdown format will be saved in date-stamped folders.  There will be one file of json GitHub API output, and one file of markdown.

The code base was then iteratively altered using Claude Sonnet.
