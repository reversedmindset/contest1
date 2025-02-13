import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1, func, funx

@decorator_1
def test_typeBasedTransformer():
    print("Testing typeBasedTransformer:")
    result = typeBasedTransformer(
        num=4, text="Hello", flag=True,
        data=[1, 2, 3], mapping={"a": 1, "b": 2},
        unsupported={1, 2, 3}
    )
    print(result)

@decorator_1
def test_kwargsAcceptFun():
    print("Testing kwargsAcceptFun:")
    kwargsAcceptFun(name="Komron", age=22, country="Karakalpakstan", hobby="Music")

if __name__ == "__main__":
    func()
    funx()
    func()
    funx()
    func()
    test_typeBasedTransformer()
    test_kwargsAcceptFun()
