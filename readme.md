# Tools to convert SQL DDL into data dictionaries and ERD diagrams


# Process flow

* Read the source SQL DDL
* Build a Graph from the Tables, optionally filtered
* Execute the specified Commands
    * Create an ERD diagram
    * Create data dictionaries
    * Report on the Graph
    * Etc

# Data Graph

* A Graph of Nodes and their Relations
    * Nodes have a Table object
    * Relations are added based on related Tables

* Produced by the GraphBuilder