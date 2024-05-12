-- Drop the table if it already exists
DROP TABLE IF EXISTS Restaurant;

-- Create the table
CREATE TABLE Restaurant(
    name    TEXT PRIMARY KEY     NOT NULL,
    style    TEXT                 NULL,
    notes   TEXT                    NULL,
);

-- Populate the table
INSERT INTO Restaurant VALUES
('Jimmy Johns','Fast Food','quick, cheap'),
('The District','American','Close by'),
('Egg Roll Plus','Asian','Closed Mondays')
;