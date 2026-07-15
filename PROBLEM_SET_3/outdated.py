
months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def main():

    # Keep asking until a valid date is entered
    while True:
        try:

            # Take input and remove leading/trailing spaces
            anno_domini = input("Date: ").strip()

            # ---------- Format: MM/DD/YYYY ----------
            if "/" in anno_domini:

                # Split into month, day and year
                month, day, year = anno_domini.split("/")

                # Convert strings to integers
                month = int(month)
                day = int(day)
                year = int(year)

            # ---------- Format: Month DD, YYYY ----------
            elif "," in anno_domini:

                # Example:
                # "September 8, 1636"
                # becomes
                # ["September", "8,", "1636"]
                month, day, year = anno_domini.split()

                # Remove comma from day
                day = day.replace(",", "")

                # Convert month name to month number
                month = months.index(month) + 1

                # Convert day and year to integers
                day = int(day)
                year = int(year)

            # Invalid format
            else:
                raise ValueError

            # Validate month
            if not (1 <= month <= 12):
                raise ValueError

            # Validate day
            if not (1 <= day <= 31):
                raise ValueError

            # Print in ISO format
            print(f"{year}-{month:02}-{day:02}")
            break
        # Invalid input → ask again
        except (ValueError, IndexError):
            continue


main()