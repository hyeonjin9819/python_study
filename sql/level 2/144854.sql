-- 코드를 입력하세요
-- 도서 ID, 저자명, 출판일
-- 경제 카테고리에 속하는것
-- 출판일 오름차순 정렬
SELECT book_id, author.author_name, TO_CHAR(published_date, 'yyyy-mm-dd') published_date
FROM book JOIN author
ON book.author_id = author.author_id
WHERE book.category = '경제'
ORDER BY published_date;