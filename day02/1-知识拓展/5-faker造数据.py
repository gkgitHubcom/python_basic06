from faker import Faker

f = Faker("zh_CN")
print(f.phone_number())