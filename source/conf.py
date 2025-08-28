# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Welcome to Spatial Data for GIS'
copyright = 'University of Twente, 2025'
author = 'André da Silva Mano (editor), Cees van Vesten (scientific coordination), Nanette Kingma, Elinor Meredith, Irene Manzella and Catherine Nabukulu'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
import sphinx_readable_theme

sys.path.append(os.path.abspath("./_ext"))

# Name of the master document.
master_doc = 'index'

extensions = ['sphinx_design', #requires pip install sphinx-design (to allow for dropdown admonitions)
              'docxbuilder']   #requires pip install docxbuilder (to allow making docx files)

templates_path = ['_templates']
exclude_patterns = ['_static/assets/external_links.rst', '_static/assets/data-links.rst']

numfig = True

link_file = ['_static/assets/external_links.rst',
            '_static/assets/data-links.rst'
            ]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_permalinks_icon = '<span>#</span>'
html_theme = 'readable'
html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_logo = "_static/itc_logo.png"
html_static_path = ["_static"]
html_css_files = [
    'itc_logo.css',
]

html_theme_options = {
    "logo_light": "_static/itc_logo.png",  # shown in light mode
    "logo_dark": "_static/itc_logo.png",   # shown in dark mode (can be different)
}

# sphinx default themes
# html_theme = 'alabaster'
# html_theme = 'pyramid'
# html_theme = 'sphinx-book-theme'

# Allows storing external links in separated rst
rst_epilog=""

# Target link-files
link_files = ['_static/assets/external_links.rst',
            '_static/assets/data-links.rst'
            ]

# Read links in the from the target files
for file in link_files:
    with open(file) as f:
        rst_epilog += f.read()


html_static_path = ['_static']

# Configure paper size, font size, preamble options, etc (for LaTeX output).
latex_elements = {
    'figure_align': 'H',
    'preamble': '''
        \\usepackage{float}
        ''',
}
