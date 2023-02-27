-- 코드를 입력하세요
-- 예약 환자 수, 진료과 코드별
-- appointment 테이블에서
-- 5월에 예약
-- 예약한 환자 수 오름차순 -> 진료과 코드 오름차순
SELECT mcdp_cd as "진료과코드", COUNT(mcdp_cd) as "5월예약건수"
FROM appointment
WHERE to_char(APNT_YMD, 'YYYY-MM') = '2022-05'
GROUP BY mcdp_cd
ORDER BY "5월예약건수" asc, mcdp_cd asc;