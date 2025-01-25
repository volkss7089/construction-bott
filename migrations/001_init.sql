BEGIN TRANSACTION;
CREATE TABLE employees(
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    position TEXT DEFAULT 'Рабочий'
);
COMMIT;