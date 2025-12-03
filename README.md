# docker-kub
Docker with Kub
## Overview

This repository contains Docker and Kubernetes learning material. The following content will be used to create a README.md inside every directory under the repository root (starting from "docker-hub"). Each generated README should describe that directory's purpose and list its immediate contents.

## Per-directory README template

Use this template for every folder README.md:

# <folder-name>

Short description of this folder's purpose.

Contents
- files and subfolders (one-line description each)

How to use
- Quick instructions to run or build artifacts from this folder

Related
- Links to related folders or top-level docs

Notes
- Any prerequisites or special notes

## Automatic generation scripts

Bash (Linux / WSL / Git Bash)
```bash
# Run from the repository root (docker-hub)
find . -type d -print0 | while IFS= read -r -d '' dir; do
    name="$(basename "$dir")"
    readme="$dir/README.md"
    {
        echo "# ${name:-root}"
        echo
        echo "Short description of the ${name:-root} folder."
        echo
        echo "Contents"
        echo
        # list immediate children (files and dirs) with short descriptions placeholder
        for item in "$dir"/* "$dir"/.*; do
            [ -e "$item" ] || continue
            base="$(basename "$item")"
            # skip parent/current dirs
            [ "$base" = "." ] || [ "$base" = ".." ] && continue
            if [ -d "$item" ]; then
                echo "- ${base}/ — (subfolder)"
            else
                echo "- ${base} — (file)"
            fi
        done
        echo
        echo "How to use"
        echo
        echo "- Describe how to use files in this folder."
        echo
        echo "Related"
        echo
        echo "- Link to parent or related READMEs."
        echo
    } > "$readme"
done
```

PowerShell (Windows)
```powershell
# Run from the repository root (docker-hub)
Get-ChildItem -Directory -Recurse -Force | ForEach-Object {
    $dir = $_.FullName
    $name = $_.Name
    $readme = Join-Path $dir 'README.md'
    $children = Get-ChildItem -LiteralPath $dir -Force | Sort-Object PSIsContainer -Descending, Name
    $lines = @()
    $lines += "# $name"
    $lines += ""
    $lines += "Short description of the $name folder."
    $lines += ""
    $lines += "Contents"
    foreach ($c in $children) {
        if ($c.PSIsContainer) { $lines += "- $($c.Name)/ — (subfolder)" }
        else { $lines += "- $($c.Name) — (file)" }
    }
    $lines += ""
    $lines += "How to use"
    $lines += ""
    $lines += "- Describe how to use files in this folder."
    $lines += ""
    $lines += "Related"
    $lines += ""
    $lines | Out-File -FilePath $readme -Encoding utf8
}
```

## Manual checklist after generation

- Review each README and replace placeholder descriptions with real information.
- Add usage examples, commands, and links to parent/related topic READMEs.
- Commit the generated README.md files.

## Example top-level entries to consider documenting

- experiments/ — ad-hoc experiments and playbooks
- images/ — Dockerfile images, build instructions
- k8s/ — Kubernetes manifests, Helm charts
- docs/ — architecture notes, tutorials
- scripts/ — helper scripts for building and deploying

Use the automatic scripts to create initial README.md files and then edit them to reflect actual content and instructions for your learning material.