# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "dandi-team"
copyright = "2026, DANDI team"
author = "Elizabeth DuPre, Lune Bellec, Bertrand Thirion"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".nox"]

import os
import sys

sys.path.insert(0, os.path.abspath("."))

# env vars
language_env = os.environ.get("SPHINX_LANG", "en")

# Language of the current build
# language can later be overridden (eg with the -D flag)
# but we need it set here so it can make it into the html_context
language = language_env
languages = ["en", "fr"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = "https://dandi-team.github.io"
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_js_files = ["language-select.js"]

html_sidebars = {
    "path/to/page": [],
}
html_theme_options = {
    "navbar_persistent": ["language-selector", "search-button"],
    "secondary_sidebar_items": {
        "path/to/page": [],
    },
}
html_context = {
    "language": language,
    "languages": languages,
    "baseurl": html_baseurl,
}
