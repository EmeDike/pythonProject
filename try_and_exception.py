try:
    age = int(input("Enter your age: "))
    result = 10 / age
    print(result)

except ZeroDivisionError:
    pass
except ValueError:
    print("Ur age cannot be String literally")
finally:
    print("try again, Thanks")
