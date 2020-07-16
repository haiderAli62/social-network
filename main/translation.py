from modeltranslation.translator import translator, TranslationOptions
from modeltranslation.decorators import register
from .models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


#translator.register(Post, PostTranslationOptions)
