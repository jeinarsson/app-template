#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 <<-EOSQL
    CREATE USER dbuser WITH PASSWORD 'dbpassword';
    CREATE DATABASE projectdb;
    GRANT ALL PRIVILEGES ON DATABASE projectdb TO dbuser;
EOSQL