class BasePage:

    url = None

    def __init__(self, page):
        self.page = page

    def open_page(self):
        if self.url:
            self.page.goto(self.url)
        else:
            print('Not possible to open page without url')
            