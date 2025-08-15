ANNUAL = 0.05
MONTHLY = ANNUAL / 12
from customUtils import read_base, read_month, print_monthly_savings
def main():
    base = read_base()
    month = read_month()
    print_monthly_savings(base, month, MONTHLY)

main()