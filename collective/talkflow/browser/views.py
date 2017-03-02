from collective.talkflow.interfaces import DISCUSSION_TYPE, ANSWER_TYPE
from plone import api

import utils


_marker = object()


class BaseView(object):
   
    index = None  # to be defined by Five magic template generated class
    _can_add = _marker
 
    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal = api.portal.get()
        self.catalog = api.portal.get_tool(name='portal_catalog')

    def _search(self, query, restricted=True):
        name = 'searchResults' if restricted else '_unrestrictedSearchResults'
        search = getattr(self.catalog, name)
        return search(query)

    def update(self, *args, **kwargs):
        raise NotImplementedError('base method')

    def can_add(self):
        if self._can_add is _marker:
            # get local permissions for current auth user
            permissions = api.user.get_permissions(obj=self.context)
            self._can_add = permissions.get('Add portal content', False)
        return self._can_add

    def __call__(self, *args, **kwargs):
        self.update(*args, **kwargs)
        return self.index(*args, **kwargs)


class FlowView(BaseView):
    """Basic flow view"""

    def __init__(self, context, request):
        super(FlowView, self).__init__(context, request)

    def discussions(self):
        """get all brains for contained discussions"""
        query = utils.local_query(
            self.context,
            {'sort_on': 'modified', 'sort_order': 'descending'},
            types=(DISCUSSION_TYPE,)
            )
        return self._search(query)

    def update(self, *args, **kwargs):
        pass  # TODO


class DiscussionView(BaseView):
    """View discussion or question/answers"""

    def __init__(self, context, request):
        super(DiscussionView, self).__init__(context, request)

    def answers(self):
        """get all brains for contained question answers"""
        if not getattr(self.context, 'question', False):
            return []
        query = utils.local_query(
            self.context,
            {'sort_on': 'modified', 'sort_order': 'descending'},
            types=(ANSWER_TYPE,)
            )
        return self._search(query)

    def update(self, *args, **kwargs):
        pass  # TODO

