def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    months = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
    
    
    
    return 0

def Is_leap_year(year):
    result = False
    if year % 4 == 0:
        if year % 100 != 0:
            if year % 400 == 0:
                result = True
        
    return result

def testIs_leap_year():
    # test leap year
    assert(Is_leap_year(2012) == True)
    # test if year is multple of 100
    assert(Is_leap_year(1900) == False)
    # test leap year
    assert(Is_leap_year(2324) == True)
    # test not leap year
    assert(Is_leap_year(2001) == False)


def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
# testDaysBetweenDates()
testIs_leap_year()