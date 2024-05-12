--
-- File generated with SQLiteStudio v3.4.4 on Sat May 11 09:19:10 2024
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Restaurant
DROP TABLE IF EXISTS Restaurant;
CREATE TABLE IF NOT EXISTS Restaurant(
    name    TEXT PRIMARY KEY     NOT NULL,
    style    TEXT                 NULL,
    notes   TEXT                    NULL
);
INSERT INTO Restaurant (name, style, notes) VALUES ('Jimmy Johns', 'Fast Food', 'quick, cheap');
INSERT INTO Restaurant (name, style, notes) VALUES ('The District', 'American', 'Close by');
INSERT INTO Restaurant (name, style, notes) VALUES ('Egg Roll Plus', 'Asian', 'Closed Mondays');

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
