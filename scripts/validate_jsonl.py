"""Check a chat fine-tuning file before you upload it to Microsoft Foundry.

Usage (no packages to install, Python 3.9+):
    python scripts/validate_jsonl.py assets/travel-finetune-hotel.jsonl

It checks what makes uploads or jobs fail:
  - the file really ends in .jsonl (not .jsonl.txt)
  - every line is valid JSON with a "messages" list
  - roles are system / user / assistant and every example ends with an assistant reply
  - there are at least 10 examples (the minimum for Azure OpenAI fine-tuning)
and prints a rough token count so you can estimate the training cost.
"""
import json
import sys
from pathlib import Path

MIN_EXAMPLES = 10
VALID_ROLES = {"system", "user", "assistant"}


def rough_tokens(text: str) -> int:
    # About 4 characters per token for English text: good enough for a cost estimate.
    return max(1, len(text) // 4)


def main(path_str: str) -> int:
    path = Path(path_str)
    problems = []

    if not path.exists():
        print(f"❌ File not found: {path}")
        return 1
    if path.suffix.lower() != ".jsonl":
        problems.append(f"File name ends in '{path.suffix}', not '.jsonl'. Rename it (e.g. remove a hidden .txt).")

    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append("File starts with a UTF-8 BOM. Save it as 'UTF-8' (without BOM).")

    examples, total_tokens = 0, 0
    for n, line in enumerate(raw.decode("utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as err:
            problems.append(f"Line {n}: not valid JSON ({err.msg}). Each example must be on ONE line.")
            continue
        msgs = obj.get("messages")
        if not isinstance(msgs, list) or not msgs:
            problems.append(f"Line {n}: missing a non-empty \"messages\" list.")
            continue
        roles = [m.get("role") for m in msgs]
        bad = [r for r in roles if r not in VALID_ROLES]
        if bad:
            problems.append(f"Line {n}: unknown role(s) {bad}. Use system, user, assistant.")
        if roles[-1] != "assistant":
            problems.append(f"Line {n}: the last message must be from the assistant (that's what the model learns).")
        if any(not str(m.get("content", "")).strip() for m in msgs):
            problems.append(f"Line {n}: a message has empty content.")
        examples += 1
        total_tokens += sum(rough_tokens(str(m.get("content", ""))) for m in msgs)

    if examples < MIN_EXAMPLES:
        problems.append(f"Only {examples} example(s). Azure OpenAI needs at least {MIN_EXAMPLES}.")

    print(f"File:      {path.name}")
    print(f"Examples:  {examples}")
    print(f"Tokens:    ~{total_tokens:,} per epoch (rough estimate)")
    if problems:
        print("\n❌ Fix these before uploading:")
        for p in problems:
            print("   -", p)
        return 1
    print("\n✅ Looks good. Upload this file in the fine-tuning wizard.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
