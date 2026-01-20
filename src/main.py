from textnode import TextNode, TextType

def main():
    new_object = TextNode("this is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_object)

main()