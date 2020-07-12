SELECT SUM(hr), month from
((SELECT
  	EXTRACT(MONTH FROM p.duedate) as month,
 	value as hr
 FROM
 	"Cards" as d
 	join "ParcelCard" as p on p.cardid = d.cardid
 WHERE
 	EXTRACT(YEAR FROM p.duedate) = {}
 	and parceltype <> 'fixa')

UNION ALL

(SELECT
  	EXTRACT(MONTH FROM p.duedate) as month,
 	value as hr
 FROM
 	"Debts" as d
 	join "Parcel" as p on p.debtid = d.debtid
 WHERE
 	EXTRACT(YEAR FROM p.duedate) = {}
 	and parceltype <> 'fixa'
 )) as a
 group by month