# Meaningful Use exploration

### Goals
This is a project inspired by the Medicare Meaningful Use attestation datasets.
I'll use it to practice some Flask and D3 skills, and play around with libraries
new to me, like Folium.


### Usage
1. Clone the repository
1. Set up and activate a new `python3` virtual environment for the project
1. Install the project requirements: `pip install -r requirements.txt`
1. Initialize a local database with: `psql -d postgres -f db_reset.sql`
1. Download (TODO: timestamp checking) and load the csv data into the database:
`python init_load_data.py`
<br>.<br>.<br>.<br>
7. Profit


*Note: working through the notebook will additionally require:*
`pip install jupyter`
