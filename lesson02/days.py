mon=1
tue=2
wed=3
thu=4
fri=5
sat=6
sun=7
class Person():
    def __init__(self,name:str,age:int) :
        self.__name=name
        self.__age=age
    def __repr__(self)->str:
        return f'我的名字:{self.name}\n我的age{self.age}'
    @property
    def name(self)->str:
        return self.__name
    @property
    def age(self) -> int:
        return self.__age
class Student(Person):
    def __init__(self, name: str, age: int, chinese:int=0 ,english:int=0, math:int=0):
        super().__init__(name=name, age=age)
        self.chinese=chinese
        self.english=english
        self.math=math
    @property
    def total(self)->int:
        return self.chinese+self.english+self.math
    def average(self)->float:
        return round(self.total/3,ndigits=2)
def get_person(name:str, age:int)->Person:
    return Person(name=name,age=age)
def get_student(name:str,age:int,chinese=60,english=60,math=60)->Student:
    return Student(name=name,age=age,chinese=chinese,english=english,math=math)