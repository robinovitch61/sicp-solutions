# sicp-solutions

This is all the SICP solutions from http://community.schemewiki.org/?SICP-Solutions in a single PDF.

To regenerate:

1. Install [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html)

2. Setup Python by installing:

```shell
pip install requests beautifulsoup4 pdfkit pypdf
```

3. Temporarily change file limit for current shell (may be different on different OS's)

```shell
ulimit -n 10240
```

4. Run `python generate.py`
