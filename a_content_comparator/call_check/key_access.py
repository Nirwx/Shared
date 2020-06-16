class Keys:

    def __init__(self, data, url):
        self.d = data
        self.url = url

    def title(self):
        try:
            title = self.d['content'][0]['title']
        except KeyError:
            title = ' '
            print('Missing Title key for: ', self.url)
        return title

    def ID(self):
        try:
            ID = self.d['content'][0]['altID']['ID']
        except KeyError:
            ID = ' '
            print('Missing ID key for: ', self.url)
        return ID

    def parentId(self):
        try:
            parentId = self.d['content'][0]['altID']['parentId']
        except KeyError:
            parentId = ' '
           # print('Missing parentId key for: ', self.url)
        return parentId

    def rootId(self):
        try:
            rootId = self.d['content'][0]['altID']['rootId']
        except KeyError:
            rootId = ' '
            print('Missing rootId key for: ', self.url)
        return rootId

    def mediaId(self):
        try:
            mediaId = self.d['content'][0]['altID']['mediaId']
        except KeyError:
            mediaId = ' '
            print('\n Missing mediaId key for: ', self.url)
        return mediaId

    def currentProductIds(self):
        try:
            cProductIds = self.d['content'][0]['custom']['currentProductIds']
        except KeyError:
            cProductIds = ' '
            print('Missing currentProductIds key for: ', self.url)
        return cProductIds

    def availability(self):
        try:
            availability = self.d["content"][0]["availability"]
        except KeyError:
            availability = ' '
            print('Missing availaility key for: ', self.url)
        return availability

