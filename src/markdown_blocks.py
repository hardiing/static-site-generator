def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split("\n\n")
    for block in sections:
        if block == "":
            continue
        block = block.strip()
        blocks.append(block)
    return blocks