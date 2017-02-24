from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.supermodel import model
from zope.interface import Interface
from zope import schema

from collective.talkflow import _
from plone.app.dexterity import _ as _d_


class IBaseDiscussionContent(model.Schema):
    """Base discussion content (rich text)"""

    text = RichText(
        title=_(u'label_text', default=u'Compose text'),
        )

    # omit description field from add/edit forms
    directives.omitted('description')
    description = schema.Text()


class IDiscussionPost(IBaseDiscussionContent):
    """Discussion post, may be discussion or question"""

    question = schema.Bool(
        title=_(u'label_question', default=u'Is question'),
        description=_(
            u'help_question',
            default=u'Should this discussion be treated as a question '
                    u'with answers permitted within?'
            ),
        default=False,
        )

    subjects = schema.Tuple(
        title=_d_(u'label_tags', default=u'Tags'),
        description=_d_(
            u'help_tags',
            default=u'Tags are commonly used for ad-hoc organization of ' +
                    u'content.'
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'subjects',
        AjaxSelectFieldWidget,
        vocabulary='plone.app.vocabularies.Keywords'
    )


class IQuestionPost(Interface):
    """
    Marker interface for an IDiscussionPost object that also is a question.
    """


class IAnswer(IBaseDiscussionContent):
    """Answer to a question"""


class IDiscussionFlow(model.Schema):
    """Discussion flow (board) contains discussion and question content"""

    review_posts = schema.Bool(
        title=_(u'label_review_posts', default=u'Review new posts?'),
        description=_(
            u'help_review_posts',
            default=u'Should new posts be held for review?'
            ),
        default=False,
        )

    review_comments = schema.Bool(
        title=_(u'label_review_comments', default=u'Review comments?'),
        description=_(
            u'help_review_comments',
            default=u'Should comments be moderated?'
            ),
        default=False,
        )

