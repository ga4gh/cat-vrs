# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import subprocess

# import sys
# sys.path.insert(0, os.path.abspath('.'))


def _get_git_tag():
    res = subprocess.run(
        "git describe --tags --exact-match".split(), capture_output=True
    )
    if res.stderr.decode().startswith("fatal"):
        # if no exact tag, then get branch
        res = subprocess.run(
            "git rev-parse --abbrev-ref HEAD".split(), capture_output=True
        )
    tag = res.stdout.decode().strip()
    return tag


def _parse_release_as_version(rls):
    m = re.match(r"^(\d+\.\d+)", rls)
    if m:
        return m.group(1)
    return rls


# -- Project information -----------------------------------------------------
print("RTD env:", {
    "RTD_VERSION": os.environ.get("READTHEDOCS_VERSION"),
    "RTD_VERSION_TYPE": os.environ.get("READTHEDOCS_VERSION_TYPE"),
    "RTD_GIT_IDENTIFIER": os.environ.get("READTHEDOCS_GIT_IDENTIFIER"),
    "RTD_GIT_COMMIT_HASH": os.environ.get("READTHEDOCS_GIT_COMMIT_HASH")
})

project = "GA4GH Categorical Variation Representation Specification"
copyright = "2023-%Y, GA4GH CatVRS Contributors."
author = "Committers"
master_doc = "index"
# N.B. RTD ignores these values. :-/
release = _get_git_tag()
version = _parse_release_as_version(release)

# Generate GitHub version depending on the Readthedocs Version
# - stable: will use the tag name
# - latest: will use the corresponding branch name
# - other branch versions: will use the branch name
# - PR previews: will use the commit hash
if os.environ.get("READTHEDOCS"):
    identifier = os.environ.get("READTHEDOCS_GIT_IDENTIFIER")
    if identifier and identifier.isdigit():
        github_version = os.environ.get("READTHEDOCS_GIT_COMMIT_HASH", "main")
    else:
        github_version = identifier or os.environ.get("READTHEDOCS_GIT_COMMIT_HASH", "main")
else:
    github_version = "main"

# -- Schema doc paths --------------------------------------------------------

rst_epilog_fn = os.path.join(os.path.dirname(__file__), "rst_epilog")
rst_epilog = open(rst_epilog_fn).read().format(release=release)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.todo", "sphinx_toolbox.collapse"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["def/**"]

# TODO directive output
todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = "images/GA-logo.png"

html_theme_options = {"collapse_navigation": False}
html_context = {
    "conf_py_path": "/docs/source/",
    "display_github": True,
    "github_user": "ga4gh",
    "github_repo": "cat-vrs",
    "github_version": github_version,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["theme_overrides.css"]

# Sidebars

html_sidebars = {
    "**": ["globaltoc.html", "relations.html", "sourcelink.html", "searchbox.html"]
}
