
import os

import pycountry

from bcp47 import bcp47
from bcp47l10n import (
    bcp47_langs, bcp47_regions, bcp47_variants,
    supported_locales)


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
