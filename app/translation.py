from modeltranslation.translator import translator, TranslationOptions
from .models import Home


class NewsTranslationOptions(TranslationOptions):
    fields = ('rental_period',)


translator.register(Home, NewsTranslationOptions)
