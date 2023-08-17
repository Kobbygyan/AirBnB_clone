import argparse

class AirbnbConsole:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="AirBnB Clone Console")
        self.parser.add_argument("command", choices=["create", "list"], help="Command to execute")
        self.args = self.parser.parse_args()

    def create_listing(self):
        location = input("Enter location: ")
        price = float(input("Enter price: "))
        description = input("Enter description: ")
        # Logic to create a new listing
        print("Listing created!")

    def list_listings(self):
        # Logic to list all listings
        print("List of all listings.")

    def main(self):
        if self.args.command == "create":
            self.create_listing()
        elif self.args.command == "list":
            self.list_listings()
        else:
            print("Invalid command")

if __name__ == "__main__":
    console = AirbnbConsole()
    console.main()
