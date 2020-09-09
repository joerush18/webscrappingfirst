from item_locator.item_locator import ItemLocator


# get content of quotes details
class Parse:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'<Quotes = {self.content}  by {self.author} Tags:- {self.tags}>'

    @property
    def content(self):
        locator = ItemLocator.CONTENT
        quote = self.parent.find_element_by_css_selector(locator)
        return quote.text

    @property
    def author(self):
        locator = ItemLocator.AUTHOR
        author = self.parent.find_element_by_css_selector(locator)
        return author.text

    @property
    def tags(self):
        locator = ItemLocator.TAGS
        tags = self.parent.find_element_by_css_selector(locator)
        return [e for e in tags]
