select
	extract(month from vencimento),
	sum(valor)

from caddiv

where iscardcred = 'true' and extract(month from vencimento) > '01' and extract(year from vencimento) = {}

group by
	extract(month from vencimento),
	extract(year from vencimento)