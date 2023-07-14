-- An SQL script that creates an index idx_name_first on the table names
-- and the first letter of name
-- Requirements:
-- Import a table dump
-- Only the first letter of name must be indexed
CREATE INDEX idx_name_first_score ON names(name(1), score)