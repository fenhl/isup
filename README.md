**isup** is a Python 3 script that uses [isup.me][isupme] to check if a website is up or down, based on [this Python 2 script][gistisup].

This is `isup` version 1.1.2 ([semver][]). The versioned API includes the usage pattern, as found in the docstring of [`isup.py`](isup.py), as well as the meanings of the statuses, described in the *Statuses* section below.

Requirements
============

*   [docopt][]
*   [fancyio][]

Changes
=======

The following things have been changed:

*   The script has been updated to Python 3.
*   Multiple websites are now checked concurrently.
*   The script now prints the status in a fancy output box before the domain name. The meanings of the statuses are described below.

Statuses
========

*   `[....]` The website is still being checked.
*   `[ UP ]` The website is up, according to [isup.me][isupme].
*   `[DOWN]` The website is down for everyone, according to [isup.me][isupme]. Note that if the structure of the [isup.me][isupme] website changes in the future, this may be erroneously displayed instead of `[ UP ]`.
*   `[ ?! ]` An error occured while checking the website, for example [isup.me][isupme] could not be reached.

[docopt]: http://docopt.org/ (docopt)
[fancyio]: https://github.com/fenhl/fancyio
[gistisup]: https://gist.github.com/andrix/1423960#file-isup-py (gist:andrix/isup.py)
[isupme]: http://isup.me/ (isup.me)
[semver]: http://semver.org/ (Semantic Versioning 2.0.0)
