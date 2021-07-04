-- creating application's user
CREATE USER hist_user WITH PASSWORD 'haslo12345';
-- changing password
ALTER USER hist_user WITH ENCRYPTED PASSWORD 'haslo12345';
-- creating database
CREATE DATABASE his_database_[LANG] WITH OWNER = hist_user;
-- removing database
DROP DATABASE IF EXISTS his_database_[LANG];
-- adding permission for tests
ALTER USER hist_user CREATEDB;