## Create Table -lauseet ##

* CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(140) NOT NULL, 
	PRIMARY KEY (id)
);

* CREATE TABLE "match" (
	id INTEGER NOT NULL, 
	winner VARCHAR(144) NOT NULL, 
	opponent VARCHAR(144) NOT NULL, 
	date_when DATE, 
	score VARCHAR(50) NOT NULL, 
	event VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

* CREATE TABLE comment (
	id INTEGER NOT NULL, 
	content VARCHAR(250) NOT NULL, 
	matchid INTEGER NOT NULL, 
	name VARCHAR(144) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);


