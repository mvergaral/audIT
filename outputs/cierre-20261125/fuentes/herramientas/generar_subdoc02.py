import os
import re

# Read MD drafts
with open("../../07_Entrega_2/borradores_subdocumentos/AUDIT-Subdocumento2.md", "r", encoding="utf-8") as f:
    md_main = f.read()

with open("../../07_Entrega_2/borradores_subdocumentos/AUDIT-Subdocumento2-Anexos.md", "r", encoding="utf-8") as f:
    md_anexos = f.read()

print(f"Read main: {len(md_main)} chars, anexos: {len(md_anexos)} chars")
