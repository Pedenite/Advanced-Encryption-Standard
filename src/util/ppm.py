class Ppm:
    def __init__(self, content):
        self.content = content
        self.is_ppm = False
        self.headers = self.get_headers()

    def get_headers(self):
        begin = [ord('P'), ord('6'), ord('\n')]
        for i in range(len(begin)):
            if self.content[i] != begin[i]:
                return None

        i += 1
        valid = False
        while self.content[i] != ord('\n'):
            if self.content[i] == ord(' ') and valid:
                valid = False
                break

            if self.content[i] == ord(' ') and not valid:
                valid = True
            
            i += 1

        if not valid:
            return None

        end = [ord('2'), ord('5'), ord('5'), ord('\n')]
        for elem in end:
            i += 1
            if self.content[i] != elem:
                return None

        i += 1
        
        self.is_ppm = True
        header = self.content[:i]
        self.content = self.content[i:]
        return header
