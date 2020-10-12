import sys
import math
import argparse


def nop(p, a, i):
    base = 1 + i
    numeric_value = a / (a - i * p)
    result = int(math.ceil(math.log(numeric_value, base)))
    overpayment = int(a * result - p)
    if result == 1:
        return "It will take 1 month to repay this loan\nOverpayment = {}".format(overpayment)
    elif result % 12 == 0:
        years = int(result / 12)
        if years == 1:
            return "It will take 1 year to repay this loan\nOverpayment = {}".format(overpayment)
        else:
            return "It will take {} years to repay this loan\nOverpayment = {}".format(years, overpayment)
    else:
        years = int(result / 12)
        months = int(result % 12)
        if years == 0:
            return "It will take {} months to repay this loan\nOverpayment = {}".format(months, overpayment)
        else:
            return "It will take {} years and {} months to repay this loan\nOverpayment = {}" \
                .format(years, months, overpayment)


def ampa(p, n, i):
    i2 = (1 + i) ** n
    result = p * ((i * i2) / (i2 - 1))
    result = int(math.ceil(result))
    overpayment = int(result * n - p)
    return "Your annuity payment = {}!\nOverpayment = {}" \
        .format(result, overpayment)


def lp(a, n, i):
    i2 = (1 + i) ** n
    result = a * ((i2 - 1) / (i2 * i))
    result = int(result)
    overpayment = int(a * n - result)
    return "Your loan principal = {}!\nOverpayment = {}".format(result, overpayment)


def diff(p, n, i):
    total_result = 0
    for month in range(1, (n + 1)):
        result = int(math.ceil(p / n + i * (p - (p * (month-1)) / n)))
        print("Month {}: payment is {}".format(month, result))
        total_result += result
    overpayment = int(total_result - p)
    print("Overpayment = {}".format(overpayment))

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--principal", type=float)
args = parser.parse_args()
args2 = sys.argv
if len(args2) != 5:
    print("Incorrect parameters.")
elif not args.interest:
    print("Incorrect parameters.")
else:
    interest = args.interest / 1200
    if args.type == "annuity":
        if not args.payment:
            print(ampa(args.principal, args.periods, interest))
        elif not args.periods:
            print(nop(args.principal, args.payment, interest))
        else:
            print(lp(args.payment, args.periods, interest))
    elif args.type == "diff":
        diff(args.principal, args.periods, interest)