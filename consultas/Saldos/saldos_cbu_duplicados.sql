select CTA_CBU, count(* )
from VTA_SALDOS vs inner join SALDOS s on JTS_OID_SALDO=JTS_OID
where vs.TZ_LOCK=0 and s.TZ_LOCK=0 and MONEDA <> 5
group by CTA_CBU
having count(*)>1