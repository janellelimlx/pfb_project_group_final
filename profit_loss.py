from pathlib import Path
def profitloss_function(forex):
# define profitloss_function(forex) to create a function so that it can be imported to main
    profit_and_loss_csv = []
# an empty list is created
    home = Path.cwd()
    file_path = home/"csv_reports"/"Profit and loss.csv"
    file_path.touch
    with file_path.open(mode="r", encoding ="UTF-8")as file:
        for row in file.readlines():
            # read the profit and loss csv to extract the data
            profit_and_loss_split = row.strip().split(",")
            # .strip().split(",") is used to remove the \n from the code
            profit_and_loss_csv.append(profit_and_loss_split)
            # the data extracted from profit and loss csv is appended to an empty list
    days_profit = 0
    number = 1
    # since the data that is needed does not include the header, number = 1
    file_write_path = home/"summary_report.txt"
    file_write_path.touch
    with file_write_path.open(mode="a", encoding ="UTF-8", newline="")as file_write:
        # the data extracted is appended to the summary_report.txt file
        while number < len(profit_and_loss_csv):
            net_profit = profit_and_loss_csv[number]
            # while loop is created where the code will run when the number is less than the length of profit_and_loss_csv
            today_profit = float(net_profit[4])
            # indexing [4] is used to get the net profit
            day = net_profit[0]
            # indexing [0] is used to get the day
            if number == 1:
                prev_profit = today_profit
            else:
                deficit = round(float(prev_profit - today_profit)*float(forex),2)
                # since prev_day is not equals to today_cash, deficit is calculated
                # the difference between the previous day profit the the current day profit is calculated
                # it is rounded off to 2 decimals place
                if deficit > 0:
                    print(f"[PROFIT DEFICIT] Day: {day}, Amount : SGD{deficit}\n")   
                    file_write.write(f"[PROFIT DEFICIT] Day: {day}, Amount = SGD{str(deficit)}\n")
                    # if the defict value is negetive, it will print f"[CASH DEFICIT] Day: {day}, Amount = SGD{str(deficit)}     
                else:        
                    days_profit += 1
            number +=1
            prev_profit = today_profit
        file.close()
        if days_profit == (len(profit_and_loss_csv) - 2):    
            print(f"[NET PROFIT SURPLUS] net profit on each day is higher than the previous day\n")
            file_write.write(f"[NET PROFIT SURPLUS] net profit on each day is higher than the previous day\n")
        file_write.close
    return None  





    

    
