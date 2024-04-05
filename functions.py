from flask import Flask, render_template, request, render_template_string
from flask_flatpages import FlatPages
from flask_flatpages.utils import pygmented_markdown

# custom renderer function for FlatPages so that it renders markdown with Jinja
def my_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)
    # Or, if you wish to render using the markdown extensions
    # listed in FLATPAGES_MARKDOWN_EXTENSIONS:
    #return pygmented_markdown(prerendered_body, flatpages=pages)