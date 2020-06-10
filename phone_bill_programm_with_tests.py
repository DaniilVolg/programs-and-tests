
# Enter base cost of the plan:82.45
# Enter overage minutes: 9
# Phone Bill Statement
# Plan: $82.45
# Overage: $2.25
# Tax: $12.71
# Total: $97.41

base_plan_cost = 82.45
base_plan_time = 100
base_minite_cost = float(base_plan_cost / base_plan_time)
overage_minute_cost = 2.25
tax_size = float(12.71 / (base_plan_cost / 100))
base_plan_cost_total = float(base_plan_cost + (base_plan_cost / 100 * tax_size))


# print(BASE_PLAN_COST_TOTAL)
def phone_bill_cost(used_minutes):
    if used_minutes > 0 and used_minutes <= 100:
        bill_withot_tax = used_minutes * base_minite_cost
        tax = bill_withot_tax / 100 * tax_size
        bill_total = bill_withot_tax + tax

        return round(bill_withot_tax, 2), round(tax, 2), round(bill_total, 2)

    elif used_minutes <= 0:
        bill_without_tax = 0
        tax = 0
        bill_total = 0
        return bill_without_tax, tax, bill_total

    elif used_minutes > 100:
        bill_without_tax = base_plan_cost + ((used_minutes - base_plan_time) * 2.25)
        tax = bill_without_tax / 100 * tax_size
        bill_total = bill_without_tax + tax
        return round(bill_without_tax, 2), round(tax, 2), round(bill_total, 2)


# print(phone_bill_cost(float(150)))


def test_phone_bill_positive():
    actual_data = phone_bill_cost(65)
    expected_data = (53.59, 8.26, 61.85)
    assert actual_data == expected_data


def test_phone_bill_negative():
    actual_data = phone_bill_cost(0)
    expected_data = (0, 0, 0)
    assert actual_data == expected_data


def test_phone_bill_overage_minutes():
    actual_data = phone_bill_cost(110)
    expected_data = (104.95, 16.18, 121.13)
    assert actual_data == expected_data
