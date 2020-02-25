
from functools import lru_cache

import gettext
import pycountry

from bcp47 import bcp47


@lru_cache()
def country_gettext(language_code):
    return gettext.translation(
        'iso3166',
        pycountry.LOCALES_DIR,
        languages=[language_code])


@lru_cache()
def language_gettext(language_code):
    return gettext.translation(
        'iso639-3',
        pycountry.LOCALES_DIR,
        languages=[language_code])


@lru_cache()
def bcp47_langs():
    return {
        x: y["Description"][0]
        for x, y
        in bcp47["languages"].items()}


@lru_cache()
def bcp47_regions():
    return {
        x: y["Description"][0]
        for x, y
        in bcp47["regions"].items()}


@lru_cache()
def bcp47_variants():
    return {
        x: y["Description"][0]
        for x, y
        in bcp47["variants"].items()}


@lru_cache()
def bcp47_trans(lang, locale="en"):
    country_trans = country_gettext(locale)
    lang_trans = language_gettext(locale)
    bcp47langs = bcp47_langs()
    bcp47regions = bcp47_regions()
    bcp47variants = bcp47_variants()
    if "-" not in lang:
        if lang in bcp47langs:
            return lang_trans.gettext(bcp47langs[lang])
        return lang
    try:
        _lang = bcp47(lang)
    except Exception:
        return lang
    name = lang_trans.gettext(bcp47langs[_lang.language])
    if _lang.variant:
        return (
            "%s (%s)"
            % (name,
               bcp47variants[_lang.variant]))
    if _lang.region:
        return (
            "%s (%s)"
            % (name,
               country_trans.gettext(bcp47regions[_lang.region])))
