
import os
from functools import lru_cache

import gettext as _gettext
import pycountry

from bcp47 import bcp47, BCP47Exception


@lru_cache()
def supported_locales():
    return {
        x.replace("_", "-").replace("@", "-"): x
        for x in os.listdir(pycountry.LOCALES_DIR)}


@lru_cache()
def country_gettext(locale):
    supported = supported_locales()
    if locale == "en" or locale not in supported:
        return lambda x: x
    return _gettext.translation(
        'iso3166',
        pycountry.LOCALES_DIR,
        languages=[supported[locale]]).gettext


@lru_cache()
def language_gettext(locale):
    supported = supported_locales()
    if locale == "en" or locale not in supported:
        return lambda x: x
    return _gettext.translation(
        'iso639-3',
        pycountry.LOCALES_DIR,
        languages=[supported[locale]]).gettext


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
def gettext(lang_code, locale="en"):
    lang_trans = language_gettext(locale)
    bcp47langs = bcp47_langs()
    if "-" not in lang_code:
        return (
            lang_trans(bcp47langs[lang_code])
            if lang_code in bcp47langs
            else lang_code)
    try:
        _lang = bcp47(lang_code)
    except BCP47Exception:
        return lang_code
    name = lang_trans(bcp47langs[_lang.language])

    # handle grandfathereds ?
    # localize the output string ?

    if _lang.variant:
        bcp47variants = bcp47_variants()
        return (
            "%s (%s)"
            % (name,
               bcp47variants[_lang.variant]))
    if _lang.region:
        country_trans = country_gettext(locale)
        bcp47regions = bcp47_regions()
        return (
            "%s (%s)"
            % (name,
               country_trans(bcp47regions[_lang.region])))
