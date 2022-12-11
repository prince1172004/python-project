print("Read the insturctions carefully.\n0-to exit code \n1- to see all contacts\n2-To add contacts \n3-To access contact")
numbers = {"Aryan Raj": 9934300594, "Abhi Raj": 6200978658, "Rakesh Jagdev": 7848998796, "Anushka Sagar": 7395929210,
           "Aravindh": 9865185910,
           "Hardik Harsh": 9818624454, "Omkar Ashish": 7854852832, "Rishabh": 7209029115, "Soumya": 6299240326,
           "vidisha": 7307072678, "Vardhan": 6302429577,"Pavan Kalyan":9100528708}


def access():
    """to access all contacts presented in repository"""
    for i, j in numbers.items():
        print(i, ":\t", j)
    return input_in()


def add():
    """to add contacts"""
    name = input("Enter name: ")
    ph_no = int(input("phone no: "))
    numbers[name] = ph_no
    print("the number is successfully added")
    return input_in()


def single():
    name = input("Enter name: ")
    print(name, "\t", numbers[name])
    return input_in()


def check_in(a):
    if a == 0:
        print("Thank u for visiting")
    elif a == 1:
        return access()
    elif a == 2:
        return add()
    elif a == 3:
        return single()
    else:
        print("please check given input.")
        return input_in()


def input_in():
    n = int(input("choose a number: "))
    check_in(n)


input_in()