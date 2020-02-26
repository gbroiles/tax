import datetime
import t1040


def test_age1():
    testday = datetime.datetime(1969, 1, 1)
    taxreturn = t1040.TaxReturn
    taxreturn.taxpayer_date_of_birth = testday
#    result = taxreturn.age_at_year_end(testday)
#    print(result)

treturn = t1040.TaxReturn
treturn.gross_income = 10000
print(treturn.gross_income)

print(test_age1())

treturn.hello("world")

