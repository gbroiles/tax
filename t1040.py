""" modules for income tax """
import datetime


class taxReturn:
    """ Tax return class """

    personal_exemptions = {
        "single": 12200,
        "mfj": 24400,
        "ss": 24400,
        "hoh": 18350,
        "mfs": 12200,
    }

    # brackets = min, max, base, rate
    tax_table = {
        "mfj": [
            [0, 19400, 0, 0.10],
            [19400, 78950, 1940, 0.12],
            [78950, 168400, 9086, 0.22],
            [168400, 321450, 28765, 0.24],
            [321450, 408200, 65497, 0.32],
            [408200, 612350, 93257, 0.35],
            [612350, None, 165709.50, 0.37],
        ],
        "ss": [
            [0, 19400, 0, 0.10],
            [19400, 78950, 1940, 0.12],
            [78950, 168400, 9086, 0.22],
            [168400, 321450, 28765, 0.24],
            [321450, 408200, 65497, 0.32],
            [408200, 612350, 93257, 0.35],
            [612350, None, 165709.50, 0.37],
        ],
        "hoh": [
            [0, 13850, 0, 0.10],
            [13850, 52850, 1385, 0.12],
            [52850, 84200, 6065, 0.22],
            [84200, 160700, 12962, 0.24],
            [160700, 204100, 31322, 0.32],
            [204100, 510300, 45210, 0.35],
            [510300, None, 152380, 0.37],
        ],
        "single": [
            [0, 9700, 0, 0.10],
            [9700, 39475, 970, 0.12],
            [39475, 84200, 4543, 0.22],
            [84200, 160725, 14382.5, 0.24],
            [160725, 204100, 32748.5, 0.32],
            [204100, 510300, 46628.5, 0.35],
            [510300, None, 153798.5, 0.37],
        ],
        "mfs": [
            [0, 9700, 0, 0.10],
            [9700, 39475, 970, 0.12],
            [39475, 84200, 4543, 0.22],
            [84200, 160725, 14382.5, 0.24],
            [160725, 204100, 32748.5, 0.32],
            [204100, 306175, 46628.5, 0.35],
            [306175, None, 82354.75, 0.37],
        ],
    }

    def __init__(self):
        self.taxpayername = ""
        self.baseform = "1040"
        self.tax_year = "2019"
        self.filingstatus = ""
        self.gross_income = 0
        self.adjusted_gross_income = 0
        self.itemized_deduction_total = 0
        self.personal_exemption = 0
        self.tax_year_end = datetime.date(2019, 12, 31)
        self.taxpayer_blind = False
        self.spouse_blind = False

    def age_at_year_end(self, date_of_birth):
        """ Calculates age in years as of last day of tax year """
#        if date_of_birth == "" and not self.taxpayer_date_of_birth:
#            raise ValueError("Date of birth not set, cannot caclulate age")

#        if date_of_birth == "":
#            date_of_birth = self.taxpayer_date_of_birth

#        if date_of_birth > self.tax_year_end:
#            return 0
        daysold = self.tax_year_end - date_of_birth
        return daysold.days // 365  # days // 365 = years old at end of tax year

    def age_today(self, date_of_birth):
        """ Calculates age in years as of today """
        if date_of_birth == "" and not self.taxpayer_date_of_birth:
            raise ValueError("Date of birth not set, cannot caclulate age")

        if date_of_birth == "":
            date_of_birth = self.taxpayer_date_of_birth

        daysold = datetime.date.today() - date_of_birth
        return daysold // 365


