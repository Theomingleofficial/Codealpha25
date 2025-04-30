#install yfiance
import yfinance as yf

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        ticker = ticker.upper()
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker}.")

    def remove_stock(self, ticker, shares):
        ticker = ticker.upper()
        if ticker in self.portfolio:
            if shares >= self.portfolio[ticker]:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker}.")
            else:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker}.")
        else:
            print(f"{ticker} not found in portfolio.")

    def view_portfolio(self):
        if not self.portfolio:
            print("Your portfolio is empty.")
            return

        print("\nCurrent Portfolio:")
        total_value = 0.0
        for ticker, shares in self.portfolio.items():
            try:
                stock = yf.Ticker(ticker)
                price = stock.info.get('regularMarketPrice')
                if price is None:
                    print(f"Could not fetch price for {ticker}.")
                    continue
                value = price * shares
                total_value += value
                print(f"{ticker}: {shares} shares @ ${price:.2f} = ${value:.2f}")
            except Exception as e:
                print(f"Error fetching data for {ticker}: {e}")
        print(f"Total Portfolio Value: ${total_value:.2f}\n")

def main():
    portfolio = StockPortfolio()

    while True:
        print("\n=== Stock Portfolio Tracker ===")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == '1':
            ticker = input("Enter stock ticker (e.g., AAPL): ")
            try:
                shares = int(input("Enter number of shares: "))
                if shares > 0:
                    portfolio.add_stock(ticker, shares)
                else:
                    print("Number of shares must be positive.")
            except ValueError:
                print("Invalid number of shares.")

        elif choice == '2':
            ticker = input("Enter stock ticker to remove: ")
            try:
                shares = int(input("Enter number of shares to remove: "))
                if shares > 0:
                    portfolio.remove_stock(ticker, shares)
                else:
                    print("Number of shares must be positive.")
            except ValueError:
                print("Invalid number of shares.")

        elif choice == '3':
            portfolio.view_portfolio()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1–4.")

if __name__ == "__main__":
    main()
