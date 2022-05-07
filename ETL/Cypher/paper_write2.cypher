USING PERIODIC COMMIT
LOAD CSV WITH HEADERS FROM
'file:///home/paper_write.csv' AS line
FIELDTERMINATOR ';'
WITH line

MERGE (author:Author {name: line.author})
MERGE (p:Paper {index: toInt(line.paper)})

CREATE (author)-[:WRITE]->(p)
;