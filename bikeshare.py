# This project was given by Udacity 
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city = ""
    month = ""
    day = ""
    # lower() method was applied to accept any upper and lower combination while inputting

    while city != "chicago" and city != "new york city" and city != "washington" :
        city_raw = input("type either chicago or new york city or washington:")
        city = city_raw.lower()  
        print(city, "was selected")
        # TO DO: get user input for month (all, january, february, ... , j     month = ""
    while month != "all" and month != "january" and month != "february" and month != "march" and month != "april" and month != "may" and month != "june" :
        month_raw = input("user input for month (all, january, february, ... , june):")  
        month = month_raw.lower()
        print(month, "was selected")

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day != "all" and day != "monday" and day != "tuesday" and day != "wednesday" and day != "thursday" and day != "friday" and day != "saturday" and day != "sunday": 
        day_raw = input("user input for month (all, monday, tuesday, ... sunday):")  
        day = day_raw.lower()
        print(day, "was selected")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # day_name for python 0.23


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_int = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month_int]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print ('The most common month is {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print ('The most common day of week is {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print ('The most common start hour is {}'.format(df['Start Time'].dt.hour.mode()[0]))
       
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station is {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('most commonly used end station is {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start-End'] = df['Start Station']+' and '+ df['End Station']
    print('most frequent combination is {}'.format(df['Start-End'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('mean travel time is {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user type is\n',df['User Type'].value_counts())
    # Hint: You can use try/except or if/else conditions.
    # If user_stats encounter KeyError, handle this by try and except sentence  
    try:
    # TO DO: Display counts of gender
        print('counts of gendar is\n',df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        print('most earliest year is {}, recent year is {}, common year is {}'.format(df['Birth Year'].min(0),df['Birth Year'].max(0),df['Birth Year'].mode()[0]))

    except KeyError:
        print("washington data doesn't have Gender data and Birth Year data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Added new function for showing consective 5 rows data by asking user 

def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Hit "Y" or "N"\n').lower()
    start_loc = 0
    
    if view_data == 'y':

        while True:
            print(df.iloc[start_loc:start_loc+5])
            view_display = input("Do you wish to continue?: Hit 'Y' or 'N' :").lower()

            if view_display != 'y':
                break
            else:
                start_loc += 5

    elif view_data == 'n':
        print("We don't display data")

    else:
        print("You entered incorrect input, only 'Y' or 'N' is allowed")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? hit "Y" or "N"\n')
        if restart.lower() != 'y':
            break


if __name__ == "__main__":
	main()

