SELECT COUNT(books.author_id), authors.first, authors.last
FROM books, authors
WHERE books.author_id = authors.author_id
GROUP BY books.author_id

