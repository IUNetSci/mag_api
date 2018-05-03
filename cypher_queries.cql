Marcelo A. Carignano
10.1016/j.cplett.2015.06.032
2015
A statistical study of heterogeneous nucleation of ice by molecular dynamics

//Search Endpoint

MATCH (a:paper)
WHERE a.paper_year = '2015'
AND a.paper_title CONTAINS toLower('A statistical study of heterogeneous nucleation of ice by molecular dynamics')
AND a.doi = '10.1016/j.cplett.2015.06.032'
RETURN ID(a)

MATCH (a:paper)<-[:AUTHORED_BY]-(b:author)
WHERE b.normalized_name CONTAINS toLower('Marcelo A. Carignano')
RETURN ID(a)

MATCH (a:paper)
WHERE a.paper_year = 'year'
AND normalized_title CONTAINS toLower('title')
RETURN ID(a)

MATCH (a:paper)
WHERE a.paper_year = 'year'
AND doi = 'doi'
RETURN ID(a)

MATCH (a:paper)
WHERE normalized_title CONTAINS toLower('title')
AND doi = 'doi'
RETURN ID(a)

//References
MATCH (a:paper)-[:CITING]->(b:paper)
WHERE a.paper_year = '2015'
AND a.paper_title CONTAINS toLower('A statistical study of heterogeneous nucleation of ice by molecular dynamics')
AND a.doi = '10.1016/j.cplett.2015.06.032'
RETURN ID(b)

MATCH (c:paper)<-[:CITING]-(a:paper)<-[:AUTHORED_BY]-(b:author)
WHERE b.normalized_name CONTAINS toLower('Marcelo A. Carignano')
RETURN ID(c)

MATCH (a:paper)-[:CITING]->(b:paper)
WHERE a.paper_year = 'year'
AND a.normalized_title CONTAINS toLower('title')
RETURN ID(b)

MATCH (a:paper)-[:CITING]->(b:paper)
WHERE a.paper_year = 'year'
AND a.doi = 'doi'
RETURN ID(b)

MATCH (a:paper)-[:CITING]->(b:paper)
WHERE a.normalized_title CONTAINS toLower('title')
AND a.doi = 'doi'
RETURN ID(b)


//CITING
MATCH (a:paper)<-[:CITING]-(b:paper) 
WHERE b.paper_year = '2015'
AND a.paper_title CONTAINS toLower('A statistical study of heterogeneous nucleation of ice by molecular dynamics')
AND a.doi = '10.1016/j.cplett.2015.06.032'
RETURN ID(b)

MATCH (c:paper)<-[:CITING]-(a:paper)<-[:AUTHORED_BY]-(b:author)
WHERE b.normalized_name CONTAINS toLower('Marcelo A. Carignano')
RETURN ID(c)

MATCH (a:paper)<-[:CITING]-(b:paper)
WHERE a.paper_year = 'year'
AND a.normalized_title CONTAINS toLower('title')
RETURN ID(b)

MATCH (a:paper)<-[:CITING]-(b:paper)
WHERE a.paper_year = 'year'
AND a.doi = 'doi'
RETURN ID(b)

MATCH (a:paper)<-[:CITING]-(b:paper)
WHERE a.normalized_title CONTAINS toLower('title')
AND a.doi = 'doi'
RETURN ID(b)






CALL apoc.export.csv.query("
MATCH (a:paper)
a.paper_title CONTAINS toLower('A statistical study of heterogeneous nucleation of ice by molecular dynamics')
RETURN ID(a)",
"file/path/here.csv", {})
