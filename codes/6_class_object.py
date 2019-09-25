class Student:
    __name = ''
    __rollNo = 0
    __id = 0
    def __init__(self,n,r,i):
        self.__name = n
        self.__rollNo = r
        self.__id = i
    def show_data(self):
        print("Name = ",self.__name)
        print("Roll No. = ",self.__rollNo)
        print("Id = ",self.__id)

if __name__ == "__main__":
    s = Student("Vikas",342323,23)
    print(s.show_data())
