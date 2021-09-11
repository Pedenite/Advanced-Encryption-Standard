class Jpg:
    def __init__(self, content):
        self.content = content
        self.is_jpg = False
        self.headers = self.get_headers()

    def get_headers(self):
        if len(self.content) < 10:
            return None

        begin = [0xff, 0xd8, 0xff]
        end = [0xff, 0xd9]
        for i in range(len(begin)):
            if self.content[i] != begin[i]:
                return None

        if self.content[-1] != end[1] or self.content[-2] != end[0]:
            return None

        self.is_jpg = True
        headers = None
        print("Separando headers do JPG")
        for i in range(len(self.content)):
            if self.content[i] == 0xff and self.content[i+1] == 0xda:
                headers = self.content[:i+14]
                self.content = self.content[i+14:-2]
                break

        return headers
