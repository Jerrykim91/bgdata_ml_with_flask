-- 자치구 목록 가져오기
SELECT * FROM tbl_areas;

-- 용산구의 ID 
SELECT gu_id FROM tbl_areas WHERE gu='용산구';

-- 용산구의 행정구역 gps를 가져와라
-- 이 쿼리를 이용하여 gps를 제공하는 API 제공
tbl_areasSELECT * FROM tbl_gps WHERE gu_id=1;
SELECT * FROM tbl_gps
WHERE gu_id=(SELECT gu_id FROM tbl_areas WHERE gu='용산구');