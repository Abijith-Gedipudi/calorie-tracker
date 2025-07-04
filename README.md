CALAORIE TRACKER
1) Features
  Food Selection Dropdown: Choose from a list of food items to add to your daily log.

  Live Nutrient Breakdown: View real-time pie chart showing % of carbs, proteins, and fats.

  Dynamic Totals: Automatically updates total calories and macronutrients as you add or remove items.

  Calorie Goal Progress Bar: Visual tracker showing how close you are to your daily calorie target.

  Nutritional Insights Engine: Smart feedback based on your current intake (e.g., low protein warning).

2)Tech Stack
  Frontend:
    HTML5, CSS3, Bootstrap 4
    JavaScript (Chart.js for dynamic charts)

  Backend:
    Python
    Django Web Framework

  Database:
    SQLite (default Django database)

  Tools & Environment:
    Git & GitHub for version control
    VS Code for development
    Virtual Environment (venv) for dependency isolation
 
 3)Screenshot
 ![image](https://github.com/user-attachments/assets/a5c311b9-fa33-4c9b-808a-92d29e09c2a2)

3)Project Structure
calorie-tracker/
├── calorietracker/            # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── tracker/                   # Main app
│   ├── migrations/
│   ├── static/                # Static files (CSS, JS)
│   ├── templates/             # HTML templates
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── db.sqlite3                 # SQLite database
├── manage.py                  # Django's management script
└── requirements.txt           # Project dependencies

  
