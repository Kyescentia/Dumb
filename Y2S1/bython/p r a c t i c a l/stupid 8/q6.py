from customUtils import read_work_hours, calculate_total_wage, calculate_regular_pay, calculate_OT_pay

def main():
    hours = read_work_hours()
    print("\n{:<15s} RM{:.2f}".format("Total wage", calculate_total_wage(hours)))
    print("{:<15s} RM{:.2f}".format("Regular pay", calculate_regular_pay(hours)))
    print("{:<15s} RM{:.2f}".format("Overtime pay", calculate_OT_pay(hours)))

main()