import math
# Datos del Caso
viajes=96000; km=41_000_000; camiones=374; audit=148+34; proy=430
torre=22                     # personas en la torre, Caso p.7
# Supuestos del Informe 1 (S-01 a S-03) que el profesor aceptó
vel=55; h_marcha_72=30       # km/h ; horas de marcha en 72 h
pos_marcha=30; pos_det=300   # s
tel_min=60                   # s
b_pos=64; b_tel=160; b_ev_72=32*1024; b_docs=195*1024; foto=300*1024; fotos=8
# Registros y bytes por camión en 72 h
rp=h_marcha_72*3600/pos_marcha + (72-h_marcha_72)*3600/pos_det
rt=h_marcha_72*3600/tel_min
reg=rp+rt+50
by=rp*b_pos+rt*b_tel+b_ev_72+b_docs
print(f"72 h: posiciones {rp:.0f}, telemetría {rt:.0f}, total registros ~{reg:.0f}")
print(f"72 h: bytes sin fotos {by/1e6:.2f} MB, fotos {fotos*foto/1e6:.2f} MB")
# Reconexión: 300 camiones (Caso 14.2, p.30)
N=300; msg=4096
m_cam=math.ceil(by/msg); print(f"mensajes de 4 KB por camión: {m_cam}; total {N*m_cam}")
for unid in (1,2,3):
    envios=max(100,12*unid); t=N*m_cam/envios
    subidas=1.67*unid
    print(f"S1 x{unid}: envíos {envios}/s -> {t/60:.1f} min; fotos una por archivo {N*fotos/subidas/60:.1f} min; fotos en un paquete por camión {N/subidas/60:.1f} min; conexiones nuevas {N/envios:.0f} s")
# Operación normal: un mensaje por minuto en marcha y uno cada 5 min detenido
h_marcha_dia=h_marcha_72/3
msg_dia=h_marcha_dia*60+(24-h_marcha_dia)*12
for flota in (camiones,proy):
    print(f"flota {flota}: {msg_dia:.0f} msj/día/camión -> {flota*msg_dia:,.0f} msj/día; más una reconexión {N*m_cam:,}")
reg_dia=(h_marcha_dia*3600/pos_marcha+(24-h_marcha_dia)*3600/pos_det+h_marcha_dia*3600/tel_min)
print(f"registros/día/camión {reg_dia:.0f}; EPS promedio flota 374: {camiones*reg_dia/86400:.1f}/s; 430: {proy*reg_dia/86400:.1f}/s")
print(f"EPS en la reconexión (300 x {reg:.0f} en 10 min): {N*reg/600:,.0f}/s")
# Asignación
print(f"viajes/día {viajes/365:.0f}; cota superior: 374 asignaciones en 1 h = {camiones/3600:.3f}/s; x10 consultas = {camiones*10/3600:.2f} TPS")
# Terminales: visitas y actualización remota solo en terminal (restricción 5)
visitas=camiones/6; print(f"visitas a terminal por día (flota/6): {visitas:.0f}; por terminal promedio {visitas/5:.1f}")
for img in (0.5,1.0):
    gb=visitas/5*img; mbps=gb*8e3/(8*3600)
    print(f"imagen {img} GB: {gb:.1f} GB/día por terminal -> {mbps:.1f} Mbit/s si se reparte en 8 h")
