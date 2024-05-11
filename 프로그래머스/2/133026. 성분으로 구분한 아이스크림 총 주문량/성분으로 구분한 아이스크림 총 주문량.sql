-- 코드를 입력하세요
SELECT B.INGREDIENT_TYPE, SUM(TOTAL_ORDER)
FROM FIRST_HALF AS A 
JOIN ICECREAM_INFO AS B
ON A.FLAVOR = B.FLAVOR
GROUP BY B.INGREDIENT_TYPE