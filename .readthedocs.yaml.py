# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details
# Required
import conf as conf
import docs as docs

version: 2

# Set the OS, Python version and other tools you might need
build:
  tools:
    python: "3.12"
    # You can also specify other tool versions:
    # nodejs: "20"
    # rust: "1.70"
    # golang: "1.20"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py
  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
  # builder: "dirhtml"
  # Fail on all warnings to avoid broken references
  # fail_on_warning: true

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#   - pdf
#   - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
# python:
#   install:
#     - requirements: docs/requirements.txt