USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/paper_cite.csv' as line
FIELDTERMINATOR ';'
WITH line

MERGE (p:Paper {index: toInt(line.paper)})
MERGE (c:Paper {index: toInt(line.cited)})

create (p)-[:CITE]->(c)
;