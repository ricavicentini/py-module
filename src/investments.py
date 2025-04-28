def predict_income(initial_value, expected_value):
    """
    Predicts the income from an investment based on the initial and expected values.
    Args:
        initial_value (float): The initial value of the investment.
        expected_value (float): The expected value of the investment.
    Returns:
        float: The predicted percentage income from the investment.
    """
    return (expected_value - initial_value) / initial_value * 100

def compound_interest(principal, anual_rate, time):
    """
    Calculates the compound interest from an investment.
    Args:
        principal (float): The initial value of the investment.
        rate (float): The rate of interest.
        time (int): The time period of the investment in years.
    Returns:
        float: The compound interest from the investment.
    """
    decimal_rate = anual_rate / 100
    return principal * (1 + decimal_rate) ** time


def anual_rate_to_monthly(anual_rate):
    """
    Converts an annual rate to a monthly rate using compound interest formula.
    Args:
        anual_rate (float): The annual interest rate in percentage.
    Returns:
        float: The equivalent monthly interest rate in percentage.
    """
    monthly_rate = (1 + anual_rate / 100) ** (1 / 12) - 1
    return monthly_rate * 100


def cagr(initial_value, final_value, time): 
    """
    Calculates the Compound Annual Growth Rate (CAGR) of an investment.
    Args:
        initial_value (float): The initial value of the investment.
        final_value (float): The final value of the investment.
        time (int): The time period of the investment in years.
    Returns:
        float: The Compound Annual Growth Rate (CAGR) of the investment.
    """
    return ((final_value / initial_value) ** (1 / time) - 1) * 100



