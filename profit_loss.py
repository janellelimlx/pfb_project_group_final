from pathlib import Path
def profitloss_function(forex):
    profit_and_loss_csv = []
    home = Path.cwd()
    file_path = home/"csv_reports"/"Profit and loss.csv"
    file_path.touch
    with file_path.open(mode="r", encoding ="UTF-8")as file:
        for row in file.readlines():
            profit_and_loss_split = row.strip().split(",")
            profit_and_loss_csv.append(profit_and_loss_split)
    days_profit = 0
    number = 1
    file_write_path = home/"summary_report.txt"
    file_write_path.touch
    with file_write_path.open(mode="a", encoding ="UTF-8", newline="")as file_write:
        while number < len(profit_and_loss_csv):
            net_profit = profit_and_loss_csv[number]
            today_profit = float(net_profit[4])
            day = net_profit[0]
            if number == 1:
                prev_profit = today_profit
            else:
                deficit = round(float(prev_profit - today_profit)*float(forex),2)
                if deficit > 1:
                    print(f"[PROFIT DEFICIT] Day: {day}, Amount : SGD{deficit}\n")   
                    file_write.write(f"[PROFIT DEFICIT] Day: {day}, Amount = SGD{str(deficit)}\n")     
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





    

    
