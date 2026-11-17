#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把各批章节内容插入骨架，生成最终单文件 HTML"""
import sys, pathlib

BASE = pathlib.Path(__file__).parent
ROOT = BASE.parent


def load(name):
    ns = {}
    code = (BASE / name).read_text(encoding='utf-8')
    exec(compile(code, name, 'exec'), ns)
    return {k: v for k, v in ns.items() if k.startswith('CH_')}


# 第 0-11 章
core = ''.join(load(f'chapters_{c}.py')['CH_' + c.upper()] for c in 'abcde')

# 切掉旧的 summary 章（id="summary"），后面用 chapters_k.py 的新版替换
idx = core.index('<section class="chapter" id="summary"')
end = core.rindex('</section>', 0, idx) + len('</section>')
core = core[:end]

# 第 12-18 章
part_f = load('chapters_f.py')['CH_F']
part_g = load('chapters_g.py')['CH_G']
part_h = load('chapters_h.py')['CH_H']
part_i = load('chapters_i.py')['CH_I']
part_j = load('chapters_j.py')
part_j_text = part_j['CH_J'] + part_j['CH_K']
part_k = load('chapters_k.py')['CH_SUMMARY']

chapters = core + part_f + part_g + part_h + part_i + part_j_text + part_k

html_path = ROOT / 'index.html'
html = html_path.read_text(encoding='utf-8')
if '<!-- REST_CHAPTERS -->' not in html:
    # 锚点已被替换（非首次运行）——重新跑骨架脚本恢复锚点
    import subprocess
    subprocess.run([sys.executable, str(BASE / 'build_skeleton.py')], check=True, cwd=str(ROOT))
    html = html_path.read_text(encoding='utf-8')
assert '<!-- REST_CHAPTERS -->' in html, 'anchor missing'
html = html.replace('<!-- REST_CHAPTERS -->', chapters)

out = ROOT / 'index.html'
out.write_text(html, encoding='utf-8')
print('最终文件大小:', round(len(html) / 1024), 'KB')
print('章节数量:', html.count('<section class="chapter"'))
