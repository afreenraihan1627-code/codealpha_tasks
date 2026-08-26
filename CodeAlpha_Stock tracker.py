from datetime import datetime

# Hardcoded dictionary of stock prices (per share)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}


def show_available_stocks():
    """Display the list of stocks and their prices."""
    print("\nAvailable Stocks:")
    print("-" * 30)
    for stock, price in STOCK_PRICES.items():
        print(f"{stock:<8} : ${price}")
    print("-" * 30)


def get_portfolio_input():
    """Ask the user for stock names and quantities, and build the portfolio."""
    portfolio = {}

    print("\nEnter stock symbol and quantity (type 'done' to finish).")

    while True:
        stock = input("\nStock symbol (e.g. AAPL): ").upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"⚠️  '{stock}' not found in our stock list. Please choose from the list above.")
            continue

        qty_input = input(f"Quantity of {stock}: ").strip()

        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("⚠️  Please enter a valid positive number for quantity.")
            continue

        qty = int(qty_input)

        # If stock already entered before, add to existing quantity
        if stock in portfolio:
            portfolio[stock] += qty
        else:
            portfolio[stock] = qty

        print(f"✅ Added {qty} share(s) of {stock}.")

    return portfolio


def calculate_investment(portfolio):
    """Calculate total investment value and per-stock breakdown."""
    breakdown = {}
    total = 0

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * qty
        breakdown[stock] = value
        total += value

    return breakdown, total


def display_summary(portfolio, breakdown, total):
    """Print a nicely formatted summary of the portfolio."""
    print("\n" + "=" * 40)
    print("        PORTFOLIO SUMMARY")
    print("=" * 40)
    print(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        value = breakdown[stock]
        print(f"{stock:<8}{qty:<6}${price:<9}${value:<10}")

    print("-" * 40)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 40)


def save_to_file(portfolio, breakdown, total, file_format="txt"):
    """Save the portfolio summary to a .txt or .csv file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if file_format == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = breakdown[stock]
                f.write(f"{stock},{qty},{price},{value}\n")
            f.write(f"\nTotal Investment,,,{total}\n")
            f.write(f"Generated On,,,{timestamp}\n")
    else:
        filename = "portfolio_summary.txt"
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 40 + "\n")
            f.write(f"{'Stock':<8}{'Qty':<6}{'Price':<10}{'Value':<10}\n")
            f.write("-" * 40 + "\n")
            for stock, qty in portfolio.items():
                price = STOCK_PRICES[stock]
                value = breakdown[stock]
                f.write(f"{stock:<8}{qty:<6}${price:<9}${value:<10}\n")
            f.write("-" * 40 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total}\n")
            f.write(f"Generated On: {timestamp}\n")

    print(f"\n💾 Summary saved to '{filename}'")


def main():
    print("=" * 40)
    print("     STOCK PORTFOLIO TRACKER")
    print("=" * 40)

    show_available_stocks()

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting program.")
        return

    breakdown, total = calculate_investment(portfolio)
    display_summary(portfolio, breakdown, total)

    save_choice = input("\nDo you want to save this summary to a file? (y/n): ").lower().strip()

    if save_choice == "y":
        format_choice = input("Save as (txt/csv)? ").lower().strip()
        if format_choice == "csv":
            save_to_file(portfolio, breakdown, total, "csv")
        else:
            save_to_file(portfolio, breakdown, total, "txt")

    print("\nThank you for using Stock Portfolio Tracker! 📈")


if __name__ == "__main__":
    main()