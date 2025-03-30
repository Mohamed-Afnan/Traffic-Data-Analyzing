# Task D: Histogram Display
from graphics import GraphWin, Rectangle, Text, Point, Line #Importing graphic into the code
from w2120190_ABC import validate_date_input, validate_continue_input, process_csv_data, display_outcomes,save_results_to_file  # Importing the functions from the ABC python file

class HistogramApp:
    def __init__(self, traffic_data, date): #Initialize the HistogramApp with hourly vehicles data and the specific date.
        self.traffic_data = traffic_data
        self.date = date

    def setup_window(self): #Set up the window and the background colour of the window with the name
        self.window = GraphWin("Histogram", width=1400, height=600)
        self.window.setBackground("#FAF9F6")

    def draw_histogram(self):
        # Finding the maximum value on both datasets
        elm_max = max(self.traffic_data[0])
        han_max = max(self.traffic_data[1])
        both_max = max(elm_max,han_max)
        elm = self.traffic_data[0]
        elm_extender = 100 #First bar starting point

        for elm_hour_data in elm: # Drawing the bars for Elm Avenue/Rabbit Road
            hour_elm = Rectangle(Point(elm_extender,(530-((elm_hour_data/both_max)*320))),Point(elm_extender+20,530))
            hour_elm.setFill("#4bda4b")
            hour_elm.setOutline("grey")
            hour_elm.draw(self.window)
            
            # Display the value of vehicales above the bar
            value_elm = Text(Point(elm_extender+10,(530-(((elm_hour_data/both_max)*320)+8))), elm_hour_data)
            value_elm.setFace("times roman")
            value_elm.setStyle("bold")
            value_elm.setTextColor("#4bda4b")
            value_elm.setSize(9)
            value_elm.draw(self.window)
            
            elm_extender += 50 # Increment the x-coordinate for next bar to draw with spacified gap

        han = self.traffic_data[1]
        han_extender = 120 #first bar starting point
        
        for han_hour_data in han: # Drawing the bars for Hanley Highway/Westway
            hour_han = Rectangle(Point(han_extender,(530-((han_hour_data/both_max)*320))),Point(han_extender+20,530))
            hour_han.setFill("#fc9296")
            hour_han.setOutline("grey")
            hour_han.draw(self.window)
            
            # Display the value of vehicales above the bar
            value_elm = Text(Point(han_extender+10,(530-(((han_hour_data/both_max)*320)+8))), han_hour_data)
            value_elm.setFace("times roman")
            value_elm.setStyle("bold")
            value_elm.setTextColor("#fc9296")
            value_elm.setSize(9)
            value_elm.draw(self.window)
            
            han_extender += 50 # Increment the x-coordinate for next bar to draw with spacified gap

         # Drawing the x-axis label bellow the histogram 
        axis_text = Text(Point(700,565), "Hours 00:00 to 24:00")
        axis_text.setFace("times roman")
        axis_text.setStyle("bold")
        axis_text.setTextColor("grey")
        axis_text.setSize(11)
        axis_text.draw(self.window)

        # Drawing the x-axis line
        lower_line = Line(Point(100,530),Point(1290,530))
        lower_line.draw(self.window)

        # Adding the hour below the x-axis line
        line_value = 120
        for hours in range (0,24):
            hours = f"{hours:02}"
            hour_num = Text(Point(line_value,538), hours)
            hour_num.setFace("times roman")
            hour_num.setStyle("bold")
            hour_num.setTextColor("black")
            hour_num.setSize(8)
            hour_num.draw(self.window)
            line_value += 50 # Increment the x-coordinate for next bar to draw with spacified gap
            
    def add_legend(self):
        # Adding the topic and date of the graph displayied 
        header_details = Text(Point(366,38), f" Histogram of Vehicle Frequency per Hour ({self.date})")
        header_details.setFace("times roman")
        header_details.setStyle("bold")
        header_details.setTextColor("grey")
        header_details.setSize(16)
        header_details.draw(self.window)

        # Creating Legend for Elm Avenue/Rabbit Road and naming it
        square_1 = Rectangle(Point(100,60),Point(120,80))
        square_1.setFill("#4bda4b")
        square_1.setOutline("grey")
        square_1.draw(self.window)
        road_name_1 = Text(Point(214,70), "Elm Avenue/Rabbit Road")
        road_name_1.setFace("times roman")
        road_name_1.setStyle("bold")
        road_name_1.setTextColor("grey")
        road_name_1.setSize(11)
        road_name_1.draw(self.window)

        # Creating Legend for Hanley Highway/Westway and naming it
        square_2 = Rectangle(Point(100,90),Point(120,110))
        square_2.setFill("#fc9296")
        square_2.setOutline("grey")
        square_2.draw(self.window)
        road_name_2 = Text(Point(216,102), "Hanley Highway/Westway")
        road_name_2.setFace("times roman")
        road_name_2.setStyle("bold")
        road_name_2.setTextColor("grey")
        road_name_2.setSize(11)
        road_name_2.draw(self.window)
        
    def run(self):
        self.setup_window() # Creating a canvas
        self.draw_histogram() # Drawing the histrogram
        self.add_legend() # Adding the title and legends with their
        self.window.getMouse() # Waiting until for a mouse click to close the histrogram
        self.window.close() # Closing the window


# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor: 
    def __init__(self): #Initialize the MultiCSVProcessor with histrogram data, histrogram date, outcomes
        self.histogram_date = None 
        self.histogram_data = None
        self.outcomes = None

    def load_csv_file(self, file_path): #Load the csv file to process the data and to get the outcomes and histogram data
        self.outcomes , self.histogram_data = process_csv_data(file_path) 

    def clear_previous_data(self): #Clear the previous data to avoid on the code for avoid re-usage of the previous data
        self.histogram_date = None
        self.histogram_data = None
        self.outcomes = None

    def handle_user_interaction(self): #Handle the user interaction to continue or terminate the process
        while True:
            try:
                self.clear_previous_data() # Clear the previous data
                self.name , self.histogram_date = validate_date_input() 
                self.load_csv_file(self.name)
                display_outcomes(self.outcomes)
                save_results_to_file(self.outcomes , self.name , txtfile_name="results.txt")
                histrogram = HistogramApp(self.histogram_data, self.histogram_date) # Display the histogram
                histrogram.run() # Run the histogram
                break
            except FileNotFoundError:  
                print(f"Error: File '{self.name}' not found.") # Display an error message if the file is not found
                break 
            except IndexError:
                print(f"File {self.name} is empty.")
                break

    def process_files(self): #Process the files and display the outcomes on a histogram
        while True:
            self.handle_user_interaction() # Handle the user interaction to continue or terminate the code
            self.statement = validate_continue_input() 
            if self.statement.upper() == "N": # If the user chooses "N" the process stops and exit the loop.
                print("\nTerminating the process...........")
                break
            else: # If the user wish to continue, print a message and repeat the process.
                print("\nInitializing a new data collection...........")

MultiCSVProcessor().process_files()
