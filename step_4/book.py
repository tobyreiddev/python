from author import Author


class Book:
    def __init__(self, title, revision, authors):
        self.title = title
        self.revision = revision
        self.authors = authors

    def lend(self, username):
        print(
            "Book: {} ({}, {})\nLent by: {}".format(
                self.title, self.authors.name, self.authors.firstName, username
            )
        )
