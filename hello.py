from graphviz import Digraph

dot = Digraph(comment='The Round Table')

dot.node('A', 'Navid')
dot.node('B', 'Khar')
dot.node('L', 'Ast')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)
dot.render('test-output/round-table.gv', view=True)