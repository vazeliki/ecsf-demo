import openpyxl, json, sys, re
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src, data_only=True)
clean = lambda s: re.sub(r'\s*\n\s*', ' ', str(s)).replace('  ', ' ').strip() if s is not None else None
# Knowledge Areas sheet
ws = wb['Knowledge Areas']
kas, order = {}, []
for r in ws.iter_rows(min_row=5, values_only=True):
    dom, ka, name, desc, ki, kiname, typ, *_ = r[:12]
    tech = r[11]
    if not (ka and str(ka).startswith('KA') and ki): continue
    if ka not in kas:
        kas[ka] = {"id": ka, "name": clean(name), "domain": clean(dom), "description": clean(desc) or "", "items": []}
        order.append(ka)
    elif desc and not kas[ka]["description"]:
        kas[ka]["description"] = clean(desc)
    if typ not in ('F','C','Su','Sp'): print('WARN type', ki, typ)
    kas[ka]["items"].append({"id": ki, "name": clean(kiname), "type": typ, "tech": clean(tech)})
# Profiles x KAs
ws = wb['Profiles x KAs']
rows = list(ws.iter_rows(values_only=True))
hdr = rows[3]; codes = list(hdr[2:])
domains, profiles = [], {c: [] for c in codes}
for r in rows[4:]:
    if r[0] and not str(r[0]).startswith('KA') and not r[1]:
        domains.append({"name": clean(r[0]), "kas": []}); continue
    if not (r[0] and str(r[0]).startswith('KA')): continue
    ka = r[0]
    if ka not in kas: print('WARN missing KA', ka)
    domains[-1]["kas"].append(ka)
    for c, v in zip(codes, r[2:]):
        if v in ('F','C'): profiles[c].append({"id": ka, "type": v})
        elif v: print('WARN value', ka, c, v)
missing = [k for k in order if not any(k in d["kas"] for d in domains)]
if missing: print('WARN KAs not in matrix', missing)
data = {"source": "ECSF2_KnowledgeAreas_v1.xlsx",
        "domains": domains, "areas": [kas[k] for k in order], "profiles": profiles}
with open(out, 'w') as f:
    f.write("// Generated from ECSF2_KnowledgeAreas_v1.xlsx (sheets: 'Knowledge Areas', 'Profiles x KAs').\n")
    f.write("window.ECSF_KA = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")
print(len(order), 'KAs', sum(len(kas[k]['items']) for k in order), 'KIs', {c: len(v) for c, v in profiles.items()})
