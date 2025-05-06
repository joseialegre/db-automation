with reservas as (
select r.SALDO_JTS_OID jts, sum(r.importe_origen) totReservas
from VTA_RESERVAS r
where r.estado =1 and r.TZ_LOCK = 0
group by SALDO_JTS_OID)
SELECT jts, totReservas, c2627, s.*
FROM reservas inner join SALDOS s on jts= s.JTS_OID
WHERE s.C2627 <> -1 * totReservas