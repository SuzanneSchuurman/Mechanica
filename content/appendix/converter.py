from pathlib import Path
import argparse
import yaml


def yaml_to_cards(data):
    if not isinstance(data, list):
        raise ValueError("YAML root must be a list of items.")

    cards = []

    for i, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise ValueError(f"Item #{i} is not a dictionary.")

        id = str(item.get("id") or "").strip()
        name = (item.get("name") or "").strip()
        url = (item.get("url") or "").strip()

        if not id:
            raise ValueError(f"Item #{i} is missing 'id'.")
        if not url:
            raise ValueError(f"Item #{i} is missing 'url'.")

        card = (
            f"```{{grasple}} {url}\n"
            f":label: {id}\n\n"
            f"{name}\n"
            f"```"
        )
        cards.append(card)

    return "\n\n".join(cards)


def main():
    parser = argparse.ArgumentParser(
        description="Convert a YAML file into a markdown file with card blocks."
    )
    parser.add_argument("input_file", help="Path to input YAML file")
    parser.add_argument("output_file", help="Path to output markdown file")

    args = parser.parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)

    with input_path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or []

    markdown = yaml_to_cards(data)

    with output_path.open("w", encoding="utf-8") as f:
        f.write(markdown + "\n")

    print(f"Wrote markdown cards to {output_path}")


if __name__ == "__main__":
    main()