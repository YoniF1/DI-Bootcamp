class Pagination():

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.start_index = 0
        self.end_index = self.start_index + pageSize
        self.size = len(items)

    def getVisibleItems(self):
        print(self.items[self.start_index:self.end_index:])
            
    def nextPage(self):
        self.start_index += self.pageSize
        self.end_index += self.pageSize

    def prevPage(self):
        self.start_index -= self.pageSize
        self.end_index -= self.pageSize

    def lastPage(self):
        remaining = self.size % self.pageSize
        self.start_index = self.size - remaining
        self.end_index = self.size

    def goToPage(self, pageNum):
        self.start_index = (pageNum * self.pageSize) - self.pageSize
        self.end_index = pageNum * self.pageSize


alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]



        