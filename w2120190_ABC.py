# Author: M.U.M Afnan
# Date: 09/12/2024
# Student ID: 21201907


# Task A: Input Validation
def validate_date_input():  # Code used to get input of date (day, month, year) in a specific format.
    while True:
        while True:
            try:
                day = int(input("Please enter the day of the survey in the format dd: "))  # Allowing the user to input day and check if it's a within the valid range.
                if 1 <= day <= 31:
                    print()
                    break
                else:
                    print("Out of range - values must be in the range 1 to 31.")
            except ValueError:
                print("Integer required for day.")

        while True:
            try:
                month = int(input("Please enter the month of the survey in the format MM: "))  # Allowing the user to input month and check if it's a within the valid range.

                if 1 <= month <= 12:
                    num = f"{month:02}"
                    break
                else:
                    print("Out of range - values must be in the range 1 to 12.")
            except ValueError:
                print("Integer required for month.")

        while True:
            try:
                year = int(input("Please enter the year of the survey in the format YYYY: "))  # Allowing the user to input year and check if it's a within the valid range.
                if 2000 <= year <= 2024:
                    break
                else:
                    print("Out of range - values must range from 2000 to 2024.")
            except ValueError:
                print("Integer required for year.")

        leapYear = 0
        if year % 4 == 0:  # Equation use to find the leap year
            if year % 100 != 0 or year % 400 == 4:
                leapYear = year

        if month in [4,6,9,11,]:  # Check if the day range for the months of April, June, September, November is 30
            if day > 30:
                print(f"Invalid day {month:02} has only 30 days\n")
                continue

        elif (month == 2):  # Checking the no.of days in February is 28 or 29 based on type of year
            if leapYear:
                if day > 29:
                    print("Invalid day February in a leap year has only 29 days.\n")
                    continue
            else:
                if day > 28:
                    print("Invalid day February in a non-leap year has only 28 days.\n")
                    continue
        break

    day = f"{day:02}"  # converts the 'day' variable as a two-digit string

    date = (day + num + str(year))  # Converts 'day', 'num', and 'year' into a single string.

    file_path = ("traffic_data" + date + ".csv")  # Create the name of file using the provided file path

    histro_date = f"{day}/{num}/{year}"  # create a single string with the date in the format dd/mm/yyyy to use in histrogram

    return file_path, histro_date


# Ask user whether they want to generate another dataset.
def validate_continue_input():
    # loops until user provides the sutible answer
    while True:
        repeat = (input("\nDo you want to load another dataset? (Y or N): ").strip().upper())
        if repeat in ["Y", "N"]:
            condition = repeat
            break
        else:
            print("Invalid input you entered. Please enter 'Y' or 'N'.")
    return condition


# Task B: Processed Outcomes
def process_csv_data(file_name):

    # Open the CSV file in read mode
    file = open(file_name, "r")
    data = file.readlines()  # reading the CSV file line by line

    print()
    print("*************************** ")
    print("data file selected is", file_name)
    print("*************************** ")

    # Remove empty space and split each row by commas and convert into a lists
    for i in range(len(data)):
        data[i] = data[i].strip()
        data[i] = data[i].split(",")

    # assigning variabales
    vehicles_hour = {}
    elm_vehicles_per_hour = {}
    han_vehicles_per_hour = {}
    rain_hour = set()
    count = truck = electric = two_wheel = bus = forword = bike = speed = elm_road = han_road = scooter = truck_percentage = avg_bike = avg_scooter = total_rain = 0

    # Loop the data, skipping the header row
    for row in data[1:]:  # Get the count of the number of vehicles passing on a day
        count += 1
        if row[-2] == "Truck":  # Get the count of the number of truck passing on a day
            truck += 1
        if row[-1].lower() == "true":  # Get the count of the number of electric vehicles passing on a day
            electric += 1
        if row[-2] == "Bicycle" or row[-2] == "Motorcycle" or row[-2] == "Scooter":  # Get the count of the number of two-wheeled vehicles passing on a day
            two_wheel += 1
        if row[0] == "Elm Avenue/Rabbit Road" and row[4] == "N" and row[-2] == "Buss":  # Get the count of the number of Busses leaving Elm Avenue/Rabbit Road heading North on a day
            bus += 1
        if row[3] == row[4]:  # Get the count of the number of Vehicles go through both junctions not turning left or right on a day
            forword += 1
        if row[-2] == "Bicycle":  # Get the average number of Bikes per hour on a day
            bike += 1
        if int(row[6]) < int(row[-3]):  # Get the count of the Vehicles recorded as over the speed limit on a day
            speed += 1
        if row[0] == "Elm Avenue/Rabbit Road":  # Get the count of the vehicles recorded through Elm Avenue/Rabbit Road junction on a day
            elm_road += 1
        if row[0] == "Hanley Highway/Westway":  # Get the count of the vehicles recorded through Hanley Highway/Westway junction on a day
            han_road += 1
        if row[0] == "Elm Avenue/Rabbit Road" and row[-2] == "Scooter":  # Get the percentage of scooters on a day
            scooter += 1
        if row[0] == "Hanley Highway/Westway":  # Get the count of the highest number of vehicles in an hour on Hanley Highway/Westway on a day
            hour = row[2].split(":")[0]
            if hour not in vehicles_hour:
                vehicles_hour[hour] = 0
            vehicles_hour[hour] += 1
        if row[5].lower() == "heavy rain" or row[5].lower() == "light rain":  # Get the count of the number of hours of rain on a day
            rain = row[2].split(":")[0]
            rain_hour.add(rain)
        if row[0] == "Elm Avenue/Rabbit Road":  # Get the number of vehicles passing through Elm Avenue/Rabbit Road junction on a day
            travel_hour = row[2].split(":")[0]
            if travel_hour not in elm_vehicles_per_hour:
                elm_vehicles_per_hour[travel_hour] = 0
            elm_vehicles_per_hour[travel_hour] += 1
        elif row[0] == "Hanley Highway/Westway":  # Get the number of vehicles passing through Hanley Highway/Westway junction on a day
            travel_hour = row[2].split(":")[0]
            if travel_hour not in han_vehicles_per_hour:
                han_vehicles_per_hour[travel_hour] = 0
            han_vehicles_per_hour[travel_hour] += 1

    # appending the values on dictionary to a list
    elm_vehicles = list(elm_vehicles_per_hour.values())
    han_vehicles = list(han_vehicles_per_hour.values())

    # creating a final list with all data of vehicles passing through both the junctions
    final_list_of_vehicale = [elm_vehicles, han_vehicles]

    if count > 0:  # Get the percentage of trucks on a day
        truck_percentage = round((truck / count) * 100)
    else:
        truck_percentage = 0

    highest = max(vehicles_hour.values())

    for key,value in (vehicles_hour.items()):  # Get the exact hour range of the highest number of vehicles in an hour on Hanley Highway/Westway on a day
        if value == highest:
            s_hour = int(key)

    avg_bike = bike // 24
    avg_scooter = int((scooter / elm_road) * 100)
    total_rain = len(rain_hour)

    # Prepare the final dictionary with all outputs providing sutible key and value
    final = {
        "vehicle": count,"trucks": truck,"electric": electric,"two-wheel": two_wheel,"bus": bus,"both_junctions": forword,"percentage": truck_percentage,"bike": avg_bike,
        "over_speed": speed,"Elm Avenue/Rabbit": elm_road,"Highway/Westway": han_road,"scooter": avg_scooter,"highest": highest,"most_vehicles": s_hour,"rain": total_rain,}

    # Close the file after processing
    file.close()

    return final, final_list_of_vehicale


def display_outcomes(outcomes):  # print all the data into expected outputs.
    print(f'The total number of vehicles recorded for this date is {outcomes["vehicle"]}')
    print(f'The total number of trucks recorded for this date is {outcomes["trucks"]}')
    print(f'The total number of electric vehicles for this date is {outcomes["electric"]}')
    print(f'The total number of two wheel vehicles for this date is {outcomes["two-wheel"]}')
    print(f'The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes["bus"]}')
    print(f'The total number of vehicles through both junctions not turning left or right is {outcomes["both_junctions"]}')
    print(f'The percentage of total vehicles recorded that are trucks for this date is {outcomes["percentage"]}%.')
    print(f'The average number of bikes per hour for this date is {outcomes["bike"]}\n ')
    print(f'The total number of vehicles recorded as over the speed limit for this date is {outcomes["over_speed"]}')
    print(f'The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes["Elm Avenue/Rabbit"]}')
    print(f'The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes["Highway/Westway"]}')
    print(f'{outcomes["scooter"]}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n')
    print(f'The highest number of vehicles in an hour on Henley Highway/Westway is {outcomes["highest"]}')
    print(f'The most vehicles through Henley/Westway were recorded between {outcomes["most_vehicles"]}:00 and {outcomes["most_vehicles"]+1}:00. ')
    print(f'The number of hours of rain for this day is {outcomes["rain"]}')


# Task C: Save Results to Text File
def save_results_to_file(
    outcomes, fname, txtfile_name="results.txt"):  # Open the file in append mode ("a")
    with open(txtfile_name, "a") as file:  # write all the data into the file
        file.write(f"data file selected is,{fname}\n")
        file.write(f'The total number of vehicles recorded for this date is {outcomes["vehicle"]}\n')
        file.write(f'The total number of trucks recorded for this date is {outcomes["trucks"]}\n')
        file.write(f'The total number of electric vehicles for this date is {outcomes["electric"]}\n')
        file.write(f'The total number of two wheel vehicles for this date is {outcomes["two-wheel"]}\n')
        file.write(f'The total number of busses leaving Elm Avenue/Rabbit Road heading North is {outcomes["bus"]}\n')
        file.write(f'The total number of vehicles through both junctions not turning left or right is {outcomes["both_junctions"]}\n')
        file.write(f'The percentage of total vehicles recorded that are trucks for this date is {outcomes["percentage"]}%.\n')
        file.write(f'The average number of bikes per hour for this date is {outcomes["bike"]}\n ')
        file.write(f'The total number of vehicles recorded as over the speed limit for this date is {outcomes["over_speed"]}\n')
        file.write(f'The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {outcomes["Elm Avenue/Rabbit"]}\n')
        file.write(f'The total number of vehicles recorded through Hanley Highway/Westway junction is {outcomes["Highway/Westway"]}\n')
        file.write(f'{outcomes["scooter"]}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n')
        file.write(f'The highest number of vehicles in an hour on Henley Highway/Westway is {outcomes["highest"]}\n')
        file.write(f'The most vehicles through Henley/Westway were recorded between {outcomes["most_vehicles"]}:00 and {outcomes["most_vehicles"]+1}:00.\n')
        file.write(f'The number of hours of rain for this day is {outcomes["rain"]}\n')
        file.write(f"\n")
        file.write(f"***************************\n")
        file.write(f"\n")


def main():
    while True:  # Start a loop to repeatedly do task until it get stopped by the user.
        file_name, histrogram_date = validate_date_input()
        try:
            final_output, histrogram_data = process_csv_data(file_name)
            display_outcomes(final_output)
            save_results_to_file(final_output, file_name, txtfile_name="results.txt")

        except FileNotFoundError:  # Handling error that could happen when the specified file cannot be found
            print(f"Error: File '{file_name}' not found.")

        except IndexError:  # Handling error that could happen there is no data inside the file
            print(f"File {file_name} is empty.")

        condition = validate_continue_input()

        if condition == "N":  # If the user chooses "N" the process stops and exit the loop.
            print("\nTerminating the process...........")
            break
        else:  # If the user wish to continue, print a message and repeat the process.
            print("\nInitializing a new data collection...........")


if __name__ == "__main__":
    main()
