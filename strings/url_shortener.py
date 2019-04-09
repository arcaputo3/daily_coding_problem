"""
This problem was asked by Microsoft.
Implement a URL shortener with the following methods:
•	shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
•	restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""


class URL_shortener():
    """ URL Shortener:
    Returns six-character alphanumeric strings
    representing underlying url address. """

    def __init__(self):
        self._url_map = {}

    def shorten(self, url):
        """
        Args:
            url: str representing url address
        Returns:
            six-character alphanumeric string
        """
        short = hex(hash(url))[3:9]
        self._url_map[short] = url
        return short

    def restore(self, short):
        """
        Args:
            short: six-character alphanumeric string
        Returns:
            original str representing url (if exists)
        """
        return self._url_map[short] if short in self._url_map else None


if __name__ == "__main__":
    # Test cases
    shortener = URL_shortener()
    url_1 = "https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html"
    url_2 = "https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html"
    url_3 = "python.org"
    short_1 = shortener.shorten(url_1)
    short_2 = shortener.shorten(url_2)
    print(short_1)
    print(short_2)
    print(shortener.restore(url_3))
    print(shortener.restore(short_1) == url_1)
    print(shortener.restore(short_1) == url_2)
    print('Probability of collision: ', 16**-6 * 100, '%')
