from flask import render_template as flask_render_template


def render_template(*args, **kwargs):
    return flask_render_template(*args, data=kwargs)
