# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'NY Assembly Transcript API'
copyright = '2024, Nick Gutin'
author = 'Nick Gutin'
release = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = None
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}

# Add custom CSS
def setup(app):
    app.add_css_file('custom.css')
