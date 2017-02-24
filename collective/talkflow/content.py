from AccessControl.User import nobody
from plone import api
from plone.dexterity.content import Container
from zope.interface import implements

import interfaces


class DiscussionFlow(Container):
    """Discussion flow content."""

    implements(interfaces.IDiscussionFlow)

    def __init__(self, *args, **kwargs):
        super(DiscussionFlow, self).__init__(*args, **kwargs)
        self._adjust_review()

    def _adjust_review(self, role='Reviewer'):
        # Get owner
        owner = api.user.get_current().getId()
        # the owner of the board gets the Reviewer role:
        if owner != nobody.getId():
            rolemap = dict(self.get_local_roles())
            roles = set(rolemap.get(owner, [])).union(['Reviewer'])
            self.manage_setLocalRoles(owner, list(roles))


class DiscussionPost(Container):
    """Discussion post content, may be discussion or question."""

    implements(interfaces.IDiscussionPost)


class DiscussionAnswer(Container):
    """
    Answer to question, may be folderish enough to contain added
    images or files.
    """

    implements(interfaces.IAnswer)

