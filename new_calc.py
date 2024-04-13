import numpy as np

def calculate_irr_bcr_npv():
    # Get user input
    project_duration = int(input("Enter the project duration (in years): "))
    yearly_costs = []
    yearly_revenue = []
    discount_rate = float(input("Enter the discount rate: "))

    for year in range(project_duration):
        yearly_costs.append(float(input(f"Enter the yearly cost for year {year + 1}: ")))
        yearly_revenue.append(float(input(f"Enter the yearly revenue for year {year + 1}: ")))

    # Calculate cash flow
    cash_flow = [revenue - cost for revenue, cost in zip(yearly_revenue, yearly_costs)]

    # Calculate IRR
    irr = np.irr(cash_flow)

    # Calculate BCR
    npv = 0
    for i, cf in enumerate(cash_flow):
        npv += cf / (1 + discount_rate) ** (i + 1)
    bcr = npv / sum(yearly_costs)

    # Calculate NPV
    npv = 0
    for i, cf in enumerate(cash_flow):
        npv += cf / (1 + discount_rate) ** (i + 1)

    # Print results
    print(f"Internal Rate of Return (IRR): {irr:.2%}")
    print(f"Benefit-Cost Ratio (BCR): {bcr:.2f}")
    print(f"Net Present Value (NPV): {npv:.2f}")

if __name__ == "__main__":
    calculate_irr_bcr_npv()
