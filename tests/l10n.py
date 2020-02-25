
from unittest.mock import patch

import os

import pycountry

from bcp47 import bcp47
from bcp47l10n import (
    bcp47_langs, bcp47_regions, bcp47_variants,
    gettext, supported_locales)


def test_supported_locales():
    assert (
        supported_locales()
        == {
            x.replace("_", "-").replace("@", "-"): x
            for x in os.listdir(pycountry.LOCALES_DIR)})
    assert(
        list(supported_locales.cache_info())
        == [0, 1, 128, 1])
    assert (
        supported_locales()
        == {
            x.replace("_", "-").replace("@", "-"): x
            for x in os.listdir(pycountry.LOCALES_DIR)})
    assert(
        list(supported_locales.cache_info())
        == [1, 1, 128, 1])


def test_langs():
    assert (
        bcp47_langs()
        == {x: y["Description"][0] for x, y in bcp47["languages"].items()})
    assert(
        list(bcp47_langs.cache_info())
        == [0, 1, 128, 1])
    assert (
        bcp47_langs()
        == {x: y["Description"][0] for x, y in bcp47["languages"].items()})
    assert(
        list(bcp47_langs.cache_info())
        == [1, 1, 128, 1])


def test_regions():
    assert (
        bcp47_regions()
        == {x: y["Description"][0] for x, y in bcp47["regions"].items()})
    assert(
        list(bcp47_regions.cache_info())
        == [0, 1, 128, 1])
    assert (
        bcp47_regions()
        == {x: y["Description"][0] for x, y in bcp47["regions"].items()})
    assert(
        list(bcp47_regions.cache_info())
        == [1, 1, 128, 1])


def test_variants():
    assert (
        bcp47_variants()
        == {x: y["Description"][0] for x, y in bcp47["variants"].items()})
    assert(
        list(bcp47_variants.cache_info())
        == [0, 1, 128, 1])
    assert (
        bcp47_variants()
        == {x: y["Description"][0] for x, y in bcp47["variants"].items()})
    assert(
        list(bcp47_variants.cache_info())
        == [1, 1, 128, 1])


@patch("bcp47l10n.bcp47_variants")
@patch("bcp47l10n.bcp47_regions")
@patch("bcp47l10n.bcp47_langs")
@patch("bcp47l10n.bcp47")
@patch("bcp47l10n.country_gettext")
@patch("bcp47l10n.language_gettext")
def test_gettext(m_lang, m_country, m_bcp, m_langs, m_regions, m_variants):
    m_langs.return_value.__contains__.return_value = True
    m_langs.return_value.__getitem__.side_effect = lambda x: x.upper()
    m_lang.return_value = lambda x: "TRANSLATED: %s" % x
    result = gettext("zu")
    assert (
        list(m_lang.call_args)
        == [('en',), {}])
    assert (
        list(m_langs.call_args)
        == [(), {}])
    assert not m_regions.called
    assert not m_variants.called
    assert not m_bcp.called
    assert not m_country.called
    assert result == 'TRANSLATED: ZU'


@patch("bcp47l10n.bcp47_variants")
@patch("bcp47l10n.bcp47_regions")
@patch("bcp47l10n.bcp47_langs")
@patch("bcp47l10n.bcp47")
@patch("bcp47l10n.country_gettext")
@patch("bcp47l10n.language_gettext")
def test_gettext_missing(m_lang, m_country, m_bcp,
                         m_langs, m_regions, m_variants):
    gettext.cache_clear()
    m_langs.return_value.__contains__.return_value = False
    m_langs.return_value.__getitem__.side_effect = lambda x: x.upper()
    m_lang.return_value = lambda x: "TRANSLATED: %s" % x

    result = gettext("zu")
    assert (
        list(m_lang.call_args)
        == [('en',), {}])
    assert (
        list(m_langs.call_args)
        == [(), {}])
    assert not m_regions.called
    assert not m_variants.called
    assert not m_bcp.called
    assert not m_country.called
    assert result == 'zu'


@patch("bcp47l10n.bcp47_variants")
@patch("bcp47l10n.bcp47_regions")
@patch("bcp47l10n.bcp47_langs")
@patch("bcp47l10n.bcp47")
@patch("bcp47l10n.country_gettext")
@patch("bcp47l10n.language_gettext")
def test_gettext_locale(m_lang, m_country, m_bcp,
                        m_langs, m_regions, m_variants):
    gettext.cache_clear()
    m_langs.return_value.__contains__.return_value = True
    m_langs.return_value.__getitem__.side_effect = lambda x: x.upper()
    m_lang.return_value = lambda x: "TRANSLATED: %s" % x

    result = gettext("zu", locale="fr")
    assert (
        list(m_lang.call_args)
        == [('fr',), {}])
    assert (
        list(m_langs.call_args)
        == [(), {}])
    assert not m_regions.called
    assert not m_variants.called
    assert not m_bcp.called
    assert not m_country.called
    assert result == 'TRANSLATED: ZU'
