from flask import abort, current_app


def to_int(n, default=None):
    try:
        return int(n)
    except ValueError:
        return default


def pagination(model, url, start, limit):
    # https://blog.fossasia.org/paginated-apis-in-flask/
    # check if page exists
    results = model.query.all()
    start = to_int(start, 1)
    limit = to_int(limit, current_app.config['PAGE_LIMIT'])
    count = len(results)
    if (count < start):
        abort(404)

    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj
