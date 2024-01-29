class Assignment2:
    def __init__(self, year):
        self.year = year
    def tellAge(self, currentYear):
        age = currentYear - self.year
        print(f"Your age is {age}")
    def listAnniversaries(self):
        currentYear = 2022
        return [i for i in range(10, (currentYear - self.year) + 1, 10)]
    def modifyYear(self, n):
        year_str = str(self.year)
        first_two = year_str[:2] * n
        odd_chars = year_str[::2] * n
        return first_two + odd_chars
    @staticmethod
    def checkGoodString(string):
        if len(string) >= 9 and string[0].islower() and sum(c.isdigit() for c in string) == 1:
            return True
        return False
    @staticmethod
    def connectTcp(host, port):
        import socket
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((host, port))
            return True
        except:
            return False
retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")
