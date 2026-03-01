# Churn Daily Automation

Automated daily churn data collection and reporting system for telecommunications companies (PLK, Netia, CP).

## Features

- **Automated data collection** from multiple sources:
  - PLK: Outlook email (HTML table parsing)
  - Netia: Outlook email (MultiIndex table parsing)
  - CP: Teradata SQL query
- **Intelligent data storage** in Teradata database
- **Smart INSERT/UPDATE logic** based on month existence
- **Error handling** with partial data saving
- **Windows Task Scheduler integration** for daily execution
- **Planned React dashboard** for data visualization

## Project Structure

```
churn-daily-automation/
├── backend/
│   ├── scripts/
│   │   └── churn_daily.py          # Main automation script
│   ├── api/                         # FastAPI (coming soon)
│   └── requirements.txt             # Python dependencies
├── automation/
│   └── uruchom_churn.bat           # Task Scheduler launcher
├── docs/
│   └── project-plan.md             # Detailed project plan
├── .gitignore
└── README.md
```

## Quick Start

### Prerequisites

- Python 3.14+
- Teradata ODBC Driver 16.20
- Microsoft Outlook (Windows)
- Access to Teradata database

### Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/churn-daily-automation.git
cd churn-daily-automation
```

1. Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

1. Configure credentials:
Create `Pass.xlsx` in your user directory with:

- Column "Co": credential keys (teralog, terapas, dbc)
- Column "wartosc": credential values

### Running the Script

**Manual execution:**

```bash
python backend/scripts/churn_daily.py
```

**Automated execution (Windows Task Scheduler):**

1. Open Task Scheduler
2. Import task from `automation/uruchom_churn.bat`
3. Configure to run daily at 14:00

## 📊 Data Flow

```
Outlook (PLK) ──┐
                ├──> Python Script ──> Teradata Database ──> Excel Power Query
Outlook (Netia)─┤
                │
Teradata (CP) ──┘
```

## 🔧 Technical Details

### Data Sources

1. **PLK** (Polkomtel)
   - Source: Daily email with HTML table
   - Products: BIZ, DATA, DATA_FTTH, IND, MIX
   - Arrival: 9:30-10:00

2. **Netia**
   - Source: Daily email with MultiIndex HTML table
   - Products: BB OFFNET, BB ONNET, MOBILE, TV, VOICE OFFNET, VOICE ONNET
   - Arrival: 12:50-13:00
   - Note: Data appears after 10th of month

3. **CP** (Cyfrowy Polsat)
   - Source: Teradata SQL query
   - Products: TV (Kontrakt TV), IN (Internet)
   - Real-time data

### Database Schema

```sql
CREATE TABLE db_work_dwn.Churn_Daily (
    DATA_RAPORTU DATE,
    SPOLKA VARCHAR(10),
    PRODUKT VARCHAR(20),
    WARTOSC INTEGER,
    MIESIAC CHAR(6)
);
```

## Roadmap

- [x] Automated data collection
- [x] Teradata integration
- [x] Error handling
- [x] Task Scheduler automation
- [ ] FastAPI backend
- [ ] React dashboard
- [ ] Manual data entry interface
- [ ] SQL playground
- [ ] Month-to-month comparisons

## Contributing

This is a personal project, but suggestions and feedback are welcome!

## License

This project is for internal use.

## Author

**Mateusz Grabiński**

- Data Analyst @ Polkomtel (Cyfrowy Polsat Group)
- Focus: Data automation, ETL processes, Python development

---

**Note:** Sensitive data (credentials, company-specific information) are excluded via `.gitignore`.
