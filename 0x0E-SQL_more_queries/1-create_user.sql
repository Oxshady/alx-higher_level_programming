-- create new user with privillage on mysql server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILLAGE ON "." 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
