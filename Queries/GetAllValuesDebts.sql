(SELECT 
 	debtname, value, duedate 
 FROM 
 "Debts" as d 
 join "Parcel" as p on p.debtid = d.debtid 
 
 WHERE 
 EXTRACT(MONTH FROM p.duedate) = {}
 and EXTRACT(YEAR FROM p.duedate) = {})
 
 UNION 
 
 (SELECT 
  	debtname, value, duedate 
  FROM
  "Debts" as d 
  join "Parcel" as p on p.debtid = d.debtid 
  WHERE 
  parceltype = 'fixa')