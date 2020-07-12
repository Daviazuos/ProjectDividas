SELECT
 	value as hr
FROM
 	"Debts" as d
 	join "Parcel" as p on p.debtid = d.debtid

WHERE
 	parceltype = 'fixa'