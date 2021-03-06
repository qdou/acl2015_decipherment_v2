import sys
import numpy
import numpy.linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pyplot
import fileinput


_, filename = sys.argv

""" 1. form a data matrix """

phrase_id_files = [
    't_sne.output.top100'
]
'''
phrase_dict = {}
for line in fileinput.input(phrase_id_files):
    fields = line.split()
    phrase = fields[:-1]
    phrase_id = fields[-1].strip()
    phrase_dict[phrase_id] = ' '.join(phrase)
'''
print 'here'
xs = []
ys = []
phrase_table = []
for line in open(filename):
    phrase_id, x, y = line.split('\t')
    phrase_id = phrase_id.strip()
    x = float(x)
    y = float(y)
    xs.append(x)
    ys.append(y)
    #phrase_table.append(phrase_dict[phrase_id])
    phrase_table.append(phrase_id)

png = '{}.viz.png'.format(filename)
print 'Saving the plot to:', png

fig, ax = pyplot.subplots(figsize=(200, 200))
ax.scatter(xs, ys, color='w')
for i, phrase in enumerate(phrase_table):
    if 'magis' in phrase:
        print 'yes'
        ax.annotate(phrase.decode('utf-8'), (float(xs[i]), float(ys[i])), fontsize='large',color='green')
    else :
        ax.annotate(phrase.decode('utf-8'), (float(xs[i]), float(ys[i])), fontsize='medium')

ax.set_xlabel('t-sne 1', fontsize='medium')
ax.set_ylabel('t-sne 2', fontsize='medium')
ax.set_xticks([])
ax.set_yticks([])
ax.set_title(filename, fontsize='medium')
fig.savefig(png)
