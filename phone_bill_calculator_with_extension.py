base_plan_cost = input("Enter Base Plan Cost")
base_plan_time = input("Enter Base Plan Time")
state_tax = input("Enter Tax")
overage_minute_cost = input("Enter Overage Minute Cost")



base_minute_cost = (float(base_plan_cost) / float(base_plan_time))
tax_size = float(state_tax) /(float(base_plan_cost) / 100)
base_plan_cost_total = (float(base_plan_cost) + ((float(base_plan_cost) / 100) * float(tax_size)))



def phone_bill_cost(used_minutes):
    if used_minutes > 0 and used_minutes <= 100:
        bill_withot_tax = float(used_minutes * base_minute_cost)
        tax = float(bill_withot_tax / 100 * tax_size)
        bill_total = float(bill_withot_tax + tax)

        return round(bill_withot_tax, 2), round(tax, 2), round(bill_total, 2)

    elif used_minutes <= 0:
        bill_without_tax = 0
        tax = 0
        bill_total = 0
        return bill_without_tax, tax, bill_total

    elif used_minutes > 100:
        bill_without_tax = float(base_plan_cost + (used_minutes - base_plan_time) * overage_minute_cost)
        tax = float(bill_without_tax / 100 * tax_size)
        bill_total = float(bill_without_tax + tax)
        return round(bill_without_tax, 2), round(tax, 2), round(bill_total, 2)


print(phone_bill_cost(80))
