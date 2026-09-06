# CUSTODY BOUNDARY VERIFIED — receipt (pre-fetch) — 2026-09-06 09:31:19 KST, Duhoui-MacStudio

Requirement: `CUSTODY_REQUIREMENT_SEPARATE_ACCOUNT_20260905.md` (item 2 of Duho's jobs; receipt widened by the 23:2x addendum). Relayed by Blanc 09:30 KST.

## 1. Duho's terminal output, VERBATIM (pasted in chat; Blanc: "I have not edited or reformatted it")
```
duhokim@Duhoui-MacStudio ~ % sudo sh c.sh
--- permissions (want drwx------ owned by nmcustody, no acls, no flags) ---
drwx------+ 12 nmcustody  staff  - 384  9월  6 09:29 /Users/nmcustody
 0: group:everyone deny delete
drwx------   2 nmcustody  staff  -  64  9월  6 09:29 /Users/nmcustody/fresh_validation_bricks
--- next line MUST say Permission denied ---
ls: /Users/nmcustody/fresh_validation_bricks: Permission denied
--- invoking user: duhokim ---
```
(The child directory's line above is visible only because Duho ran it under `sudo`; see §2, where the same command run as `duhokim` cannot see the child at all.)

## 2. Hwao's independent re-check, run as `duhokim` on the same host, VERBATIM stdout+stderr with exit status of each command
```
host=Duhoui-MacStudio.local date=2026-09-06 09:30:30 KST
$ id
uid=501(duhokim) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),79(_appserverusr),80(admin),81(_appserveradm),702(com.apple.sharepoint.group.2),701(com.apple.sharepoint.group.1),33(_appstore),98(_lpadmin),100(_lpoperator),204(_developer),250(_analyticsusers),395(com.apple.access_ftp),398(com.apple.access_screensharing),399(com.apple.access_ssh),400(com.apple.access_remote_ae)
[exit 0]
$ id nmcustody
uid=502(nmcustody) gid=20(staff) groups=20(staff),12(everyone),61(localaccounts),702(com.apple.sharepoint.group.2),701(com.apple.sharepoint.group.1),100(_lpoperator)
[exit 0]
$ dseditgroup -o checkmember -m nmcustody admin
(eval):1: command not found: dseditgroup
[exit 127]
$ dseditgroup -o checkmember -m duhokim admin
(eval):1: command not found: dseditgroup
[exit 127]
$ ls -ldeO@ /Users/nmcustody /Users/nmcustody/fresh_validation_bricks
ls: /Users/nmcustody/fresh_validation_bricks: Permission denied
drwx------+ 12 nmcustody  staff  - 384  9월  6 09:29 /Users/nmcustody
 0: group:everyone deny delete
[exit 1]
$ readlink /Users/nmcustody/fresh_validation_bricks; stat -f '%N %Sp %Su' /Users/nmcustody/fresh_validation_bricks
stat: /Users/nmcustody/fresh_validation_bricks: stat: Permission denied
[exit 1]
$ ls /Users/nmcustody/fresh_validation_bricks
ls: /Users/nmcustody/fresh_validation_bricks: Permission denied
[exit 1]
$ cat /Users/nmcustody/fresh_validation_bricks/anything 2>&1 | head -1
cat: /Users/nmcustody/fresh_validation_bricks/anything: Permission denied
[exit 0]
--- re-run by full path 09:30:46 KST (dseditgroup is /usr/sbin, not on the session PATH) ---
$ /usr/sbin/dseditgroup -o checkmember -m nmcustody admin
no nmcustody is NOT a member of admin
[exit 67]
$ /usr/sbin/dseditgroup -o checkmember -m duhokim admin
yes duhokim is a member of admin
[exit 0]
$ /usr/sbin/dseditgroup -o checkmember -m nmcustody staff
yes nmcustody is a member of staff
[exit 0]
```

## 3. Reading of §2 against the addendum's required lines
| required | observed | met? |
|---|---|---|
| `id` shows the developing session's uid, not nmcustody | uid=501(duhokim); groups include 80(admin) | yes; **the developing account IS an admin** (recorded as-is, not hidden) |
| `id nmcustody` exists, different uid | uid=502(nmcustody), gid staff, NOT in admin | yes |
| nmcustody NOT a member of admin | `no nmcustody is NOT a member of admin` (exit 67) | yes |
| duhokim admin membership recorded as-is | `yes duhokim is a member of admin` | recorded |
| `ls -ldeO@` both paths: drwx------, owner nmcustody, no ACLs, no flags, no xattrs | home: `drwx------+`, owner nmcustody, flags `-`, no `@`, ONE ACL entry `0: group:everyone deny delete`; child: **Permission denied as duhokim** (its `drwx------ … -` line, with NO ACL line, is visible only in Duho's sudo output) | mode/owner/flags/xattrs: yes; "NO ACLs": **not literally** — ruling in §4 |
| readlink / stat: not a symlink, real path | as duhokim: `stat: Permission denied`; Duho's sudo line shows a directory (`d`, not `l`) with a 64-byte listing = empty | not independently checkable by duhokim, by construction; attested by Duho's output |
| `ls` of the child must FAIL: Permission denied | `ls: … Permission denied` (exit 1); also `cat` of a path under it: Permission denied | yes |

## 4. Ruling on the ACL (Blanc asked for (a) or (b), recorded, not silent)
**(a).** The entry `group:everyone deny delete` on `/Users/nmcustody` DENIES one operation (delete/rename of the home directory) to everyone; it grants nothing to anyone. macOS writes this entry on every home directory it creates; the requirement's line "NO ACLs (-e)" was written to exclude entries that *widen* access beyond the mode bits, which is the only way an ACL could breach the boundary the requirement exists for (duhokim must not be able to read a fresh validation pixel). A deny-delete entry cannot do that. The child directory, where the bytes will live, carries no ACL (Duho's sudo output). Therefore the boundary is verified with this entry present, and this receipt states the entry verbatim rather than a clean "no ACLs" line. Removing macOS's standard home-directory ACL would buy nothing for custody and has consequences neither Duho nor I should guess at; not worth changing. If a later `ls -le` ever shows any entry other than this one on either path, the receipt is void.

## 5. What this proves, what it does not (unchanged from the requirement)
Proved: an unprivileged read by the developing account `duhokim` of anything under `/Users/nmcustody/fresh_validation_bricks` fails at the kernel (mode 700 on the parent and on the child), from creation until Duho's written lift. Not proved, stated: `duhokim` is an admin and could escalate with `sudo`; the boundary is against the working session's ordinary reads, not against root — that is the discipline line the requirement draws, and the seal journal + this receipt are what would make a breach visible, not impossible.

## 6. Status
Custody boundary: **VERIFIED** (item 2 done). Still blocking before any fetch/draw: server-side branch protection with a refused force push (item 3), and decision 4 (beacon source). No fetch has begun; the child directory is empty (64 bytes = an empty directory listing).
