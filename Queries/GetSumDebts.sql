SELECT SUM(hr) from
((SELECT
 	value as hr
 FROM
 	"Debts" as d
 	join "Parcel" as p on p.debtid = d.debtid
 WHERE
 	EXTRACT(MONTH FROM p.duedate) = {}
 	and EXTRACT(YEAR FROM p.duedate) = {}
    and parceltype <> 'fixa')

UNION ALL

(SELECT
 	value as hr
FROM
 	"Debts" as d
 	join "Parcel" as p on p.debtid = d.debtid

WHERE
 	parceltype = 'fixa')) as a