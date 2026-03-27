import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# importing my package
from package import dfmath, displaydata, charts

def safe_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("numbers only please.")

def safe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("numbers only please.")

class BtcTracker:
    def __init__(self):
        self.filename = ""
        self.mydata = None
        self.reportfile = "Prediction_Report.txt"

    def check_data(self):
        if self.mydata is None:
            print("no data found!")
            return False
        return True

    def load_csv(self, file_name):
        try:
            self.filename = file_name
            cols = ["Date", "Close", "High", "Low", "Open", "Volume"]
            # If the file doesn't exist, pandas will throw an error and skip to the except block
            self.mydata = pd.read_csv(self.filename, skiprows=3, names=cols)
            self.mydata['Date'] = pd.to_datetime(self.mydata['Date'])
            print("loaded successfully")
        except FileNotFoundError:
            print("error: file not found")
            self.mydata = None

    def add_data_menu(self):
        if not self.check_data():
            return
            
        d = input("enter date (YYYY-MM-DD) or press enter for today: ")
        if not d:
            d = datetime.now().strftime('%Y-%m-%d')
            
        c = safe_float("close price: ")
        h = safe_float("high price: ")
        l = safe_float("low price: ")
        o = safe_float("open price: ")
        v = safe_int("volume: ")
        
        with open(self.filename, mode='a') as myfile:
            myfile.write(f"\n{d},{c},{h},{l},{o},{v}")
            
        cols = ["Date", "Close", "High", "Low", "Open", "Volume"]
        self.mydata = pd.read_csv(self.filename, skiprows=3, names=cols)
        self.mydata['Date'] = pd.to_datetime(self.mydata['Date'])
        print("data saved")

    def explore_menu(self):
        if not self.check_data():
            return
            
        print("""
1. top rows
2. bottom rows
3. random rows
4. columns
5. data types""")
        
        sub_c = safe_int("choice: ")

        match sub_c:
            case 1:
                displaydata.toprow(self.mydata, 5)
            case 2:
                displaydata.botrow(self.mydata, 5)
            case 3:
                displaydata.randomrows(self.mydata, 5)
            case 4:
                displaydata.colnames(self.mydata)
            case 5:
                displaydata.datatypes(self.mydata)
            case _:
                print("invalid option")

    def show_stats(self):
        if not self.check_data():
            return
            
        print(f"highest: {dfmath.maxval(self.mydata, 'High')}")
        print(f"lowest: {dfmath.minval(self.mydata, 'Low')}")
        print(f"average: {dfmath.colavg(self.mydata, 'Close')}")
        print(f"total vol: {dfmath.colsum(self.mydata, 'Volume')}")
        print(f"std dev: {dfmath.getstd(self.mydata, 'Close')}")

    def filter_price(self, threshold):
        if not self.check_data():
            return
            
        filtered = self.mydata[self.mydata['Close'] >= threshold]
        print(f"found {len(filtered)} days")
        if len(filtered) > 0:
            displaydata.toprow(filtered, 5)

    def predict(self):
        if not self.check_data():
            return

        avg = dfmath.colavg(self.mydata, 'Close')
        curr = self.mydata.iloc[-1]['Close']
        
        if curr > avg:
            result = "buy (going up)"
        else:
            result = "sell (going down)"
            
        print(f"prediction: {result}")
        
        today_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(self.reportfile, "a") as f:
                f.write(f"[{today_time}] avg: {avg}, current: {curr}, predict: {result}\n")
        except Exception:
            print("error writing to file")

    def view_history(self):
        try:
            with open(self.reportfile, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("no history found")

    def chart_menu(self):
# menu to pick which chart to show
        if not self.check_data():
            return
            
        print("""
1. line chart
2. bar chart
3. scatter plot
4. histogram""")
        
        c_num = safe_int("chart choice: ")

        match c_num:
            case 1:
                charts.linechart(self.mydata, 'Date', 'Close')
            case 2:
                recent = self.mydata.tail(30)
                charts.barchart(recent, 'Date', 'Open')
            case 3:
                charts.scatterplot(self.mydata, 'Volume', 'Close')
            case 4:
                charts.dohistogram(self.mydata, 'Close')
            case _:
                print("bad choice")
                return
        plt.show()

if __name__ == "__main__":
    app = BtcTracker()
    
    while True:
        print("""
===========================
BTC PREDICTION TRACKER
===========================
1. Load dataset
2. Add new daily data
3. Explore data
4. View stats
5. Filter by price
6. Predict trend
7. View history
8. Charts
9. Exit""")
        
        main_choice = safe_int("Please select an option: ")

        match main_choice:
            case 1:
                fname = input("enter file name: ")
                app.load_csv(fname)

            case 2:
                app.add_data_menu()

            case 3:
                app.explore_menu()

            case 4:
                app.show_stats()

            case 5:
                min_p = safe_float("minimum price: ")
                app.filter_price(min_p)

            case 6:
                app.predict()

            case 7:
                app.view_history()

            case 8:
                app.chart_menu()

            case 9:
                print("goodbye")
                break
                
            case _:
                print("invalid choice")

