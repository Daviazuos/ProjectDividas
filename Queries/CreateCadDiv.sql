CREATE TABLE IF NOT EXISTS cadDiv(
	Id serial PRIMARY KEY,
	name VARCHAR (50),
	valor FLOAT,
	numeroparcelas INTEGER,
	vencimento TIMESTAMP,
	TipoDeDivida VARCHAR (50));