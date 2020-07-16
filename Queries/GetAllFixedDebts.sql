SELECT SUM(hr) from
((SELECT
 	value as hr
 FROM
 	"Cards" as d
 	join "ParcelCard" as p on p.cardid = d.cardid
 WHERE
 	parceltype = 'fixa')

UNION ALL

(SELECT
 	value as hr
 FROM
 	"Debts" as d
 	join "Parcel" as p on p.debtid = d.debtid
 WHERE
 	parceltype = 'fixa'
 )) as a
