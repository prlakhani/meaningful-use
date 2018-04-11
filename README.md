# Meaningful Use exploration

### Goals
This is a project inspired by the Medicare EHR Meaningful Use attestation datasets.
I'll use it to practice some analysis, and maybe Flask and D3 skills.


### Usage
1. Optimal but optional: set up the environment using `pipenv`
1. Clone the repository
1. Set up and activate a new `python3` virtual environment for the project (only if not using `pipenv`)
1. Install the project requirements: `pipenv install` or `pip install -r requirements.txt`
1. Initialize a local database with: `psql -d postgres -f db_reset.sql`
1. Download (TODO: timestamp checking) and load the csv data into the database:
`python init_load_data.py`
<br>.<br>.<br>.<br>
1. Profit


### TODO
- Update analysis
- Move to datadotworld instead of local database
- Create static visualization site
