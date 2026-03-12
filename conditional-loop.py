# if else condition
def mark_grade(marks):
    if marks >= 90 and marks <= 100:
        print("Grade: A")
    elif marks >= 80 and marks < 90:
        print("Grade: B")
    elif marks >= 70 and marks < 80:
        print("Grade: C")
    elif marks >= 60 and marks < 70:
        print("Grade: D")
    else:
        print("Grade: F")


def true():
    while True:
        number = int(input("Enter a number (0 to exit): "))
        if number == 0:
            print("Exiting the loop.")
            break
        elif number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

marks = int(input("Enter your marks: ")) # type casting to integer

if __name__ == "__main__":
    mark_grade(marks)
    true()