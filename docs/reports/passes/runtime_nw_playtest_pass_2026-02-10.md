# Runtime NW Playtest Pass (2026-02-10)

## Scope
- Validate NW.js launch behavior after local runtime install.
- Confirm engine-level startup reaches data loading in this environment.
- Confirm all protagonist overworld sheets are structurally valid for RPG Maker MZ.

## Findings
1. Default NW launch modes in this environment can fail RPG Maker startup with:
   - `Error: Your browser does not support WebGL.`
   - Triggered in `SceneManager.checkBrowser` (`js/rmmz_managers.js`).
2. Stable runtime smoke launch was achieved with software WebGL fallback flags:
   - `--ignore-gpu-blocklist`
   - `--use-angle=swiftshader`
   - `--enable-unsafe-swiftshader`
   - `--enable-webgl`
3. With those flags, startup progressed through core runtime file loads (`data/*.json`, fonts, plugins) and remained alive for timeout-window smoke execution.

## Protagonist Sprite Validation
- Verified runtime sheets for all 13 protagonists in `img/characters/$ce_*.png`.
- All sheets matched expected MZ single-character format:
  - Resolution: `144x256` (`3x4` frames, `48x64` per frame)
- No blank direction frames detected in down/left/right/up rows.

## Project Changes
- Added reusable smoke runner:
  - `tools/run_nw_playtest.sh`
- Updated tools docs with runtime command:
  - `tools/README.md`
- Added npm alias for CI/local convenience:
  - `package.json` (`playtest:nw`)

## Command
```bash
tools/run_nw_playtest.sh
```

## Note
- This pass validates launch/runtime viability in this specific environment.
- It does not replace manual gameplay QA (map traversal, battle flow, quest progression).
