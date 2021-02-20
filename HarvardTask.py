import sys
import re
from collections import defaultdict, OrderedDict
import argparse
from multiprocessing import Pool
from cigarStringParser2 import snpDetector
from Bio import SeqIO
import networkx as nx
import subprocess
import clustering
from stringGraph import StringGraph, Node, Overlap, NodeCoords, Edge
import copy, operator


class Read(object):
    """docstring for Read"""
    def __init__(self, name, length, tgt_start, tgt_end, snp_coord, del_region):
        self.name = name
        self.length = length
        self.tgt_start = tgt_start
        self.tgt_end = tgt_end
        self.pos_var = {}
        self.pos_ref = {}
        for snp in snp_coord:
            self.pos_var[snp[0]] = snp[3]
            self.pos_ref[snp[0]] = snp[2]
        self.ori_var = copy.deepcopy(self.pos_var)
        self.deletionPos = set()
        for region in del_region:
            for pos in range(region[0], region[1]):
                    self.deletionPos.add(pos)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

