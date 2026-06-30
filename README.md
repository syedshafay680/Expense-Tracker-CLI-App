# 💰 Expense Tracker CLI

A clean, fast, and friendly command-line expense tracker built in pure Python — no external dependencies required. Track your spending, categorize transactions, and view monthly summaries, all from your terminal.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-CLI-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## ✨ Features

- **Add Expenses** — Record amount, category, description, and date in seconds
- **View All Expenses** — Neatly formatted table sorted by most recent
- **Delete Expenses** — Remove entries by ID with a confirmation prompt
- **Monthly Summary** — Spending broken down by category, grouped by month
- **Search by Category** — Instantly filter and total expenses for any category
- **Persistent Storage** — Data is saved locally to `expenses.json`
- **Input Validation** — Friendly error handling for amounts, dates, and choices
- **Zero Dependencies** — Runs with the Python standard library only

---

## 📸 Preview

```
=============================================
       💰 EXPENSE TRACKER CLI APP 💰
=============================================

─── Main Menu ───
  1. Add Expense
  2. View All Expenses
  3. Delete Expense
  4. Monthly Summary
  5. Search by Category
  6. Exit

Enter choice: 2

─── All Expenses ───

ID    Date         Category        Amount (PKR)  Description
─────────────────────────────────────────────────────────────
3     2025-06-20    Food                  450.00  Lunch with friends
2     2025-06-18    Transport             120.00  Careem ride
1     2025-06-15    Shopping             2500.00  New shoes
─────────────────────────────────────────────────────────────
                                     TOTAL   3070.00
```

---

## 🗂️ Categories

| | | |
|---|---|---|
| 🍔 Food | 🚗 Transport | 🛍️ Shopping |
| ⚕️ Health | 🎬 Entertainment | 💡 Utilities |
| 📚 Education | 📦 Other | |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/expense-tracker-cli.git
cd expense-tracker-cli

# Run the app
python expense_tracker.py
```

That's it — no `pip install` required.

---

## 🛠️ Usage

Launch the app and choose an option from the main menu:

1. **Add Expense** — Enter a description, amount, category, and date (defaults to today)
2. **View All Expenses** — See every recorded expense with a running total
3. **Delete Expense** — Pick an ID to remove, with a confirmation step
4. **Monthly Summary** — View totals grouped by month and category
5. **Search by Category** — Filter expenses by a specific category
6. **Exit** — Save and quit

All data is automatically saved to `expenses.json` in the project directory after every change.

---

## 📁 Project Structure

```
expense-tracker-cli/
├── expense_tracker.py   # Main application
├── expenses.json         # Auto-generated data file (created on first use)
└── README.md
```

---

## 🧩 How It Works

The app stores each expense as a JSON object:

```json
{
  "id": 1,
  "description": "Lunch with friends",
  "amount": 450.0,
  "category": "Food",
  "date": "2025-06-20"
}
```

All records live in a single `expenses.json` file, loaded into memory on startup and saved back after every change — keeping the app simple, transparent, and easy to back up or version control.

---

## 🗺️ Roadmap

- [ ] Export expenses to CSV/Excel
- [ ] Edit existing expenses
- [ ] Budget limits with alerts
- [ ] Multi-currency support
- [ ] Charts and visual reports

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](../../issues) or open a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Built as part of an internship task focused on practical Python programming.

<p align="center">Made with ❤️ and Python</p>
