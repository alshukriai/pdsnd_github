import time
import pandas as pd
import numpy as np
import os

#jfjklnnjkfdv

os.chdir('/Users/pro/Desktop/All projects/Udacity/\python and SQL for DS/3-python programming for DS')
print(os.getcwd())

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
    while(True):
        city = input('Enter a city (chicago, new york city, washington): ').lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Enter a valid city!')
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while(True):
        month = input('Enter a month or just type all to include all months (january, february, ... , june): ').lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Enter a valid month!')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while(True):
        day = input('Enter a day just type all to include all days (Sunday, Monday, Tuesday .... , Saturday): ').lower()
        if day not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('Enter a valid day!')
        else:
            break

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(most_common_month))

    # TO DO: display the most common day of week
    df['starting_day'] = df['Start Time'].dt.weekday_name
    most_common_day = df['starting_day'].mode()[0]
    print('The most common day of the week is: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    most_common_hour = df['start_hour'].mode()[0]
    print('The most common hour is: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    station_combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is: {}'.format(station_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum().round() / 60
    print('The total travel time = {} minutes'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean().round() / 60
    print('The mean travel time = {} minutes'.format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    UserType_count = df['User Type'].value_counts()
    print('The counts of user types = {}'.format(UserType_count))

    # TO DO: Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('The counts of gender = {}'.format(counts_of_gender))

    except:
        print('This city doesnt have a gender information.')
    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest birth year is: {}'.format(int(earliest_birth_year)))

        recent_birth_year = df['Birth Year'].max()
        print('The most recent birth year is: {}'.format(int(recent_birth_year)))

        common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is: {}'.format(int(common_birth_year)))

    except:
        print('This city doesnt have birth information.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_input(df):

    raw = input('whould you like to see raw data? [yes], [no]: ').lower()
    start = 5

    while(True):
        if raw == 'yes':
            print(df.head(start))
            start += 5
            raw = input('would you like to view 5 additional rows? [yes],[no]: ').lower()

        elif raw == 'no':
            break
        else:
            raw = input('Wrong command, please enter [yes] or [no]: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? [yes], [no].\n')

        while(True):
            if restart.lower() == 'yes':
                break

            elif restart.lower() == 'no':
                exit()

            else:
                restart = input('invalid entry. please enter [yes], [no]: ')



if __name__ == "__main__":
	main()
