# Weekly Menu Generator 🍽️

This Python script automatically generates a **weekly meal plan** based on meals provided in text files. Each week's menu is saved as a single `.txt` file named with the first and last day of the week (e.g., `2025-07-21_to_2025-07-27.txt`), and stored in the `Jadlospisy` folder.

---

## 📁 File Structure

.
├── main.py
├── Sniadania.txt   # Breakfasts
├── Obiady.txt      # Dinners
├── Przekaski.txt   # Snacks
├── Kolacje.txt     # Suppers
└── Jadlospisy/     # Generated weekly menus

---

## 📌 How It Works

- Reads meal names from:
  - `Sniadania.txt` – breakfasts (one per line)
  - `Obiady.txt` – dinners
  - `Przekaski.txt` – snacks
  - `Kolacje.txt` – suppers
- Generates a random menu for each day of the upcoming week (Monday–Sunday).
- Combines all daily menus into a **single text file**.
- Saves the file in the `Jadlospisy` folder with the name format:  
  `YYYY-MM-DD_to_YYYY-MM-DD.txt`

---

## ▶️ Usage

1. Make sure you have Python 3 installed.
2. Fill the meal files (`*.txt`) with at least 7 entries each.
3. Run the script:

```bash
python main.py
```

4. Check the generated menu in the `Jadlospisy` folder.

---

## ✅ Example

Menu for Monday, 21 July 2025
----------------------------------------
Śniadanie: Jajecznica z szynką
Obiad: Spaghetti bolognese
Przekąska: Jogurt naturalny z owocami
Kolacja: Kanapka z tuńczykiem

---

## 📎 Notes

- Meals are chosen randomly; duplicates may occur.
- If you want unique meals each week, let the script be extended accordingly.

---

## 📬 License

MIT – Feel free to use, modify, and share!
