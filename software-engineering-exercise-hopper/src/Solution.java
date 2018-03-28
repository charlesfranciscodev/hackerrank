import java.io.*;
import java.util.*;

class Solution {
  public static void main(String[] args) throws Exception {
    Outline outline = new Outline();
    outline.readStandardInput();
  }
}

class Outline {
  void readStandardInput() throws Exception {
    InputStream inputStream = new FileInputStream(new File("input.txt"));
    BufferedReader br = new BufferedReader(new InputStreamReader(inputStream)); // or System.in
    List<Heading> headings = new ArrayList<>();
    for (String line = br.readLine(); line != null; line = br.readLine()) {
      headings.add(parse(line));
    }
    Node outline = toOutline(headings);
    String html = toHtml(outline);
    System.out.println(html);
  }

  private Node toOutline(List<Heading> headings) {
    // TODO
    Node root = new Node(new Heading(0, ""));
    List<Node> list = new ArrayList<>();
    int prevWeight = 0;
    for (Heading heading : headings) {
      if (heading.weight == 1) {
        Node n = new Node(heading);
        root.children.add(n);
        n.parent = root;
        list.add(n);
        continue;
      } else if (heading.weight < prevWeight) {
        toOutline2(list);
        while (heading.weight <= list.get(list.size() - 1).heading.weight) {
          list.remove(list.size() - 1);
        }
      }
      list.add(new Node(heading));
      prevWeight = heading.weight;
    }
    toOutline2(list);
    System.err.println(root);
    return root;
  }

  private void toOutline2(List<Node> list) {
    int i = 0;
    while (i < list.size() - 1) {
      Node n1 = list.get(i);
      Node n2 = list.get(i + 1);
      if (n1.heading.weight < n2.heading.weight) {
        n1.children.add(n2);
        n2.parent = n1;
      } else if (n1.heading.weight == n2.heading.weight) {
        n1.parent.children.add(n2);
        n2.parent = n1.parent;
      }
      i++;
    }
  }

  /** Parses a line of input.
   This implementation is correct for all predefined test cases. */
  private Heading parse(String record) {
    String[] parts = record.split(" ", 2);
    int weight = Integer.parseInt(parts[0].substring(1));
    return new Heading(weight, parts[1].trim());
  }

  /** Converts a node to HTML.
   This implementation is correct for all predefined test cases. */
  private static String toHtml(Node node) {
    StringBuilder buf = new StringBuilder();
    if (!node.heading.text.isEmpty()) {
      buf.append(node.heading.text);
      buf.append("\n");
    }
    Iterator<Node> iter = node.children.iterator();
    if (iter.hasNext()) {
      buf.append("<ol>");

      while (iter.hasNext()) {
        Node child = iter.next();
        buf.append("<li>");
        buf.append(toHtml(child));
        buf.append("</li>");
        if (iter.hasNext()) {
          buf.append("\n");
        }
      }
      buf.append("</ol>");
    }
    return buf.toString();
  }

  class Heading {
    int weight;
    String text;

    Heading(int weight, String text) {
      this.weight = weight;
      this.text = text;
    }

    @Override
    public String toString() {
      return "Heading{" +
          "weight=" + weight +
          ", text='" + text + '\'' +
          '}';
    }
  }

  class Node {
    Heading heading;
    List<Node> children;
    Node parent;

    Node(Heading heading) {
      this.heading = heading;
      this.children = new ArrayList<>();
    }

    @Override
    public String toString() {
      StringBuilder builder = new StringBuilder();
      builder.append("{ heading=");
      builder.append(heading);
      builder.append(", children=[");
      for (Node child : children) {
        builder.append(child);
        builder.append(",\n");
      }
      builder.append("], ");
      if (parent != null) {
        builder.append("parent=");
        builder.append(parent.heading.text);
        builder.append(",");
      }
      builder.append(", weight=");
      builder.append(heading.weight);
      builder.append('}');
      return builder.toString();
    }
  }
}
