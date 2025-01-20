from faker import Faker

fake = Faker()
for i in range(1, 10):
    fakeAuthor = fake.name()
    print(f"{i}: {fake.name()} {fake.company_email()} ")
