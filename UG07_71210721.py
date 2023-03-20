class Browser:
    def init(self):
        self.data: list = []
        self.list_url: list = []
        self.index = 0

    def len(self):
        return len(self.data)

    def go(self, url: str):
        self.list_url.append(url)
        self.data.append(url)
        self.index += 1

    def back(self):
        self.data.pop()
        self.index -= 1
        print(self.data[self.index - 1])

    def forward(self):
        self.data.append(self.list_url[self.index])
        print(self.data[self.index])

    def printAll(self):
        print(self.data)