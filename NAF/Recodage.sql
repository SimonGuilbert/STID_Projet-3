update table LP SET q_6_8_cor = (
CASE
       WHEN NIV1="A" THEN q_6_8_cor = "1"
       WHEN NIV1 IN ("B","C","D","E") THEN q_6_8_cor = "2"
       WHEN NIV1="F" THEN q_6_8_cor = "3"
       WHEN NIV1 IN ("G","H","I") THEN q_6_8_cor = "4"
       WHEN NIV1="J" THEN q_6_8_cor = "5"
       WHEN NIV1="K" THEN q_6_8_cor = "6"
       WHEN NIV1="M" THEN q_6_8_cor = "7"
       WHEN NIV1="N" THEN q_6_8_cor = "8"
       WHEN NIV1="P" THEN q_6_8_cor = "9"
       WHEN NIV1="O" THEN q_6_8_cor = "10"
       WHEN NIV1="Q" THEN q_6_8_cor = "11"
       WHEN NIV1="R" THEN q_6_8_cor = "12"
       WHEN NIV1 IN ("L","S","T","U") THEN q_6_8_cor = "13"
END
)
