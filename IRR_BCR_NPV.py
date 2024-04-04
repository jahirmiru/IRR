import numpy as np
import numpy_financial as npf

def calculate_financial_metrics(duration, expenditures, benefits, discount_rate):
    """
    Calculates the IRR, BCR, NPV, discounted expenditures, discounted benefits,
    net income for each year, and total discounted expenditure and discounted benefits.

    Args:
        duration (int): The project duration in years.
        expenditures (list): A list of expenditures for each year.
        benefits (list): A list of benefits for each year.
        discount_rate (float): The discount rate as a percentage.

    Returns:
        tuple: (irr, bcr, npv, discounted_expenditures, discounted_benefits, net_incomes, total_discounted_expenditure, total_discounted_benefits)
        or None if calculation fails
    """

    # Input validation
    if duration <= 0:
        print("Error: Project duration must be greater than zero.")
        return None
    if len(expenditures) != duration or len(benefits) != duration:
        print("Error: Expenditures and benefits lists must match the project duration.")
        return None
    if discount_rate < 0:
        print("Error: Discount rate cannot be negative.")
        return None

    # Convert discount rate to decimal
    discount_rate /= 100 

    # Calculate cash flows (expenditures as negative values)
    cash_flows = [-expenditures[0]]  # Initial investment
    for i in range(1, duration):
        cash_flows.append(benefits[i] - expenditures[i])

    # Attempt to calculate IRR
    try:
        irr = npf.irr(cash_flows)
    except ValueError:
        print("Error: IRR could not be calculated. Check cashflow values.")
        return None

    # Calculate NPV using numpy_financial's npv function
    npv = npf.npv(discount_rate, cash_flows)

    # Calculate BCR
    pv_benefits = sum(benefit / (1 + discount_rate)**year for year, benefit in enumerate(benefits))
    pv_costs = sum(cost / (1 + discount_rate)**year for year, cost in enumerate(expenditures))
    bcr = pv_benefits / pv_costs

    # Calculate discounted expenditures, benefits, and net incomes for each year
    discounted_expenditures = []
    discounted_benefits = []
    net_incomes = []
    for year in range(duration):
        discount_factor = 1 / (1 + discount_rate) ** (year + 1)
        discounted_expenditure = expenditures[year] * discount_factor
        discounted_benefit = benefits[year] * discount_factor
        net_income = discounted_benefit - discounted_expenditure
        discounted_expenditures.append(discounted_expenditure)
        discounted_benefits.append(discounted_benefit)
        net_incomes.append(net_income)

    # Calculate total discounted expenditure and discounted benefits
    total_discounted_expenditure = sum(discounted_expenditures)
    total_discounted_benefits = sum(discounted_benefits)

    return irr, bcr, npv, discounted_expenditures, discounted_benefits, net_incomes, total_discounted_expenditure, total_discounted_benefits


# Example usage
if __name__ == "__main__":
    duration = int(input("Enter project duration (years): "))
    expenditures = list(map(float, input("Enter expenditures for each year (separated by spaces): ").split()))
    benefits = list(map(float, input("Enter benefits for each year (separated by spaces): ").split()))
    discount_rate = float(input("Enter discount rate (as a percentage): "))

    result = calculate_financial_metrics(duration, expenditures, benefits, discount_rate)

    if result is not None:  # Check if calculations were successful
        irr, bcr, npv, discounted_expenditures, discounted_benefits, net_incomes, total_discounted_expenditure, total_discounted_benefits = result
        print("IRR: {:.2%}".format(irr))
        print("BCR: {:.2f}".format(bcr))
        print("NPV: {:.2f}".format(npv))

        # Display discounted expenditures, discounted benefits, and net income for each year
        print("\nDiscounted Expenditures:")
        for year, expenditure in enumerate(discounted_expenditures, start=1):
            print(f"Year {year}: ${expenditure:.2f}")
        
        print("\nDiscounted Benefits:")
        for year, benefit in enumerate(discounted_benefits, start=1):
            print(f"Year {year}: ${benefit:.2f}")

        print("\nNet Income:")
        for year, income in enumerate(net_incomes, start=1):
            print(f"Year {year}: ${income:.2f}")

        # Display total discounted expenditure and total discounted benefits
        print("\nTotal Discounted Expenditure:", total_discounted_expenditure)
        print("Total Discounted Benefits:", total_discounted_benefits)
