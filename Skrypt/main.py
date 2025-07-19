from datetime import datetime, timedelta
import os
import random
from pathlib import Path


def get_next_week_range(today=None): # All AI function 
    if today is None:
        today = datetime.today()

    # Calculate how many days until the next Monday
    days_until_next_monday = (7 - today.weekday()) % 7
    if days_until_next_monday == 0:
        days_until_next_monday = 7  # If today is Monday, we want the NEXT one

    next_monday = today + timedelta(days=days_until_next_monday)
    next_sunday = next_monday + timedelta(days=6)

    return next_monday.date(), next_sunday.date()




def read_meals_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def create_weekly_menu():
    # Get next week's range
    start_date, end_date = get_next_week_range()

    # Load meals
    breakfasts = read_meals_from_file("Sniadania.txt")
    dinners = read_meals_from_file("Obiady.txt")
    snacks = read_meals_from_file("Przekaski.txt")
    suppers = read_meals_from_file("Kolacje.txt")

    # Create output directory
    output_dir = Path("Jadlospisy")
    output_dir.mkdir(exist_ok=True)

    # Build weekly menu content
    weekly_menu = []

    for i in range(7):
        day = start_date + timedelta(days=i)
        date_str = day.strftime("%A, %d %B %Y")

        breakfast = random.choice(breakfasts)
        dinner = random.choice(dinners)
        snack = random.choice(snacks)
        supper = random.choice(suppers)

        daily_menu = (
            f"{date_str}\n"
            f"{'-'*40}\n"
            f"Śniadanie: {breakfast}\n"
            f"Obiad: {dinner}\n"
            f"Przekąska: {snack}\n"
            f"Kolacja: {supper}\n\n"
        )

        weekly_menu.append(daily_menu)

    # Final output filename
    file_name = f"{start_date.isoformat()}_to_{end_date.isoformat()}.txt"
    file_path = output_dir / file_name

    # Write to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(weekly_menu)

if __name__ == "__main__":
    create_weekly_menu()