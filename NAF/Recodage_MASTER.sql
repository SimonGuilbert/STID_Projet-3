update MASTER SET q6_8_cor = (
CASE
       WHEN NIV1="A" THEN "1"
       WHEN NIV1 IN ("B","C","D","E") THEN "2"
       WHEN NIV1="F" THEN "3"
       WHEN NIV1 IN ("G","H","I") THEN "4"
       WHEN NIV1="J" THEN  "5"
       WHEN NIV1="K" THEN  "6"
       WHEN NIV1="M" THEN  "7"
       WHEN NIV1="N" THEN  "8"
       WHEN NIV1="P" THEN  "9"
       WHEN NIV1="O" THEN  "10"
       WHEN NIV1="Q" THEN  "11"
       WHEN NIV1="R" THEN  "12"
       WHEN NIV1 IN ("L","S","T","U") THEN "13"
END
);
