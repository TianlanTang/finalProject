## Installation
```powershell
# Clone the repository
git clone https://github.com/TianlanTang/finalProject guessCountryOrRegion
cd guessCountryOrRegion

# Start game
python main.py
```
1. Select a difficulty level (1–3).
2. Guess the country or region by name or use fuzzy/prefix match.
3. View colored hints and table comparisons after each guess.
4. You have 10 attempts to guess the target country.

## Project Structure
```
├── main.py             # Game entry point
├── country_data.py     # Load and preprocess CSV data
├── cal_stats.py        # Compare statistics and formatting
├── trie_tree.py        # Trie implementation for prefix & fuzzy search
├── global_stats_2022.csv
└── readme.md
```