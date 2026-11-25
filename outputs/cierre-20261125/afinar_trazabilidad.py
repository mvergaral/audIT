from pathlib import Path
O=Path(__file__).resolve().parent;B=O/'fuentes'
p=B/'anexos/observaciones-informe3.tex';t=p.read_text(encoding='utf-8')
t=t.replace('La tabla de respuestas se consolida en este anexo independiente del Art. 46°.','La tabla de respuestas se consolida en la sección del Art. 46° del documento SUBDOC00, separada del cuerpo de los subdocumentos.')
t=t.replace('T-14, T-15 y T-18 fueron integrados por D2 en el cierre de planificación.','T-14, T-15 y T-18 incorporan una tabla propia de uso de IA y distinguen la revisión humana pendiente de la edición final.')
t=t.replace('La línea al sistema contable lleva el rótulo «Internet del emisor»','La línea al sistema contable lleva el rótulo «Documentos tributarios por internet del emisor»')
p.write_text(t,encoding='utf-8')
p=B/'subdocumentos/09-calidad/formularios/catalogo-T-17.tex';t=p.read_text(encoding='utf-8')
t=t.replace('Staging Azure Multi-Region.','Staging entre los sitios primario y secundario admisibles; el fixture identifica proveedor, recursos, versiones y mecanismo de réplica homologado conforme a R-24.')
t=t.replace('Promover la base de datos réplica de PostgreSQL y TimescaleDB en el sitio secundario aprobado a nodo primario de lectura/escritura.','Promover la réplica consistente de PostgreSQL y TimescaleDB del sitio secundario aprobado a lectura/escritura mediante el mecanismo homologado e identificado en el fixture.')
t=t.replace('Escalar los microservicios en el clúster AKS del sitio secundario aprobado de 2 a 8 pods por servicio.','Restablecer la capacidad de los microservicios en el sitio secundario mediante los recursos homologados del fixture. En la rama Azure con AKS, comprobar el escalado de 2 a 8 pods por servicio; en otra rama admisible, comprobar la capacidad equivalente sin presumir AKS.')
t=t.replace('Redirigir el tráfico global en Azure Front Door hacia la IP pública del sitio secundario aprobado.','Conmutar el punto de entrada hacia el endpoint homologado del sitio secundario aprobado, conservando autenticación, autorización y trazabilidad. En la rama Azure se verifica la regla correspondiente de Front Door; el fixture de otra rama identifica su mecanismo equivalente.')
phrase='Una plataforma sin exportación autorizada no se declara integrada ni aprobada por registrar la restricción en el acta. Para esa plataforma se obtiene una vía de acceso o extracción autorizada y homologada, se ejecuta la misma muestra y se comprueban sus criterios; si no existe evidencia suficiente, el resultado es no conforme y se escala antes de aceptar H5/H10, sin rebajar unilateralmente el requisito ni sustituir la muestra real por un doble sintético.'
needle='documentando en el acta de H5/H10 cualquier restricción real de exportación y su mecanismo de contingencia.'
t=t.replace(needle,needle+' '+phrase)
p.write_text(t,encoding='utf-8')
p=B/'subdocumentos/09-calidad/formularios/T-13.tex';t=p.read_text(encoding='utf-8')
t+='\n'+r'\paragraph{Tratamiento de la plataforma sin exportación autorizada}'+'\n'+phrase+'\n'
p.write_text(t,encoding='utf-8')
print('Afinados localizadores y criterios de aceptación; las condiciones futuras no se declaran ejecutadas.')
