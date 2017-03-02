
def local_query(context, query, types=None, depth=2):
    """
    Given a catalog search query dict and a context, restrict
    search to items contained in the context path or subfolders,
    and particularly only items of one or more content portal_type.

    Returns modified query dict for use with catalog search.
    """
    query = dict(query.items())  # cheap copy
    path = '/'.join(context.getPhysicalPath())
    query['path'] = {
        'query': path,
        'depth': depth,
        }
    if types is not None:
        query['portal_type'] = {
            'query': types,
            'operator': 'or',
            }
    return query
