update DeviceControlMessagesYun set resvdate = DATE_FORMAT(now(), '%Y-%m-%d'), atv=true;

select *
from DeviceControlMessagesYun
where time like "15:%"
order by resvdate, time;

select *
from DeviceControlMessagesYun
where isGroupMsg = TRUE;

 SELECT *
  FROM( SELECT *
       FROM DeviceControlMessagesYun
	   WHERE (atv = FALSE
	   AND isGroupMsg = TRUE
	   AND usrPk in (7,8))
       OR (atv = FALSE
	   AND usrPk in (7))
    	ORDER BY resvdate, time desc limit 7) d
  ORDER BY d.resvdate, d.time;


 SELECT *
from (SELECT *
  FROM( SELECT *
       FROM DeviceControlMessagesYun
	   WHERE (atv = FALSE AND isGroupMsg = TRUE AND usrPk in (7,8))
          OR (atv = FALSE AND usrPk in (7))) d
    WHERE CONCAT(d.resvdate,'_',`time`) < date_format('2019-08-07_11:28:00', '%Y-%m-%d_%H:%i:%s' )
  ORDER BY d.resvdate, d.time desc limit 7) d2
  ORDER BY d2.resvdate, d2.time;