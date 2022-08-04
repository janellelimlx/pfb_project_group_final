import api,overheads,cash_on_hand,profit_loss
# main.py will import each python file as modules
def main():
    forex = api.api_function()
    overheads.overhead_function(forex)
    # by using overhead_function(forex) the exchange rate will be imported to overheads so that the amount can be converted from USD to SGD.
    cash_on_hand.coh_function(forex)
    profit_loss.profitloss_function(forex)
main()
# the main.py will coordinate all the files so functions are executed in just one file (main.py)
