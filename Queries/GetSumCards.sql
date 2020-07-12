SELECT SUM(hr) from
((SELECT
 	sum(value) as hr
 FROM
 	"Cards" as d
 	join "ParcelCard" as p on p.cardid = d.cardid
 WHERE
 	EXTRACT(MONTH FROM p.duedate) = {}
 	and EXTRACT(YEAR FROM p.duedate) = {}
 	and parceltype <> 'fixa')

UNION ALL

(SELECT
 	sum(value) as hr
 FROM
 	"Cards" as d
 	join "ParcelCard" as p on p.cardid = d.cardid

WHERE
 	parceltype = 'fixa')) as a