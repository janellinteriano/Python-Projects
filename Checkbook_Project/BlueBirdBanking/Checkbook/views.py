from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# Create your views here.

# this function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)  # retrieves transaction form
    # checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieves which account the user wants to view
        return balance(request, pk)  # call balance function to render that account's balance sheet
    content = {'form': form}  # passes content to the template as dictionary
    # adds content of form to page
    return render(request, 'checkbook/index.html', content)


# this function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieves the Account form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # checks to see if the submitted form is valid and if so, saves the form
            form.save()  # saves new account
            return redirect('index')  # returns user back to the home page
    content = {'form': form}  # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)


# this function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieves requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk)  # retrieves all of that account's transactions
    current_total = account.initial_deposit  # creates account total variable, starting with initial deposit value
    table_contents = {}  # creates a dictionary into which transaction information will be placed
    for t in transactions:   # loop through transactions and determines which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount  # if deposit add amount to balance
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtract amount from balance
            table_contents.update({t: current_total})  # add transaction and total to the dictionary
    # pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the Transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)  # retrieves the Transaction form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # checks to see if the submitted form is valid and if so, saves the form
            pk = request.POST['account']  # retrieves which account the transaction was for
            form.save()  # saves transaction form
            return balance(request, pk)  # renders balance of the accounts balance sheet
    # passes content to the template as a dictionary
    content = {'form': form}
    # adds content of form to page
    return render(request, 'checkbook/AddTransaction.html', content)



