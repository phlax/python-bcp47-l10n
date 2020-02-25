
from bcp47 import bcp47
from bcp47l10n import bcp47_langs


def test_bcp47_langs():
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
