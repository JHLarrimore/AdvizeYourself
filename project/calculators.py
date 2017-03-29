from datetime import datetime, timedelta, date
from numpy import fv
def RetirementCalc(userInfo, interestRate):
    pv = -1*(userInfo["currentValue"])
    i = interestRate
    dob = datetime.strptime(userInfo["dob"], '%m/%d/%Y')
    currentAge = calculate_age(dob)
    dateRetire = add_years(dob, userInfo["age_at_retire"])
    companyMatch = float(100+userInfo["companyMatch"])/100
    pmt = -1*(userInfo["yearlyContributions"] * companyMatch)
    n = userInfo["age_at_retire"] - currentAge
    value = fv(i,n,pmt, pv)
    return value
    
def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
if __name__ == '__main__':
    userInfo = {"currentValue":10000, 
                "companyMatch":50,
                "income" : 80000,
                "yearlyContributions" : 8000,
                "age_at_retire" : 65,
                "dob" : "01/01/1987"}
    print RetirementCalc(userInfo, 0.07)
    