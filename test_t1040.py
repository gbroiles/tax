import datetime
import t1040

def test_age1():
    testday = datetime.datetime(1969,1,1)
    taxreturn = t1040.taxReturn
    result = taxreturn.age_at_year_end(testday)
    print(result)

test_age1()
