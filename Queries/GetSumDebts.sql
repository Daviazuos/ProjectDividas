select sum(valor) from caddiv WHERE iscardcred = 'false' and EXTRACT(MONTH FROM vencimento) = {} and EXTRACT(YEAR FROM vencimento) = {} or tipodedivida = 'fixa'