from investments import predict_income, compound_interest, anual_rate_to_monthly, cagr

def main():
    # Example values
    initial_investment = 1000.0
    expected_value = 1500.0
    annual_rate = 12.0
    time_years = 3

    # Calculate and display results
    print("\nInvestment Analysis")
    print("=" * 50)
    
    # Predict income
    income_percentage = predict_income(initial_investment, expected_value)
    print(f"\nPredicted Income:")
    print(f"Initial Investment: ${initial_investment:,.2f}")
    print(f"Expected Value: ${expected_value:,.2f}")
    print(f"Predicted Return: {income_percentage:.2f}%")

    # Compound interest
    final_amount = compound_interest(initial_investment, annual_rate, time_years)
    print(f"\nCompound Interest Calculation:")
    print(f"Principal: ${initial_investment:,.2f}")
    print(f"Annual Rate: {annual_rate:.2f}%")
    print(f"Time Period: {time_years} years")
    print(f"Final Amount: ${final_amount:,.2f}")

    # Annual to monthly rate conversion
    monthly_rate = anual_rate_to_monthly(annual_rate)
    print(f"\nRate Conversion:")
    print(f"Annual Rate: {annual_rate:.2f}%")
    print(f"Equivalent Monthly Rate: {monthly_rate:.2f}%")

    # CAGR calculation
    cagr_rate = cagr(initial_investment, final_amount, time_years)
    print(f"\nCompound Annual Growth Rate (CAGR):")
    print(f"Initial Value: ${initial_investment:,.2f}")
    print(f"Final Value: ${final_amount:,.2f}")
    print(f"Time Period: {time_years} years")
    print(f"CAGR: {cagr_rate:.2f}%")

if __name__ == "__main__":
    main() 