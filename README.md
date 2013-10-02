**isup** is a Python 3 script that uses [isup.me][isupme] to check if a website is up or down, based on [this Python 2 script][gistisup].

This is `isup` version 1.0.0 ([semver][]). The versioned API includes the usage pattern, as found in the docstring of [`isup.py`](isup.py).

Requirements
============

To run `isup`, you will need [docopt][].

Changes
=======

The following things have been changed:

*   The script has been updated to Python 3.
*   When checking multiple websites at once, the script now prints the result for each website before checking the next one.

[docopt]: http://docopt.org/ (docopt)
[gistisup]: https://gist.github.com/andrix/1423960#file-isup-py (gist:andrix/isup.py)
[isupme]: http://isup.me/ (isup.me)
[semver]: http://semver.org/ (Semantic Versioning 2.0.0)
