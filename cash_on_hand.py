from pathlib import Path
def coh_function(forex):
# def coh_function(forex) to create a function so that it can be imported to main 
    cash_on_hand_csv = []
    # ann empty list is created
    home = Path.cwd()
    file_path = home/"csv_reports"/"Cash on hand.csv"
    file_path.touch
    with file_path.open(mode="r", encoding ="UTF-8")as file:
        for row in file.readlines():
          # read the cash on hand.csv to extract the data               
          cash_on_hand_split = row.strip().split(",")
          # .strip().split(",") is used to remove the \n from the code
          cash_on_hand_csv.append(cash_on_hand_split)
          # the data extracted from cash on hand csv is appended to the empty list
    file_write_path = home/"summary_report.txt"
    file_write_path.touch
    with file_write_path.open(mode="a", encoding ="UTF-8", newline="")as file_write:
      # the data extracted is appended to the summary_report.txt file
      days_cash = 0
      number = 1
      # since the data that is needed does not include the header, number = 1
      while number < len(cash_on_hand_csv):
        cash_on_hand = cash_on_hand_csv[number]
        today_cash = float(cash_on_hand[1])
        day = cash_on_hand[0]
        # while loop is created where the code will run when the number is less than the length of cash_on_hand_csv
        # indexing of [1] and [0] is used to find the amount and day respectively
        if number == 1:
          prev_day = today_cash
        else:
          deficit = round(float(prev_day - today_cash) * float(forex),2)
          # since prev_day is not equals to today_cash, deficit is calculated
          # the difference between the previous day cash on hand the the current day cash on hand is calculated
          # it is rounded off to 2 decimals place
          if deficit > 0: 
            print(f"[CASH DEFICIT] Day: {day}, Amount = SGD{deficit}")
            file_write.write(f"[CASH DEFICIT] Day: {day}, Amount = SGD{str(deficit)}\n")
            # if the defict value is negetive, it will print f"[CASH DEFICIT] Day: {day}, Amount = SGD{str(deficit)}
          else:        
            days_cash += 1
            # else the loop will continue to the next day
        number += 1
        prev_day = today_cash
      file.close()
      if days_cash == (len(cash_on_hand_csv) - 2):    
          print(f"[CASH SURPLUS] net on each day is higher than the previous day")
          file_write.write(f"[CASH SURPLUS] net on each day is higher than the previous day\n")
          # if cash on hand each day is higher than the previous day, it will print [CASH SURPLUS] net on each day is higher than the previous day
      file_write.close
    return None






    