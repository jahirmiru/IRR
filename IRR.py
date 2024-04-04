import numpy as np
import numpy_financial as npf

def calculate_financial_metrics(duration, expenditures, benefits, discount_rate):
    """
    Calculates the IRR, BCR, and NPV of a project.

    Args:
        duration (int): The project duration in years.
        expenditures (list): A list of expenditures for each year.
        benefits (list): A list of benefits for each year.
        discount_rate (float): The discount rate as a percentage.

    Returns:
        tuple: (irr, bcr, npv) or None if calculation fails
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

    return irr, bcr, npv


# Example usage
if __name__ == "__main__":
    duration = int(input("Enter project duration (years): "))
    expenditures = list(map(float, input("Enter expenditures for each year (separated by spaces): ").split()))
    benefits = list(map(float, input("Enter benefits for each year (separated by spaces): ").split()))
    discount_rate = float(input("Enter discount rate (as a percentage): "))

    irr_bcr_npv = calculate_financial_metrics(duration, expenditures, benefits, discount_rate)

    if irr_bcr_npv is not None:  # Check if calculations were successful
        irr, bcr, npv = irr_bcr_npv
        print("IRR: {:.2%}".format(irr))
        print("BCR: {:.2f}".format(bcr))
        print("NPV: {:.2f}".format(npv))
