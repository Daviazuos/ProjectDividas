(SELECT
	*
FROM
	"Cards" as d join
	"ParcelCard" as p on p.cardid = d.cardid

WHERE
	EXTRACT(MONTH FROM p.duedate) = {}
	and EXTRACT(YEAR FROM p.duedate) = {}
	and d.cardname = {})
UNION
(SELECT
	*
FROM
	"Cards" as d join
	"ParcelCard" as p on p.cardid = d.cardid

WHERE
	parceltype = 'fixa'
	and d.cardname = {})