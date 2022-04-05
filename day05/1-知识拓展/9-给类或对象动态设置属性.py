"""
    setattr(对象/类，attr,value)
    getattr(对象/类，attr)
    hasattr(对象/类，attr,value) True表示有attr,False表示没有attr
    delattr(对象/类，attr,value)
"""
class Data:
    pass

setattr(Data,"token","hdjarhjaegrjkwbfj9823592bnwdkjgwqy8v")
if hasattr(Data,"token"):
    value = getattr(Data,"token")
    print(value)
    delattr(Data,"token")

