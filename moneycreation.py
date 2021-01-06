def money_created(deposit, reserve_requirement):
  #reserve_requirement as a decimal, i.e. 10% = .10
  #deposit as a dollar amount, i.e. $10,000 = 10000
  if reserve_requirement < 0:
    print('A negative reserve requirement does not exist therefore this program QUITS when a negative value is entered for reserve_requirement!')
    quit()
  if reserve_requirement == 0:
    print('A Reserve Requirement of Zero allows the initial deposit amount to be re-loaned and re-deposited, theoretically, ad infinitum!')
    print("Becuase a zero value for reserve requirement has a potentially infinite use, this program QUITS on a zero value for reserve_requirement.")
    quit()
  if reserve_requirement >= 1:
    print('A Reserve Requirement of 100% does not allow a bank to make a loan on the initial deposit.')
    print("Therefore a reserve_requirement value of 1 or greater QUITS this program.")
    quit()
  num_deposits = 1
  first_loan = 0
  second_loan = 0
  current_loan = 0
  total_loans = 0
  total_funds_held = 0
  most = deposit * 10
  
  while (total_loans + total_funds_held) <= (deposit / reserve_requirement):
      if num_deposits == 1:
        funds_held = deposit * reserve_requirement
        first_loan = deposit - funds_held
        total_funds_held += funds_held
        total_loans += first_loan
        num_deposits += 1
        # print('initial deposit:', deposit, 'first loan:', first_loan, 'total_funds_held:', total_funds_held, 'total loans:', total_loans)

      elif num_deposits == 2:
        second_deposit = first_loan
        funds_held = second_deposit * reserve_requirement
        second_loan = second_deposit - funds_held
        total_funds_held += funds_held
        total_loans += second_loan
        num_deposits += 1
        # print('second deposit', second_deposit, 'second loan', second_loan, 'total funds held', total_funds_held, 'total loans', total_loans)

      elif num_deposits == 3:
        current_deposit = second_loan
        funds_held = current_deposit * reserve_requirement
        current_loan = current_deposit - funds_held
        total_funds_held += funds_held
        total_loans += current_loan
        num_deposits += 1
        # print('current deposit', current_deposit, 'current loan:', current_loan, 'total funds held', total_funds_held, 'total_loans', total_loans)

      elif num_deposits > 3 and num_deposits < most:
        current_deposit = current_loan
        funds_held = current_deposit * reserve_requirement
        current_loan = current_deposit - funds_held
        total_funds_held += funds_held
        total_loans += current_loan
        num_deposits += 1
        # print('current deposit', current_deposit, 'current loan:', current_loan, 'total funds held', total_funds_held, 'total_loans', total_loans)
      
      else:
        break
  # print('Total Loans:', total_loans, 'Total Funds Held:', total_funds_held)
  a = round(total_loans, 2)
  b = round(total_funds_held, 2)
  print(f"An initial deposit of ${deposit} with a reserve requirement of {reserve_requirement*100}% creates total bank loans in the amount of ${a} with the bank holding an amount of ${b} in reserve funds.")
  
  # print('Total Loans:', a)
  # print('Total Funds Held:', b)
    
      



money_created(10000, .15)
#I have stops if the user enters 0 or less and 1 or greater as the reserve_requirement value. Is there a more effective way to do this?