from datetime import datetime
from typing import Final


def kebab(str: str) -> str:
    """Return a string converted to kebab case.

    Non-alphanumeric characters are removed from `str`,
    whitespaces are replaced with hyphens, and alphabetical
    characters are all converted to lowercase.

    :param str: The string to be converted to kebab case
    :type str: str
    :return: A hyphen-separated string in lowercase
    :rtype: str

    TODO: Add support for converting strings written
    in snake_case and camelCase
    """

    # Split string in whitespaces
    words = str.split()

    # For every item in list
    for index, word in enumerate(words):

        # Recreate word excluding non-alphanumeric characters
        word = "".join([char for char in word if char.isalnum()])

        # Replace word in list with recreated word
        words[index] = word

    # Merge list into a single hyphenated string
    return "-".join(words).lower()


def generate_filename(
    subject: str,
    ext: str,
    classification: str = "",
    sep: str = "_",
) -> str:
    """Return a string concatenated from strings passed as
    arguments to the function.

    The return value is formatted in the following order
    from left to right: uppercased version of `classification`,
    `subject` in kebab-case excluding non-alphanumeric
    characters, ISO 8601 date in basic format (e.g. YYYYMMDD)
    when the file name was generated, and a dot-prefixed file
    name extension `ext`. These arguments are delimited by
    the string passed as `sep`.

    :param subject: The subject, theme, or title of the file
    :type subject: str
    :param ext: The file extension, which may or may not be
        prefixed with a dot
    :type ext: str
    :param classification: The classification under which the
        file falls. Defaults to an empty string
    :type classification: str, optional
    :param sep: A character separating the file name
        components. Defaults to an underscore
    :type sep: str, optional
    :return: A concatenation of strings passed as arguments
        to the function, separated by `sep`
    :rtype: str
    """
    CURR_DATE: Final[str] = datetime.now().strftime("%Y%m%d")
    filename_comps: list[str] = [kebab(subject) or "untitled", CURR_DATE]
    # Prefix an extension with a "." if it doesn't already have one,
    # and the extension is not an empty string
    if ext and not ext.startswith("."):
        ext = "." + ext

    if classification:
        filename_comps.insert(0, kebab(classification).upper())
    return sep.join(filename_comps) + ext
