"""Codigo auxiliar de diagramacion: extractos del maestro -> LaTeX (Pandoc)."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'INFORME-MAESTRO.md'
text = SOURCE.read_text(encoding='utf-8')
OUT = ROOT / 'compacto'
OUT.mkdir(exist_ok=True)

def cut(start, end):
    a = text.index(start)
    return text[a:text.index(end, a)].strip()

def clean(s):
    s = re.sub(r'^---+\s*$', '', s, flags=re.M)
    s = re.sub(r'^> \[!\w+\]\s*$', '', s, flags=re.M)
    s = re.sub(r'\*\*\[(?:V|S|NV)\]\*\*', '', s)
    s = re.sub(r'^#{1,6}\s+(?:\d+(?:\.\d+)*\.?\s+)?(.+)$', r'## \1', s, flags=re.M)
    return s.strip()

pages = {
    '02': cut('## Resumen ejecutivo', '# 1. Marco legal chileno'),
    '03': cut('### 1. La Asimetría', '### 3. Ley N° 21.663'),
    '04': cut('### 3. Ley N° 21.663', '### 6. Traducción'),
    '05': cut('### 1. Marco internacional aplicable', '### 3. Comparativa de herramientas'),
    '06': cut('### 3. Comparativa de herramientas', '### 4. Cierre del subdocumento'),
    '07': cut('### 1. Enfoque Metodológico', '#### 3.3 Impacto Económico'),
    '09': cut('### 4. Análisis de Sensibilidad', '# 4. Arquitectura'),
    '10': cut('#### 1. Delimitación de Fronteras', '#### 2. Privacidad por Arquitectura'),
    '11': cut('#### 2. Privacidad por Arquitectura', '## Síntesis de integración'),
    '12': cut('## Síntesis de integración', '# Referencias'),
}

pages['04'] = re.sub(r'```.*?```', '', pages['04'], flags=re.S)
pages['04'] = re.sub(r'\*Lectura de la figura\.\*.*?(?=Se identificaron)', '', pages['04'], flags=re.S)
pages['04'] += '''
## Mapa de organismos

| Organismo | Dependencia y función descritas en el maestro |
| :--- | :--- |
| ANCI y CSIRT Nacional | Ministerio de Seguridad Pública. Seguridad, coordinación y recepción de incidentes. |
| Agencia de Protección de Datos Personales | Ministerio de Economía. Fiscalización del tratamiento de datos; el maestro la reporta no constituida al corte. |
| Secretaría de Gobierno Digital | Subsecretaría de Hacienda. Transformación digital y estándares del Estado. |
| Dirección del Trabajo | Control de jornada y límites del monitoreo laboral por GPS. |

**Aplicabilidad al caso:** el maestro no acredita la calificación de Curimón como OIV. La condición de servicio esencial y la eventual designación como OIV deben distinguirse; las obligaciones adicionales de OIV no se presentan como una designación comprobada.
'''
pages['05'] = re.sub(r'##### Justificación del aporte.*?(?=Ninguna de las certificadoras)', '', pages['05'], flags=re.S)
pages['07'] = pages['07'].replace('La matriz\ncompleta constituye el **Anexo A**; el cuerpo recoge', 'El cuerpo recoge')
pages['07'] = pages['07'].replace('y se detallan en el Anexo A.', 'y requieren el detalle final de asignación por obligación.')
pages['07'] += '''
## Trazabilidad de las obligaciones restantes

| Obligación | Actividad y rol | Plazo / partida del maestro |
| :--- | :--- | :--- |
| Base de licitud | Consentimiento o fundamento documentado; DPO y Legal | Antes del tratamiento / bolsa de 255 UF |
| Evaluación de impacto | EIPD previa al monitoreo; DPO y Legal | Etapa 1 / bolsa de 255 UF |
| Decisiones automatizadas | Causal de bloqueo y revisión humana; operación | Antes de despacho / costo absorbido |
| Datos sensibles | Acceso restringido y finalidad; CISO y DPO | Desde diseño / costo absorbido |
| Contratos de encargo | DPA con transportistas; Legal | Antes del encargo / bolsa de 255 UF |
| Transferencias | Revisión de cláusulas; Legal | Antes del flujo / bolsa de 255 UF |
| Derechos de titulares | Canal de atención y trazabilidad; DPO | 30 días corridos según maestro / absorbido |
| Avisos a clientes | Escalamiento contractual; CISO | Según contrato / costo absorbido |

*Nota editorial:* esta tabla ordena las ocho obligaciones mencionadas en el maestro. La bolsa de 255 UF es compartida, no un costo por fila; la distribución individual no está desglosada en el texto consolidado.
'''
pages['10'] = re.sub(r'```.*?```', '\n\nARQUITECTURA_VECTORIAL\n\n', pages['10'], flags=re.S)

diagram = r'''\begin{center}
\begin{tikzpicture}[box/.style={draw=teal,fill=pale,rounded corners=2pt,align=center,font=\footnotesize,text width=14.5cm,inner sep=4pt},arr/.style={-{Stealth},thick,teal},node distance=3mm]
\node[box] (a) {\textbf{Titulares y activos}\\196 conductores propios · 258 externos · 148 transportistas\\374 camiones · 84 clientes corporativos};
\node[box,below=of a] (b) {\textbf{Captura e ingesta}\\App móvil y telemetría celular · búfer local cifrado de 8 GB\\Satélite transaccional de respaldo · TLS / mTLS};
\node[box,below=of b] (c) {\textbf{Azure Chile Central · frontera del encargado}\\API Management · WAF · servicio de jornada · revisión humana\\RAT y derechos · cifrado de campo AES-256-GCM\\Key Vault Premium: 686 claves · evidencias inmutables};
\node[box,below=of c] (d) {\textbf{Continuidad y transferencias}\\Réplica East US 2 · ruta a Mendoza\\Cláusulas contractuales y control de acceso a claves};
\node[box,below=of d] (e) {\textbf{Respuesta diferenciada}\\CSIRT: 3 h / actualización / cierre · sin datos personales\\Brecha de datos: sin dilación · avisos al mandante según contrato};
\draw[arr] (a)--(b);\draw[arr] (b)--(c);\draw[arr] (c)--(d);\draw[arr] (d)--(e);
\end{tikzpicture}
\end{center}
{\footnotesize\textbf{Figura 1.} Rediagramación del mapa de arquitectura del informe maestro.}
'''

for number, content in pages.items():
    result = subprocess.run(['pandoc', '--from=markdown+tex_math_dollars', '--to=latex', '--wrap=none'], input=clean(content), text=True, encoding='utf-8', capture_output=True, check=True).stdout
    result = result.replace('ARQUITECTURA\\_VECTORIAL', diagram)
    result = result.replace('\\,\\%', '\\%')
    result = result.replace('\\,%', '\\%')
    if number == '09':
        result = result.replace('\\[', '{\\small\\[').replace('\\]', '\\]}')
    (OUT / f'{number}.tex').write_text(result, encoding='utf-8')
print('Extractos LaTeX generados:', ', '.join(pages))
