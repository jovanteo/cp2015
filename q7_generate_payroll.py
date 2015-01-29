#Sample input:
#
#Enter name: Lim Ah Seng
#Enter number of hours worked weekly: 10
#Enter hourly pay rate: 6.75
#Enter CPF contribution rate(%): 20
#
#Sample output:
#
#Payroll statement for Lim Ah Seng
#Number of hours worked in week: 10
#Hourly pay rate: $6.75
#Gross pay = $67.50
#CPF contribution at 20% = $13.50
#Net pay = $54.00

name = input("Input Name")
hour = input("Input hours worked?")
pay = input ("Input pay?")
CPF = input ("Input CPF contribution(%)")
gross = float(pay)*float(hour)
CPFcon = float(CPF)/100 * gross

print("\nPayroll statement for Mr/Mdm", name,\
      "\nNumber of hours worked in a week", hour,\
      "\nHourly pay rate: $", pay,\
      "\nGross pay = $", gross,\
      "\nCPF contribution at", CPF, "% =", CPFcon,\
      "\nNet pay =", gross-CPFcon)
