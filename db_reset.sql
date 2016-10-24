-- easiest to run with `psql -d postgres -f db_reset.sql`
-- this ensures current user is the creator of the new db

DROP DATABASE IF EXISTS ehr_mu;
CREATE DATABASE ehr_mu;
\c ehr_mu
\q
