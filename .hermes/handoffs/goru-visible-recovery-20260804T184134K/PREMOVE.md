# Goru visible-board recovery premove custody

Requested change: place live Goru above Tori on `ge-mastermind:Directors`.

Identity decision:
- Surviving source Goru: pane `%21` in `goru-agy`, `agy`, dead=0.
- Protected Tori target: pane `%39` in `ge-mastermind`, dead=0.
- Method Goru panes are not the requested source and remain untouched.
- Recovery method: add a nested read/write tmux client above `%39`; do not move/kill `%21` and do not kill or respawn `%39`.

## Pre-move metadata

CLIENT tty=/dev/ttys028 session=ge-mastermind size=171x49
CLIENT tty=/dev/ttys029 session=ge-mastermind size=227x57
WINDOW 0:Directors panes=4 size=171x48 layout=b7b0,171x48,0,0{60x48,0,0[60x25,0,0,25,60x22,0,26,38],62x48,61,0,0,47x48,124,0,39}
pane=0 id=%25 left=0 top=1 width=60 height=24 title=Yui-director role= master=Yui-director pid=10224 cmd=python3.11 cwd=/Users/duhokim/NebulaMind/NebulaMind dead=0 active=1 start="export NEBULAMIND_MASTERMIND=1 NEBULAMIND_DIRECTOR_ROLE=Yui-director; exec /Users/duhokim/.local/bin/hermes -p yui"
pane=1 id=%38 left=0 top=26 width=60 height=22 title=Kun-director role= master= pid=13791 cmd=python3.11 cwd=/Users/duhokim/NebulaMind/NebulaMind dead=0 active=0 start=
pane=2 id=%0 left=61 top=1 width=62 height=47 title=✳ Resuming previous coding session role= master=Hwao-director pid=4285 cmd=claude.exe cwd=/Users/duhokim/NebulaMind/NebulaMind dead=0 active=0 start="cd /Users/duhokim/NebulaMind/NebulaMind && export NEBULAMIND_MASTERMIND=1 NEBULAMIND_DIRECTOR_ROLE=Hwao-director NEBULAMIND_MASTER_ROOT=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind NEBULAMIND_METHOD1_HANDOFF_ROOT=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1 NEBULAMIND_METHOD2_HANDOFF_ROOT=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2 NEBULAMIND_METHOD3_HANDOFF_ROOT=/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3 NEBULAMIND_METHOD1_PUBLIC_ROOT=/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation NEBULAMIND_METHOD2_PUBLIC_ROOT=/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication NEBULAMIND_METHOD3_PUBLIC_ROOT=/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild NEBULAMIND_METHOD1_SESSION=mesh-ge-m1-packet:Mesh-m1 NEBULAMIND_METHOD2_SESSION=mesh-ge-m2-source:Mesh-m2 NEBULAMIND_METHOD3_SESSION=mesh-ge-m3-debate:Mesh-m3; printf \"\\nNebulaMind Galaxy Evolution Mastermind — Hwao-director\\nMaster root: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind\\nMethod1: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1\\nMethod2: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2\\nMethod3: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3\\n\\n\" '' '' '' '' '';  exec /Users/duhokim/.local/bin/claude --model fable --effort max"
pane=3 id=%39 left=124 top=1 width=47 height=47 title=Tori-director role= master= pid=42150 cmd=python3.11 cwd=/Users/duhokim/NebulaMind/NebulaMind dead=0 active=0 start=
SOURCE pane=0 id=%21 title=Duhoui-MacStudio.local pid=5946 cmd=agy cwd=/Users/duhokim/NebulaMind/NebulaMind dead=0 start=agy
