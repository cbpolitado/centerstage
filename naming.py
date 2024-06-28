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
