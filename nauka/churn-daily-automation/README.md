# Churn Daily Automation

Automated daily churn data collection, budgeting, and reporting system with interactive React dashboard.

## Features

### ✅ Implemented

* **Automated data collection** from multiple sources:
  * Business Segment A: Outlook email (HTML table parsing)
  * Business Segment B: Outlook email (MultiIndex table parsing)
  * Business Segment C: Database SQL query
* **Budget tracking system**:
  * Budget data extraction from Excel reports
  * Budget vs execution comparison
  * Automated budget import to database
* **Interactive React Dashboard**:
  * Real-time data visualization with 3 business segment cards
  * Budget vs execution tables (WY | BU | %)
  * Color-coded performance indicators (🔴 0-69%, 🟡 70-89%, 🟢 90%+)
  * Month selector and data filtering
  * Comparison view (month-to-month analysis)
  * Charts (line, bar, pie) using Recharts
* **Intelligent data storage**:
  * Smart INSERT/UPDATE logic based on month existence
  * Error handling with partial data saving
  * Database transaction management
* **FastAPI Backend**:
  * RESTful API endpoints
  * Manual update controls per segment
  * Budget data endpoints
* **Windows Task Scheduler integration** for daily execution

### 🔜 Planned

* **Excel report automation**:
  * Automated report updates with execution data
  * Template-based Excel generation
  * Download functionality
* **Data export**:
  * Export filtered data to Excel
  * Custom date ranges
* **SQL Playground**:
  * Interactive query interface
  * Result visualization

## Project Structure

```
churn-daily-automation/
├── backend/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application
│   │   ├── database.py          # Database connection
│   │   └── models.py            # Pydantic models
│   ├── scripts/
│   │   ├── __init__.py
│   │   ├── churn_daily.py       # Main automation script
│   │   ├── load_budget.py       # Extract budget from Excel
│   │   └── insert_budget.py     # Insert budget to database
│   ├── credentials/             # NOT COMMITTED
│   │   ├── Pass.xlsx            # Database credentials
│   │   └── budget.xlsx          # Generated budget file
│   ├── templates/               # Excel templates
│   ├── temp/                    # Generated files
│   └── requirements.txt         # Python dependencies
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx    # Main dashboard with budget cards
│   │   │   ├── ChurnTable.jsx   # Data table with filters
│   │   │   ├── UpdateButtons.jsx # Manual update controls
│   │   │   ├── PLKForm.jsx      # Manual data entry form
│   │   │   ├── Charts.jsx       # Recharts visualizations
│   │   │   ├── Comparison.jsx   # Month-to-month comparison
│   │   │   └── Tabs.jsx         # Tab navigation
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── automation/
│   ├── uruchom_churn.bat        # Task Scheduler (daily automation)
│   └── uruchom_serwer.bat       # Start both servers (dev)
├── .gitignore                   # Excludes credentials & sensitive data
└── README.md
```

## Quick Start

### Prerequisites

* Python 3.14+
* Node.js 16+
* Database ODBC Driver
* Microsoft Outlook (Windows)
* Access to corporate database

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/churn-daily-automation.git
cd churn-daily-automation
```

1. **Install backend dependencies:**

```bash
cd backend
pip install -r requirements.txt
```

**requirements.txt:**

```
fastapi
uvicorn
pandas
pyodbc
openpyxl
```

1. **Install frontend dependencies:**

```bash
cd frontend
npm install
```

1. **Configure credentials:**

Create `backend/credentials/Pass.xlsx` with:

* Column "Co": credential keys (username, password, database)
* Column "wartosc": credential values

### Running the Application

#### Development Mode

**Backend (FastAPI):**

```bash
cd backend/api
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Frontend (React):**

```bash
cd frontend
npm start
```

* Backend: <http://127.0.0.1:8000>
* Frontend: <http://localhost:3000>

#### Production Mode

Use the provided batch file or Windows Task Scheduler for automated daily execution.

## 📊 Data Flow

```
Email Sources ──┐
SQL Queries ────┼──> Python Scripts ──> Database ──> FastAPI ──> React Dashboard
Excel Reports ──┘
```

## 🔧 Technical Details

### Data Sources

1. **Business Segment A**
   * Source: Daily email with HTML table
   * Products: Multiple product lines
   * Arrival: Morning (~9-10 AM)

2. **Business Segment B**
   * Source: Daily email with MultiIndex HTML table
   * Products: Multiple service categories
   * Arrival: Midday (~12-13 PM)
   * Note: Data appears after 10th of month

3. **Business Segment C**
   * Source: Database SQL query
   * Products: Subscription services
   * Real-time data

### Database Schema

#### Table 1: Execution Data

```sql
CREATE TABLE schema.Churn_Daily (
    MIESIAC CHAR(6),           -- YYYYMM format
    SPOLKA VARCHAR(10),        -- Business segment
    PRODUKT VARCHAR(20),       -- Product name
    WARTOSC INTEGER,           -- Churn count
    DATA_RAPORTU DATE,         -- Report date
    PRIMARY KEY (MIESIAC, SPOLKA, PRODUKT)
);
```

#### Table 2: Budget Data

```sql
CREATE TABLE schema.Churn_Daily_BU (
    ROK_MSC CHAR(6),          -- YYYYMM format
    SPOLKA VARCHAR(10),       -- Business segment
    PRODUKT VARCHAR(20),      -- Product name
    WARTOSC INTEGER,          -- Budget churn count
    PRIMARY KEY (ROK_MSC, SPOLKA, PRODUKT)
);
```

### API Endpoints

#### GET `/api/churn/all`

Returns all churn data.

**Response:**

```json
{
  "count": 150,
  "records": [
    {
      "MIESIAC": "202603",
      "SPOLKA": "SEGMENT_A",
      "PRODUKT": "PRODUCT_1",
      "WARTOSC": 1234,
      "DATA_RAPORTU": "2026-03-10"
    }
  ]
}
```

#### GET `/api/budget/all`

Returns all budget data.

**Response:**

```json
{
  "count": 120,
  "records": [
    {
      "ROK_MSC": "202603",
      "SPOLKA": "SEGMENT_A",
      "PRODUKT": "PRODUCT_1",
      "WARTOSC": 1500
    }
  ]
}
```

#### POST `/api/update/{segment}`

Updates data for specific business segment (previous month).

**Response:**

```json
{
  "message": "Updated SEGMENT_A for 202602: 12 records"
}
```

#### POST `/api/churn_refresh/all`

Refreshes all data.

**Response:**

```json
{
  "message": "Updated all data"
}
```

## 🎨 Dashboard Features

### Tab 1: Dashboard

* **Header:** Summary | Total for YYYY-MM: XXXX | Month selector
* **3 Business Segment Cards** with product tables:
  * Columns: Product | Execution (WY) | Budget (BU) | % Performance
  * Color-coded performance:
    * 🔴 0-69% - Weak
    * 🟡 70-89% - Average
    * 🟢 90%+ - Good
* **Legend + Update Buttons** (side by side)

### Tab 2: Table

* Full data table with filters (Segment, Month, Product)
* Record count display
* Refresh button

### Tab 3: Charts

* Line chart - Monthly trend
* Bar chart - Segment comparison
* Pie chart - Percentage distribution

### Tab 4: Manual Entry

* Form for manual data entry
* Fields: Product, Month, Value
* Submit with validation

### Tab 5: Comparison

* Month-to-month comparison table
* Change % column
* Color-coded increases (green) and decreases (red)

## 🤖 Automation Scripts

### 1. `churn_daily.py`

Main data collection script.

**Functions:**

* Fetches churn data from all sources
* Inserts data to database (UPSERT logic)
* Logs results to console

**Execution:**

```bash
python backend/scripts/churn_daily.py
```

### 2. `load_budget.py`

Extracts budget from Excel reports.

**Functions:**

* Reads Excel report file
* Extracts budget values per product per month
* Saves to Excel file in `backend/credentials/`

**Configuration (update yearly):**

```python
ROK = 2026                # ← Change at year start
MIESIAC_PROGNOZY = 3      # ← Month number with forecast column
```

**Execution:**

```bash
python backend/scripts/load_budget.py
```

### 3. `insert_budget.py`

Imports budget to database.

**Functions:**

* Reads generated budget Excel file
* Inserts data to budget table (UPSERT logic)
* Logs results to console

**Execution:**

```bash
python backend/scripts/insert_budget.py
```

## 📝 Roadmap

### Priority 1: Excel Report Automation

- [ ] Endpoint `POST /api/excel/update-report`
* [ ] Excel template in `backend/templates/`
* [ ] Row×Column mapping for execution data
* [ ] Frontend: "Update Excel Report" button
* [ ] Download functionality

### Priority 2: Data Export

- [ ] Export filtered data to Excel
* [ ] "Export to Excel" button in Table tab
* [ ] Custom date range selection

### Priority 3: SQL Playground

- [ ] Interactive query interface
* [ ] SQL textarea
* [ ] Execute button
* [ ] Results table

## 🔒 Security

### ⚠️ DO NOT COMMIT

Add to `.gitignore`:

```gitignore
# Credentials
backend/credentials/
*.xlsx
*.xls
.env

# Temporary files
backend/temp/
*.log

# IDE
.vscode/
.idea/
*.swp

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/

# Node
node_modules/
npm-debug.log
```

## 📅 Version History

### 2026-03-10 (v0.6)

- ✅ Dashboard layout redesign
* ✅ Budget vs execution cards with color coding
* ✅ Legend in single line
* ✅ Update buttons vertically aligned

### 2026-03-05 (v0.5)

- ✅ Budget table in database
* ✅ Budget extraction and import scripts
* ✅ Dashboard with budget comparison
* ✅ Performance color coding

### 2026-03-04 (v0.4)

- ✅ Dashboard tabs
* ✅ Charts (Recharts)
* ✅ Table filters
* ✅ Task Scheduler integration

### 2026-03-03 (v0.3)

- ✅ React Dashboard
* ✅ FastAPI backend
* ✅ API endpoints

### 2026-03-01/02 (v0.1/0.2)

- ✅ Python automation scripts
* ✅ Database connection
* ✅ Email parsing logic

## Contributing

This is a personal project, but suggestions and feedback are welcome!

## License

This project is for internal use.

## Author

Data Analyst specializing in automation, ETL processes, and Python development.

---

**Note:** Sensitive data (credentials, company-specific information, network paths) are excluded via `.gitignore`.
