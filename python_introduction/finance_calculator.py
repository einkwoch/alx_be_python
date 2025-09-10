monthlyIncome = int(input("Enter your monthly income:"))
monthlyExpense = int(input("Enter your monthly Expense:"))
annualIntrest = 0.05

monthlySavings = monthlyIncome - monthlyExpense

projectedSavings = monthlySavings * 12 + (monthlySavings * 12 * annualIntrest)

print(f"Your monthly savings are ${monthlySavings}.")
print(f"Projected savings after one year, with interest, is: ${projectedSavings}.")