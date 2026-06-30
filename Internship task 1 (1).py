"""
Expense Tracker CLI App
Internship Task 1 - Python Programming
"""

import json
import os
from datetime import datetime
from collections import defaultdict

DATA_FILE = "expenses.json"

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Health",
    "Entertainment",
    "Utilities",
    "Education",
    "Other"
]


# ─────────────────────────────────────────
#  DATA HELPERS
# ─────────────────────────────────────────

def load_data():
    """Load expenses from JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print("⚠️  Warning: Could not read data file. Starting fresh.")
        return []


def save_data(expenses):
    """Save expenses to JSON file."""
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(expenses, f, indent=2)
    except IOError as e:
        print(f"❌ Error saving data: {e}")


# ─────────────────────────────────────────
#  INPUT HELPERS
# ─────────────────────────────────────────

def get_float(prompt):
    """Get a valid positive float from the user."""
    while True:
        val = input(prompt).strip()
        try:
            amount = float(val)
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue
            return round(amount, 2)
        except ValueError:
            print("❌ Invalid amount. Please enter a number (e.g. 250 or 99.50).")


def get_category():
    """Let the user pick a category."""
    print("\nCategories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    while True:
        choice = input("Choose category (1-8): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print(f"❌ Please enter a number between 1 and {len(CATEGORIES)}.")


def get_description():
    """Get a non-empty description."""
    while True:
        desc = input("Description: ").strip()
        if desc:
            return desc
        print("❌ Description cannot be empty.")


def get_date():
    """Get a date from user or use today."""
    today = datetime.today().strftime("%Y-%m-%d")
    val = input(f"Date (YYYY-MM-DD) [leave blank for today: {today}]: ").strip()
    if not val:
        return today
    try:
        datetime.strptime(val, "%Y-%m-%d")
        return val
    except ValueError:
        print(f"❌ Invalid date. Using today: {today}")
        return today


def generate_id(expenses):
    """Generate next numeric ID."""
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1


# ─────────────────────────────────────────
#  CORE FEATURES
# ─────────────────────────────────────────

def add_expense(expenses):
    print("\n─── Add Expense ───")
    desc   = get_description()
    amount = get_float("Amount (PKR): ")
    cat    = get_category()
    date   = get_date()

    expense = {
        "id":          generate_id(expenses),
        "description": desc,
        "amount":      amount,
        "category":    cat,
        "date":        date
    }
    expenses.append(expense)
    save_data(expenses)
    print(f"\n✅ Expense added! ID: {expense['id']}")


def view_expenses(expenses):
    print("\n─── All Expenses ───")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"\n{'ID':<5} {'Date':<12} {'Category':<15} {'Amount (PKR)':>12}  Description")
    print("─" * 65)
    for e in sorted(expenses, key=lambda x: x["date"], reverse=True):
        print(f"{e['id']:<5} {e['date']:<12} {e['category']:<15} {e['amount']:>12.2f}  {e['description']}")
    print("─" * 65)
    total = sum(e["amount"] for e in expenses)
    print(f"{'TOTAL':>34} {total:>12.2f}")


def delete_expense(expenses):
    print("\n─── Delete Expense ───")
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses(expenses)
    while True:
        val = input("\nEnter ID to delete (or 0 to cancel): ").strip()
        if not val.isdigit():
            print("❌ Please enter a valid ID.")
            continue
        expense_id = int(val)
        if expense_id == 0:
            print("Cancelled.")
            return
        match = next((e for e in expenses if e["id"] == expense_id), None)
        if not match:
            print(f"❌ No expense found with ID {expense_id}.")
            continue
        confirm = input(f"Delete '{match['description']}' ({match['amount']} PKR)? (y/n): ").strip().lower()
        if confirm == "y":
            expenses.remove(match)
            save_data(expenses)
            print("✅ Expense deleted.")
        else:
            print("Cancelled.")
        return


def monthly_summary(expenses):
    print("\n─── Monthly Summary ───")
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Group by year-month
    monthly = defaultdict(lambda: defaultdict(float))
    for e in expenses:
        ym = e["date"][:7]  # "2025-06"
        monthly[ym][e["category"]] += e["amount"]

    for ym in sorted(monthly.keys(), reverse=True):
        print(f"\n📅  {ym}")
        print(f"  {'Category':<15} {'Amount (PKR)':>12}")
        print("  " + "─" * 28)
        total = 0
        for cat, amt in sorted(monthly[ym].items()):
            print(f"  {cat:<15} {amt:>12.2f}")
            total += amt
        print("  " + "─" * 28)
        print(f"  {'TOTAL':<15} {total:>12.2f}")


def search_by_category(expenses):
    print("\n─── Search by Category ───")
    cat = get_category()
    results = [e for e in expenses if e["category"] == cat]
    if not results:
        print(f"No expenses found in '{cat}'.")
        return
    print(f"\nExpenses in '{cat}':")
    print(f"\n{'ID':<5} {'Date':<12} {'Amount (PKR)':>12}  Description")
    print("─" * 50)
    for e in sorted(results, key=lambda x: x["date"], reverse=True):
        print(f"{e['id']:<5} {e['date']:<12} {e['amount']:>12.2f}  {e['description']}")
    total = sum(e["amount"] for e in results)
    print("─" * 50)
    print(f"{'TOTAL':>29} {total:>12.2f}")


# ─────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────

def main():
    expenses = load_data()
    print("=" * 45)
    print("       💰 EXPENSE TRACKER CLI APP 💰")
    print("=" * 45)

    menu = {
        "1": ("Add Expense",           add_expense),
        "2": ("View All Expenses",     view_expenses),
        "3": ("Delete Expense",        delete_expense),
        "4": ("Monthly Summary",       monthly_summary),
        "5": ("Search by Category",    search_by_category),
        "6": ("Exit",                  None),
    }

    while True:
        print("\n─── Main Menu ───")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("\nEnter choice: ").strip()

        if choice not in menu:
            print("❌ Invalid option. Please choose 1-6.")
            continue

        label, func = menu[choice]
        if func is None:
            print("\nGoodbye! Keep tracking those expenses 💸")
            break

        # view_expenses and monthly_summary only need expenses (read-only)
        if func in (view_expenses, monthly_summary, search_by_category):
            func(expenses)
        else:
            func(expenses)


if __name__ == "__main__":
    main()