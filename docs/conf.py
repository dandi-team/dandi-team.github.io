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
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

import os.path
from sphinx.locale import get_translation

catalog = "messages"
_ = get_translation(catalog)


def setup(app):
    locale_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "locale")

    app.add_message_catalog(catalog, locale_dir)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"

html_sidebars = {
    "path/to/page": [],
}
html_theme_options = {
    "secondary_sidebar_items": {
        "path/to/page": [],
    },
}
