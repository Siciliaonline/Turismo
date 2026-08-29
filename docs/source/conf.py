# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sizilien Tourismus Führer'
copyright = '2026, Dein Name'
author = 'Dein Name'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'it'
locale_dirs = ['locale/']
gettext_compact = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_title = "Guida turistica della Sicilia"
html_static_path = ['_static']
html_logo = "_static/images/Flag_of_Sicily.png"

html_theme_options = {
    "navigation_depth": 3,
    "collapse_navigation": False,
    "sticky_navigation": True,
    "includehidden": True,
}

html_css_files = [
    "custom.css",
]

html_sidebars = {
    '**': ['language_selector.html', 'localtoc.html', 'relations.html',
           'sourcelink.html', 'searchbox.html'],
}
