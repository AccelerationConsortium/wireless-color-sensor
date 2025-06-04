# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'wireless color sensor documentation'
copyright = '2024, Neil-YL'
author = 'Neil-YL'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Enable markdown
extensions = ['myst_parser',]

# Configure MyST-Parser
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# The suffix of source filenames.
source_suffix = [".rst", ".md"]

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'

html_theme_options = {
    "repository_url": "https://github.com/AccelerationConsortium/wireless-color-sensor",
    "repository_branch": "main",
    "path_to_docs": ".",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_source_button": True,
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_title = "Getting started guide for wireless color sensor"
html_logo = "_static/Logo/Acceleration-Consortium-vectortunnel-colour.png"

