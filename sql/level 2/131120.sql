-- 코드를 입력하세요
-- 여성, 생일 3월, 전화번호 NULL -> 출력대상 제외
-- Member_Profile에서
-- 회원 ID -> 오름차순, 이름, 성별, 생년월일 조회
SELECT
    MEMBER_ID, MEMBER_NAME, GENDER, TO_CHAR(DATE_OF_BIRTH, 'YYYY-MM-DD') as DATE_OF_BIRTH
FROM member_profile
WHERE gender = 'W' AND TLNO IS NOT NULL AND TO_CHAR(date_of_birth, 'MM') = 03
ORDER BY member_id;