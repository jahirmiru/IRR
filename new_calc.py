import numpy as np
import numpy_financial as npf

def calculate_metrics(duration, costs, revenues, discount_rate):
    """
    Calculates IRR, BCR, and NPV for a project.

    Args:
        duration (int): Project duration in years.
        costs (list): List of yearly costs.
        revenues (list): List of yearly revenues.
        discount_rate (float): Discount rate as a decimal.

    Returns:
        tuple: (IRR, BCR, NPV)
    """

    # Create the cash flow array, with costs negative and revenues positive
    cash_flows = [-c + r for c, r in zip(costs, revenues)]

    # Calculate Net Present Value (NPV)
    npv = npf.npv(discount_rate, cash_flows)

    # Calculate Internal Rate of Return (IRR) - Requires iterative estimation
    irr = npf.irr(cash_flows)

    # Calculate Benefit-Cost Ratio (BCR)
    present_value_costs = sum(c / (1 + discount_rate)**t for t, c in enumerate(costs))
    present_value_revenues = sum(r / (1 + discount_rate)**t for t, r in enumerate(revenues))
    bcr = present_value_revenues / present_value_costs

    return irr, bcr, npv


# Example usage
if __name__ == "__main__":
    duration = int(input("Enter project duration (in years): "))
    costs = [float(x) for x in input("Enter yearly costs (comma-separated): ").split(",")]
    revenues = [float(x) for x in input("Enter yearly revenues (comma-separated): ").split(",")]
    discount_rate = float(input("Enter discount rate (e.g., 0.1 for 10%): "))

    irr, bcr, npv = calculate_metrics(duration, costs, revenues, discount_rate)

    print("Internal Rate of Return (IRR): {:.2%}".format(irr))
    print("Benefit-Cost Ratio (BCR): {:.2f}".format(bcr))
    print("Net Present Value (NPV): {:.2f}".format(npv))
