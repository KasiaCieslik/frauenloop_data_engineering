import numpy as np
from datetime import date,datetime


def surface_of_square(length_of_side):
    
    """Calculates square surface:

    Parameters
    ----------
    length_of_side: float
        length 

    Returns
    -------
    float
    without round
    """
    return length_of_side**2



def check_prime_number(number:int) -> bool:
    """Check if the number is prime:

    Parameters
    ----------
    number: int

    Returns
    -------
    bool
        True if prime, False otherwise.
    """
    if number == 1:
            return False
    for i in range(2,number):
        if number%i==0:
            return False
    return True


def is_leap(year:int) -> bool:
    """Calculates if the zear is leap or not:

    Parameters
    ----------
    year: int

    Returns
    -------
    bool
    True if leap, False otherwise.
    """
    leap = False
    if year % 4 == 0 and year%100!=0:
        leap = True   
    elif year%4 == 0 and year % 100 == 0 and year%400 == 0:
        leap = True
    else:
        leap = False
    return leap


  
def get_today() -> date.today:
    """Return date which is today:

    Parameters
    ----------
    None
    
    Returns
    -------
    datetime.date
    """
    return date.today()

def calculate_age_in_days(birthdate: str = '1989/04/15') -> str:
    """Calculates how many days old you are:

    Parameters
    ----------
    birthdate: str
    Birthdate in format '%Y/%m/%d'
    
    Returns
    -------
    str
    """
    today = get_today()
    birthday = datetime.strptime(birthdate,'%Y/%m/%d').date()
    days = today-birthday
    return str(days).split(',')[0]


def nearest_square(number:float) -> float:
    """Calculates the nearest square root 
    to the given number:

    Parameters
    ----------
    number: float

    Returns
    -------
    float
    """
   
    if number < 0:
        return 0
    elif number>0:
        return round(np.sqrt(number))**2

BASE = 4
EXTRA = 0.25

def taxi_fares(traveled_distance_km: float) -> float:
    """Calculates the taxi fare,
    the base fare is 4 $ and for every 140 m
    traveled another 0.25 $ would be added ):

    Parameters
    ----------
    traveled_distance_km: float
        Distance in km


    Returns
    -------
    float
        Fare in $, rounded to cents
    """
    traveled_distance_meter = traveled_distance_km * 1000
    extra_fee_traveled_distance = traveled_distance_meter/140
    
    return round(BASE + extra_fee_traveled_distance*EXTRA,2)



