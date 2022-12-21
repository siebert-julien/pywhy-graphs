import re

import networkx as nx

from pywhy_graphs.viz import draw


def test_draw_pos_is_fully_given():
    """
    Ensure the Graphviz pos="x,y!" attribute is generated by the draw function when pos is given for all nodes.
    """
    # create a dummy graph x --> y <-- z and z --> x
    graph = nx.DiGraph([("x", "y"), ("z", "y"), ("z", "x")])
    # create a graph layout manually
    pos = {"x": [0, 0], "y": [1, 0], "z": [0.5, 0.7]}
    # draw the graphs
    dot = draw(graph, pos=pos)
    # get the graph description in textual form
    dot_body_text = "".join(dot.body)
    # assert that the produced graph contains the right pos argument for all nodes
    assert re.search(r"\tx \[.* pos=\"0,0!\"", dot_body_text) is not None
    assert re.search(r"\ty \[.* pos=\"1,0!\"", dot_body_text) is not None
    assert re.search(r"\tz \[.* pos=\"0.5,0.7!\"", dot_body_text) is not None


def test_draw_pos_is_partially_given():
    """
    Ensure the Graphviz pos="x,y!" attribute is generated by the draw function 
    when pos is given for some nodes but not all.
    """
    # create a dummy graph x --> y <-- z and z --> x
    graph = nx.DiGraph([("x", "y"), ("z", "y"), ("z", "x")])
    # create a graph layout manually
    pos = {"x": [0, 0], "y": [1, 0]}
    # draw the graphs
    dot = draw(graph, pos=pos)
    # get the graph description in textual form
    dot_body_text = "".join(dot.body)
    # assert that the produced graph contains the right pos argument for nodes x and y but not for z
    assert re.search(r"\tx \[.* pos=\"0,0!\"", dot_body_text) is not None
    assert re.search(r"\ty \[.* pos=\"1,0!\"", dot_body_text) is not None
    assert "pos=" not in re.search(r"\tz \[(.*)\]", dot_body_text).groups()[0]


def test_draw_pos_is_not_given():
    """
    Ensure the Graphviz pos="x,y!" attribute is not generated by the draw function when pos is not given.
    """
    # create a dummy graph x --> y <-- z and z --> x
    graph = nx.DiGraph([("x", "y"), ("z", "y"), ("z", "x")])
    # draw the graphs
    dot = draw(graph)
    # get the graph description in textual form
    dot_body_text = "".join(dot.body)
    # assert that the produced graph does not contain any pos argument for the nodes
    assert "pos=" not in dot_body_text


def test_draw_pos_contains_more_nodes():
    """
    Ensure the Graphviz pos="x,y!" attribute is generated by the draw function 
    when pos is given for some nodes but not all.
    """
    # create a dummy graph x --> y <-- z and z --> x
    graph = nx.DiGraph([("x", "y"), ("z", "y"), ("z", "x")])
    # create a graph layout manually
    pos = {"x": [0, 0], "y": [1, 0], "t": [1, 2], "w": [3, 4]}
    # draw the graphs
    dot = draw(graph, pos=pos)
    # get the graph description in textual form
    dot_body_text = "".join(dot.body)
    # assert that the produced graph contains the right pos argument for nodes x and y but not for z
    assert re.search(r"\tx \[.* pos=\"0,0!\"", dot_body_text) is not None
    assert re.search(r"\ty \[.* pos=\"1,0!\"", dot_body_text) is not None
    assert "pos=" not in re.search(r"\tz \[(.*)\]", dot_body_text).groups()[0]
