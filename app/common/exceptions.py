from flask import jsonify


def page_not_found(e):
    # Returns a JSON version of the 404 Page not found.
    return jsonify(error=404, text=str(e)), 404
