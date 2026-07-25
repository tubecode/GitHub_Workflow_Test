import os
from pathlib import Path

from google import genai

ROOT_DIR = Path(__file__).resolve().parent.parent
PROMPTS_DIR = ROOT_DIR / "prompts"
NOTEBOOK_DIR = ROOT_DIR / "notebook"
OUTPUT_DIR = ROOT_DIR / "doc"
WIKI_OUTPUT_DIR = ROOT_DIR / "wiki"


def find_prompt_files() -> list[Path]:
    return sorted(
        [
            path for path in PROMPTS_DIR.glob("*.txt")
            if path.is_file() and not path.name.startswith(".")
        ],
        key=lambda p: p.name,
    )


def find_notebook_files() -> list[Path]:
    return [
        path for path in NOTEBOOK_DIR.rglob("*")
        if path.is_file() and not path.name.startswith(".")
    ]


def create_client() -> genai.Client:
    api_key = os.environ.get("GENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GENAI_API_KEY is not set. Define it as a GitHub secret and pass it to the workflow."
        )
    return genai.Client(api_key=api_key)


def generate_documentation(client: genai.Client, prompt_text: str, source_path: Path) -> str:
    source_content = source_path.read_text(encoding="utf-8")
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            prompt_text,
            f"### Source file: {source_path.name}\n\n{source_content}",
        ],
        config={"temperature": 0.2},
    )
    return response.text


def write_output(output_text: str, target_path: Path) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(output_text, encoding="utf-8")


def main() -> None:
    prompt_files = find_prompt_files()
    if not prompt_files:
        print(f"No prompt files found in {PROMPTS_DIR}")
        return

    notebook_files = find_notebook_files()
    if not notebook_files:
        print(f"No notebook files found in {NOTEBOOK_DIR}")
        return

    client = create_client()
    print(f"Generating documentation for {len(notebook_files)} notebook file(s) using {len(prompt_files)} prompt file(s)")

    for source_path in notebook_files:
        for prompt_path in prompt_files:
            prompt_text = prompt_path.read_text(encoding="utf-8")
            markdown_output = generate_documentation(client, prompt_text, source_path)

            if prompt_path.stem.startswith("wiki-"):
                target_path = WIKI_OUTPUT_DIR / source_path.stem / f"{source_path.stem}-{prompt_path.stem}.md"
            else:
                target_path = OUTPUT_DIR / source_path.stem / f"{source_path.stem}-{prompt_path.stem}.md"

            print(f"- Processing {source_path.relative_to(ROOT_DIR)} with {prompt_path.name} -> {target_path.relative_to(ROOT_DIR)}")
            write_output(markdown_output, target_path)

    print("Documentation generation complete.")


if __name__ == "__main__":
    main()
