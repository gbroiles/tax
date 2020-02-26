import datetime
import t1040

def test_age1():
    testday = datetime.datetime(1969,1,1)
    result = t1040.age_at_year_end(testday)
    print(result)
