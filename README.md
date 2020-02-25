
[![Build Status](https://travis-ci.org/phlax/python-bcp47-l10n.svg?branch=master)](https://travis-ci.org/phlax/python-bcp47-l10n)
[![codecov](https://codecov.io/gh/phlax/python-bcp47-l10n/branch/master/graph/badge.svg)](https://codecov.io/gh/phlax/python-bcp47-l10n)


## python-bcp47-l10n

Localised names for bcp47 language codes



### Python examples


You can localise language names using their `bcp47` codes. If no `locale` is provided, the default (ie `en`) `bcp47` names are used.

```
>>> import bcp47l10n

>>> bcp47l10n.gettext("en")
'English'
>>> bcp47l10n.gettext("en", locale="fr")
'anglais'
>>> bcp47l10n.gettext("en", locale="es")
'Inglés'
>>> bcp47l10n.gettext("en", locale="zh-CN")
'英语'

>>> bcp47l10n.gettext("en-GB")
'English (United Kingdom)'
>>> bcp47l10n.gettext("en-GB", locale="fr")
'anglais (Royaume-Uni)'
>>> bcp47l10n.gettext("en-GB", locale="es")
'Inglés (Reino Unido)'
>>> bcp47l10n.gettext("en-GB", locale="zh-CN")
'英语 (英国)'


>>> bcp47l10n.gettext("ca-valencia")
'Catalan (Valencian)'
>>> bcp47l10n.gettext("ca-valencia", locale="fr")
'catalan (Valencian)'
>>> bcp47l10n.gettext("ca-valencia", locale="es")
'Catalán (Valencian)'
>>> bcp47l10n.gettext("ca-valencia", locale="zh-CN")
'加泰罗尼亚语 (Valencian)'

```


If the locale is not recognised you get the default english name for the language code

```
>>> bcp47l10n.gettext("en-GB", locale="NOTALOCALE")
'English (United Kingdom)'
```

If the language code is not recognized (ie not valid BCP47) the original string is returned

```
>>> bcp47l10n.gettext("en-NOTAREGION", locale="zh-CN")
'en-NOTAREGION'
```
