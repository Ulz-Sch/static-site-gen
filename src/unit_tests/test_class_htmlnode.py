import unittest

from htmlnode import *


class TestClassHTMLNode(unittest.TestCase):

    def test_none(self):
        node = HTMLNode(tag="a", value="Click me!",children=['a','b'] ,props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
        self.assertIsNotNone(node)
        self.assertIsNone(node2.value)
    
    def test_noteq(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "blank"})
        self.assertNotEqual(node,node2)

    def test_eq_false(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "targe": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "https://exampl.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    def test_eq_false3(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "https://exampl.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    def test_eq_false4(self):
        node = HTMLNode(tag="a", value="Click me!", props={"hre": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    def test_eq_false5(self):
        node = HTMLNode(tag="a", value="Click me", props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    def test_eq_false6(self):
        node = HTMLNode(tag="a", value="Click me", props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)
    def test_eq_false7(self):
        node = HTMLNode(tag="b", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
        self.assertEqual(node.props, node2.props)

    def test_repr(self):
        node = HTMLNode(tag="a", value="Click me!", props={"href": "https://example.com", "target": "_blank"})
 
        self.assertEqual(
            "HTMLNode(a, Click me!, [], {'href': 'https://example.com', 'target': '_blank'})", repr(node)
        )
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )
        
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )



if __name__ == "__main__":
    unittest.main()