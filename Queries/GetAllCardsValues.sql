SELECT cardname, SUM(hr) ,duedate from
((SELECT
  	d.cardname as cardname,
 	sum(value) as hr,
 	d.duedate as duedate
 FROM
 	"Cards" as d
 	join "ParcelCard" as p on p.cardid = d.cardid
 WHERE
 	EXTRACT(MONTH FROM p.duedate) = {}
 	and EXTRACT(YEAR FROM p.duedate) = {}
  	and parceltype <> 'fixa'
  group by d.cardname, d.duedate)

UNION ALL

(SELECT
 	d.cardname,
 	sum(value) as hr,
 	d.duedate
 FROM
 	"Cards" as d
 	join "ParcelCard" as p on p.cardid = d.cardid

WHERE
 	parceltype = 'fixa'
 group by d.cardname, d.duedate
)) as a
group by cardname, duedate