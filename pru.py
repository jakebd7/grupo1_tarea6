#a = {"Matematica": {"Jose": 95, "Roberto": 10, "Juan": 74}, "Robotica": {"Maria": 75, "Miguel": 84, "Esteban": 63, "Timoteo": 49}, "Ingles": {"Jose": 17, "Miguel": 13}}

def cicle(a,b):

    f = "Que tristesa"

    for i in range(a,b,1):
        print(i)

        if i == 5:
            return print("que honda")

    return f

cicle(1,20)