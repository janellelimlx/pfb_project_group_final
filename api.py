import requests
from pathlib import Path
def api_function():
    try:
        # use def_function() to create a function so that it can be imported to main.py
        # use try block to run code to check if there are any mistakes
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=AHG5471DOI5DF9TF"
        response = requests.get(url)
        data = response.json()
        # retrieve data with .json()
        exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        # using ['Realtime Currency Exchange Rate']['5. Exchange Rate'] will extract the exchange rate from data
        print(exchange_rate)
    except IOError:
        # the except block allows to handle the error that may occur if the api website is down
        return "file not found"
    else:
        # else finally executes the code ensuring that the program does not crash
        home = Path.cwd()
        file_path = home/"summary_report.txt"
        # create a text file, summary_report.txt
        file_path.touch
        with file_path.open(mode="w", encoding ="UTF-8", newline="")as file_write:
            file_write.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{exchange_rate}\n")
# write the data extracted (exchange rate) to the summary_report.txt file
# formatted string is used.  
        file_write.close
        return exchange_rate  
