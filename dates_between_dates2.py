def IsLeapYear(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
        
    return False

def daysInMonth(year, month):
    leap = IsLeapYear(year)
    if leap and month == 2:
        return 29
    
    months = {'1': 31, '2': 28, '3': 31, '4': 30, 
                    '5': 31, '6': 30, '7': 31, '8': 31, 
                    '9': 30, '10': 31, '11': 30, 
                    '12': 31}

    return months[str(month)]

def nextDay(year, month, day):
    """
    Calculates the next day given a date separated by year, month and day
    """
    if day < daysInMonth(year, month):
        return (year, month, day+1)
    else:
        day = 1
        if month < 12:
            return (year, month+1, day)
        else:
            month = 1
            return (year+1, month, day)

def are_dates_valid(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return False
    elif year1 == year2:
        if month1 > month2:
            return False
        elif month1 == month2:
            if day1 > day2:
                return False
    return True

def isSameDate(year1, month1, day1, year2, month2, day2):
    if year1 == year2 and month1 == month2 and day1 == day2:
        return True
    else:
        return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    
    # TODO - by the end of this lesson you will have
    #  completed this function. You do not need to complete
    #  it yet though! 
    
    days = 0
    
    if are_dates_valid(year1, month1, day1, year2, month2, day2):
        while are_dates_valid(year1, month1, day1, year2, month2, day2):
            if isSameDate(year1, month1, day1, year2, month2, day2):
                break
            else:
                days += 1
                year1, month1, day1 = nextDay(year1, month1, day1)
    else:
        return "undefined"

    return days


# TESTS

def test_IsLeapYear():
    # test leap year
    assert(IsLeapYear(2012) == True)
    # test if year is multple of 100
    assert(IsLeapYear(2100) == False)
    # test leap year
    assert(IsLeapYear(2000) == True)
    # test leap year
    assert(IsLeapYear(2008) == True)
    # test not leap year
    assert(IsLeapYear(2017) == False)
    print("are_dates_valid() function passed")

def test_are_dates_valid():
    assert(are_dates_valid(2012, 2, 28, 2017, 1, 28) == True)
    assert(are_dates_valid(2014, 3, 30, 2014, 3, 29) == False)
    assert(are_dates_valid(2018, 5, 7, 2019, 6, 8) == True)
    assert(are_dates_valid(2017, 12, 30, 2017, 12, 30) == True)
    assert(are_dates_valid(2017, 12, 30, 2018, 1,  1) == True)


    print("IsLeapYear() function passed")



def test_nextDay():
    
    assert(nextDay(2017, 12, 31) == (2018, 1, 1))

    assert(nextDay(2012, 2, 28) == (2012, 2, 29))

    assert(nextDay(2014, 3, 31) == (2014, 4, 1))

    assert(nextDay(2018, 5, 7) == (2018, 5, 8))

    print("nextDay() function passed")



def test_daysInMonth():
    assert(daysInMonth(2017, 12) == 31)

    assert(daysInMonth(2012, 2) == 29)

    assert(daysInMonth(1940, 2) == 29)

    assert(daysInMonth(2018, 5) == 31)

    assert(daysInMonth(2016, 11) == 30)

    print("daysInMonth() function passed")

def test_isSameDate():
    assert(isSameDate(2017, 12, 30, 2017, 12, 30) == True)
    assert(isSameDate(2018, 1, 1, 2018, 1, 1) == True)
    assert(isSameDate(2017, 12, 30, 2017, 12, 31) == False)
    assert(isSameDate(2014, 5, 7, 2014, 5, 7) == True)
    assert(isSameDate(2017, 11, 29, 2017, 12, 30) == False)
    print("isSameDate() function passed")

def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 31, 
                              2018, 1,  1)  == 1)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")
    
test_IsLeapYear()
test_nextDay()
test_are_dates_valid()
test_daysInMonth()
test_isSameDate()
testDaysBetweenDates()
