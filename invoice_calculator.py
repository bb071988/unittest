def divide_pay(amount, staff_hours):
    """
    Divide an invoice evenly amongst staff depending on how many hours they
    worked on a project
    """
    total_hours = 0
    for person in staff_hours:
        if staff_hours[person] >= 0:
            total_hours += staff_hours[person]
        else:
            raise ValueError("Can't have negative hours")
        
    if total_hours == 0:
        raise ValueError("No hours entered")

    per_hour = amount / total_hours

    staff_pay = {}
    for person in staff_hours:
        pay = staff_hours[person] * per_hour
        staff_pay[person] = pay

    return staff_pay

def main():
    staff_pay = divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0})
    for person, pay in staff_pay.iteritems():
        print "{} should be paid ${:.2f}".format(person, pay)

if __name__ == "__main__":
    main()