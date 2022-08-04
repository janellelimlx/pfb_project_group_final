from pathlib import Path
def overhead_function(forex):
# def overhead_function(forex) to create a function so that it can be imported to main 
    overheads_csv = []
    highest_percentage = []
    highest_expense = []
    home = Path.cwd()
    file_path = home/"csv_reports"/"Overheads.csv"
    file_path.touch
    with file_path.open(mode="r", encoding ="UTF-8")as file:
        for row in file.readlines():
        # read the overheads.csv to extract the data 
            overhead_strip = row.strip().split(",")
            # .strip().split(",") is used to remove the \n from the code
            overheads_csv.append(overhead_strip)
            # the data extracted from overheads csv is appended to the empty list
    number = 1 
    # since the data that is needed does not include the header, number = 1
    while number < len(overheads_csv):
        overheads = overheads_csv[number]
        # while loop is created where the code will run when the number is less than the length of overheads_csv
        # indexing of [0:2] is used to find the expense and amount
        expense = overheads[0:2]
        expense_percentage = overheads[1]
        # indexing of [1] is used to find the amount for each expense
        highest_percentage.append(float(expense_percentage))
        highest_expense.append(expense)
        number += 1
        # number number += 1 continues the loop
    file.close
    max_percent = max(highest_percentage)
    index = highest_percentage.index(max_percent)
    # .index() is used to seperate the values in max_percent
    overheads_expense = highest_expense[index][0]
    overheads_expense_amount = highest_expense[index][1]
    print(overheads_expense)
    print(overheads_expense_amount)
    overheads_expense_amount_sgd = float(overheads_expense_amount)*float(forex)
    # this would convert the value from USD to SGD
    file_write_path = home/"summary_report.txt"
    file_write_path.touch
    with file_write_path.open(mode="a", encoding ="UTF-8", newline="")as file_write:
    # the data extracted is appeded to the summary_report.txt file    
        rounded_off_value = round(overheads_expense_amount_sgd, 2)
        # the value is then rounded off to 2 decimal place
        file_write.write(f"[HIGHEST OVERHEADS] {overheads_expense} : SGD{str(rounded_off_value)}\n")
    file_write.close
    return None

